from django import forms

from .models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'slug', 'tag', 'photographer', 'image', 'content']
