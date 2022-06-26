from .models import Comment, DessertComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'comment_writer')

        widgets = {

            'comment': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Comment here.....'}),
            'comment_writer': forms.HiddenInput()
        }


class DessertCommentForm(forms.ModelForm):
    class Meta:
        model = DessertComment
        fields = ('comment', 'dessert_comment_writer')

        widgets = {

            'comment': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Comment here.....'}),
            'dessert_comment_writer': forms.HiddenInput()
        }
