from django import forms
from fridge.models import Fridge

class FridgeForm(forms.ModelForm):
    class Meta:
        model = Fridge
        fields = [
            'name',
            'exp_date',
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "식품명"
                }
            ),
            "exp_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }
