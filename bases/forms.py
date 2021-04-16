from django import forms
from .models import Pais


class PaisForm(forms.ModelForm):
    class Meta:
        model=Pais
        fields=['pais', 'ativo']
        labels={'pais':'Pais', 'ativo':'Ativo'}
        widget={'pais':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


    