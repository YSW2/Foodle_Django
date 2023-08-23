from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tags',
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "제목"
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "내용"
                }
            ),
        }