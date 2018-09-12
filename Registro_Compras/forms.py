from django import forms

from .models import Registros

class PostForm(forms.ModelForm):

    class Meta:
        model = Registros
        fields = ('compra',)