from django import forms
from .models import Pais, Estado, Cidade


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


class EstadoForm(forms.ModelForm):
    class Meta:
        model=Estado
        fields=['estado', 'ativo']
        labels={'estado':'Estado', 'ativo':'Ativo'}
        widget={'estado':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class CidadeForm(forms.ModelForm):
    class Meta:
        model=Cidade
        fields=['cidade', 'ativo']
        labels={'cidade':'Cidade', 'ativo':'Ativo'}
        widget={'cidade':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})