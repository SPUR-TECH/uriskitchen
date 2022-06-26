from .models import Comment, DessertComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'comment_writer')

        widgets = {

            'body': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Comment here.....'}),
                'comment_writer': forms.HiddenInput()
        }


class DessertCommentForm(forms.ModelForm):
    class Meta:
        model = DessertComment
        fields = ('body', 'dessert_comment_writer')

        widgets = {

            'body': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Comment here.....'}),
                'dessert_comment_writer': forms.HiddenInput()
        }
