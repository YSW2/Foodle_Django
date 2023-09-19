from asgiref.sync import sync_to_async, async_to_sync
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseServerError
from fridge.models import Fridge
from fridge.forms import FridgeForm
from django.views.decorators.http import require_POST
from fridge import barcode, getinfo
from bs4 import BeautifulSoup
from fridge import openai_api
import json
# Create your views here.

def fridge_view(request):
    user = request.user
    fridge = Fridge.objects.filter(user=user)
    fridge_form = FridgeForm()

    context = {
        "fridge": fridge,
        "fridge_form": fridge_form
    }
    return render(request, "fridge/fridge.html", context)

@require_POST
def fridge_add(request):
    form = FridgeForm(request.POST)
    print(request.POST)

    if form.is_valid():
        print(form)
        fridge = form.save(commit=False)
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
    bot = openai_api.openai_bot()
    food_list = Fridge.objects.filter(user=user).values_list('name')
    food_query = ''
    for food in food_list:
        food_query += food[0]

    recipe = await bot.getquery(f"{food_query} 이 식재료들로 만들 음식 레시피 한개 알려줘. 모든 재료를 사용할 필요는 없어.")
    print(recipe)
    context = {
        "recipe": recipe,
    }
    return JsonResponse(context)

def test(request):
    jsonObject = json.loads(request.body)
    print(jsonObject.get('title'))
    return JsonResponse(jsonObject)

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