from django.shortcuts import render, redirect
from fridge.models import Fridge
from fridge.forms import FridgeForm
from django.views.decorators.http import require_POST

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
    if request.method == "POST":
        form = FridgeForm(request.POST)

        if form.is_valid():
            fridge = form.save(commit=False)
            fridge.user = request.user
            fridge.save()

            return redirect("fridge:fridge")
    else:
        fridge_form = FridgeForm()

    context = {
        "fridge_form": fridge_form,
    }

    return render(request, "fridge/fridge_add.html", context)

@require_POST
def fridge_delete(request, fridge_id):
    fridge = Fridge.objects.get(id=fridge_id)
    fridge.delete()

    return redirect("fridge:fridge")