from django import forms

from .models import *

class PaisForm(forms.ModelForm):
    class Meta:
        model=Pais
        fields=['descricao', 'ativo']
        labels={'descricao':'Descrição', 'ativo':'Ativo'}
        widget={'descricao':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})