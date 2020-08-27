from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type yourcomment',
        'id': 'usercomment',
        'rows': '4'

    }))

    class Meta:
        model = Comment
        fields = ('content', )
