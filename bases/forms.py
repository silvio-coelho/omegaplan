from django import forms
from .models import Pais, Estado, Cidade


class PaisForm(forms.ModelForm):
    class Meta:
        model=Pais
        #fields=['pais', 'ddi', 'sigla', 'usuario_criou', 'ativo']
        fields=['pais', 'ddi', 'sigla', 'ativo']
        labels={'pais':'Pais', 'ddi':'Ddi', 'sigla':'Sigla', 'usuario_criou': 'Criado Por', 'ativo':'Ativo'}
        widget={
            'pais':forms.TextInput, 
            'ddi':forms.TextInput, 
            'sigla':forms.TextInput,
            'ativo': forms.CheckboxInput(
                attrs={
                    'class': 'text-align-left col-md-1'
                })
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['ativo'].widget.attrs.update({'class':'form-control text-align-left col-md-1'})


class EstadoForm(forms.ModelForm):
    class Meta:
        model=Estado
        fields=['pais', 'estado', 'uf', 'ativo']
        labels={'pais':'Pais', 'estado':'Estado', 'uf':'Uf', 'ativo':'Ativo'}
        widget={'pais':forms.ModelChoiceField, 'estado':forms.TextInput, 'uf':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class CidadeForm(forms.ModelForm):
    class Meta:
        model=Cidade
        fields=['estado', 'cidade', 'codigo_municipio','ativo']
        labels={'estado':'Estado', 'cidade':'Cidade', 'codigo_municipio':'Codigo do Municipio', 'ativo':'Ativo'}
        widget={'estado':forms.ModelChoiceField, 'cidade':forms.TextInput, 'codigo_municipio':forms.IntegerField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})