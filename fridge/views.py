from asgiref.sync import sync_to_async, async_to_sync
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseServerError
from fridge.models import Fridge
from fridge.forms import FridgeForm
from django.views.decorators.http import require_POST
from fridge import barcode, getinfo
from bs4 import BeautifulSoup
from fridge import openai_api
from datetime import datetime
import json
# Create your views here.


def fridge_view(request):
    today = int(datetime.now().strftime("%d"))
    user = request.user
    fridge = Fridge.objects.filter(user=user).order_by('exp_date')
    fridge_form = FridgeForm()

    for f in fridge:
        if f.exp_date and f.exp_date.day - today < 1:
            f.danger_mode = True
        else:
            f.danger_mode = False

    context = {
        "fridge": fridge,
        "fridge_form": fridge_form
    }
    return render(request, "fridge/fridge.html", context)

@require_POST
def fridge_add(request):
    form = FridgeForm(request.POST)

    if form.is_valid():
        fridge = form.save(commit=False)
        if fridge.exp_date is None:
            fridge.exp_date_exist = False
            fridge.exp_date = datetime(9999, 12, 31)
        fridge.user = request.user
        fridge.save()
    else:
        print("not valid")

    return redirect("fridge:fridge")

@require_POST
def fridge_delete(request, fridge_id):
    fridge = Fridge.objects.get(id=fridge_id)
    fridge.delete()

    return redirect("fridge:fridge")


async def get_recipe(request):
    user = request.user
    food_list = Fridge.objects.filter(user=user).values_list('name')
    food_query = ''
    for food in food_list:
        food_query += food[0]

    recipe = await openai_api.chat_bard(f"{food_query} 중에서 몇 가지를 골라 만들 수 있는 음식 레시피 한 개 검색해줘")
    print(recipe)
    context = {
        "recipe": recipe,
    }
    return JsonResponse(context)

def barcode_scan(request):
    code = barcode.scanning()
    # code = '5000394123618'
    html_content = getinfo.getname(code)

    soup = BeautifulSoup(html_content, 'html.parser')

    # 상품명 추출
    product_name = soup.find('h3').text.strip()

    # 결과 출력
    print("상품명:", product_name)

    if product_name == "":
        return HttpResponseServerError("인식이 불가한 상품입니다")

    else:
        context = {
            "value": product_name,
        }
    return JsonResponse(context)