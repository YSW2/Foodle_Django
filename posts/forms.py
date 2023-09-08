from django import forms
from posts.models import Post, Comment

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'post',
            'content',
        ]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "내용 입력.."
                }
            ),
        }