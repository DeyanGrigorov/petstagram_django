from django import forms

from petstagram_django.common.models import Comment


class CommentForm(forms.Form):
    comment = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control rounded-2'
        })
    )

    class Meta:
        model = Comment
        fields = ('text',)

