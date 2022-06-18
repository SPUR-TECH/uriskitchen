from .models import Comment, DessertComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {

            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class DessertCommentForm(forms.ModelForm):
    class Meta:
        model = DessertComment
        fields = ('body',)

        widgets = {

            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
