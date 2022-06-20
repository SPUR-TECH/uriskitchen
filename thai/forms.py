from .models import Comment, DessertComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {

            'name': forms.CharField(max_length=120),
            'body': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Comment here.....'})
        }


class DessertCommentForm(forms.ModelForm):
    class Meta:
        model = DessertComment
        fields = ('body',)

        widgets = {

            'name': forms.CharField(max_length=120),
            'body': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Comment here.....'})
        }
