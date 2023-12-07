from django import forms
from . import models


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"

class ClienteBuscarForm(forms.ModelForm):
        sexo = forms.CharField()
        


class EstudioForm(forms.ModelForm):
    class Meta:
        model = models.Estudios
        fields = ["estudios_cursados"]