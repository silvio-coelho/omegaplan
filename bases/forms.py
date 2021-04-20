from django import forms
from .models import Pais, Estado, Cidade, OrgaoPublico, Imovel, TipoProjeto, Projeto, Obra, Arquivo


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
        fields=['estado', 'cidade', 'ddd', 'sigla', 'codigo_municipio', 'ativo']
        labels={'estado':'Estado', 'cidade':'Cidade', 'ddd':'Ddd', 'sigla':'Sigla', 'codigo_municipio':'Codigo do Municipio', 'ativo':'Ativo'}
        widget={'estado':forms.ModelChoiceField, 'cidade':forms.TextInput, 'ddd':forms.TextInput, 'sigla':forms.TextInput, 'codigo_municipio':forms.IntegerField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class OrgaoPublicoForm(forms.ModelForm):
    class Meta:
        model=OrgaoPublico
        fields=['cidade', 'orgao_publico', 'ativo']
        labels={'cidade':'Cidade', 'orgao_publico':'Órgão Público', 'ativo':'Ativo'}
        widget={'cidade':forms.ModelChoiceField, 'orgao_publico':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

    
class ImovelForm(forms.ModelForm):
    class Meta:
        model=Imovel
        fields=['orgao_publico', 'imovel', 'endereco', 'ativo']
        labels={'orgao_publico':'Órgão Público', 'imovel':'Imóvel', 'endereco':'Endereço', 'ativo':'Ativo'}
        widget={'orgao_publico':forms.ModelChoiceField, 'imovel':forms.TextInput, 'endereco':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class TipoProjetoForm(forms.ModelForm):
    class Meta:
        model=TipoProjeto
        fields=['tipo_projeto', 'ativo']
        labels={'tipo_projeto':'Tipo de Projeto', 'ativo':'Ativo'}
        widget={'tipo_projeto':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class ProjetoForm(forms.ModelForm):
    class Meta:
        model=Projeto
        fields=['imovel', 'tipo_projeto', 'projeto', 'ativo']
        labels={'imovel':'Imóvel', 'tipo_projeto':'Tipo de Projeto', 'projeto':'Projeto', 'ativo':'Ativo'}
        widget={'imovel':forms.ModelChoiceField, 'tipo_projeto':forms.ModelChoiceField, 'projeto':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class ObraForm(forms.ModelForm):
    class Meta:
        model=Obra
        fields=['projeto', 'obra', 'ativo']
        labels={'projeto':'Projeto', 'obra':'Obra', 'ativo':'Ativo'}
        widget={'projeto':forms.ModelChoiceField, 'obra':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class ArquivoForm(forms.ModelForm):
    class Meta:
        model=Arquivo
        fields=['projeto', 'titulo', 'arquivo', 'ativo']
        labels={'projeto':'Projeto', 'titulo':'Titulo', 'arquivo':'Arquivo', 'ativo':'Ativo'}
        widget={'projeto':forms.ModelChoiceField, 'titulo':forms.TextInput, 'arquivo':forms.FileField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})