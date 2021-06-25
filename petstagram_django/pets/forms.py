from django import forms

from petstagram_django.pets.models import Pets


class PetForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = '__all__'


