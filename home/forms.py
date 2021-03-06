from django import forms

from .models import Contact, Hero


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['image', 'caption', 'sub_heading']
