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

    def __init__(self, *args, **kwargs):
        super(FridgeForm, self).__init__(*args, **kwargs)

        # 'name' 필드를 필수 필드로 설정
        self.fields['exp_date'].required = False