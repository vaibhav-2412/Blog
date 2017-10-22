from django import forms

from .models import articles

class PostForm(forms.ModelForm):

    class Meta:
        model = articles
        fields = ('title', 'text',)
