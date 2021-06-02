from django.db import models
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import \
LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.forms import model_to_dict


# Create your views here.

from django.views import generic
from django.urls import reverse_lazy
from . models import Pais, Estado, Cidade, OrgaoPublico, Imovel, TipoObra, \
    Projeto, ProjetoAnexo, Obra#, Arquivo
from . forms import PaisForm, EstadoForm, CidadeForm, OrgaoPublicoForm, ImovelForm, \
    TipoObraForm, ProjetoForm, ObraForm#, ArquivoForm


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'parciais/dashboard.html'
    login_url = "bases:login"   


class PaisView(LoginRequiredMixin, generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Pais
    template_name = "bases/paises_list.html"
    context_object_name = "obj"
    login_url = "bases:login"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Lista de Países"
        context['entity'] = "País"
        context['breadcrumb'] = "Países"
        context['list_url'] = reverse_lazy("bases:pais_list")
        context['add_url'] = reverse_lazy("bases:pais_new")
        context['table_id'] = 'tabela_paises'
        return context
    

class PaisNew(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Pais
    template_name = 'bases/pais_form.html'
    context_object_name = "obj"
    form_class = PaisForm
    success_url = reverse_lazy("bases:pais_list")
    login_url = "bases:login"
    success_message = "País criado com sucesso!"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.instance.usuario_criou = self.request.user
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novo País"
        context['entity'] = "País"
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

  
class PaisEdit(SuccessMessageMixin, generic.UpdateView):
    model = Pais
    template_name = 'bases/form.html'
    context_object_name = 'obj'
    form_class = PaisForm
    success_url = reverse_lazy("bases:pais_list")
    login_url='bases:login'
    success_message = "País atualizado com sucesso!"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                form.instance.usuario_modificou_id = self.request.user.id
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar País"
        context['entity'] = "País"
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context


class PaisDelete(LoginRequiredMixin, generic.DeleteView):
    model = Pais
    template_name = 'bases/delete.html'
    success_url = reverse_lazy('bases:pais_list')
    #permission_required = 'delete_pais'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('entrou no post')
        print(request.POST)
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Apagar um país'
        context['entity'] = 'País'
        context['list_url'] = self.success_url
        return context


class EstadoView(LoginRequiredMixin, generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Estado
    template_name = "bases/estados_list.html"
    context_object_name = "obj"
    login_url = "bases:login"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Lista de Estados"
        context['entity'] = "Estado"
        context['breadcrumb'] = "Estados"
        context['list_url'] = reverse_lazy("bases:estado_list")
        context['add_url'] = reverse_lazy("bases:estado_new")
        context['table_id'] = 'tabela_estados'
        return context
    

class EstadoNew(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Estado
    template_name = 'bases/estado_form.html'
    context_object_name = "obj"
    form_class = EstadoForm
    success_url = reverse_lazy("bases:estado_list")
    login_url = "bases:login"
    success_message = "Estado criado com sucesso!"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.instance.usuario_criou = self.request.user
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novo Estado"
        context['entity'] = "Estado"
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

  
class EstadoEdit(SuccessMessageMixin, generic.UpdateView):
    model = Estado
    template_name = 'bases/estado_form.html'
    context_object_name = 'obj'
    form_class = EstadoForm
    success_url = reverse_lazy("bases:estado_list")
    login_url='bases:login'
    success_message = "Estado atualizado com sucesso!"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                form.instance.usuario_modificou_id = self.request.user.id
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Estado"
        context['entity'] = "Estado"
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context


class EstadoDelete(LoginRequiredMixin, generic.DeleteView):
    model = Estado
    template_name = 'bases/estado_delete.html'
    success_url = reverse_lazy('bases:estado_list')
    #permission_required = 'delete_pais'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('entrou no post')
        print(request.POST)
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Apagar um Estado'
        context['entity'] = 'Estado'
        context['list_url'] = self.success_url
        return context


class CidadeView(LoginRequiredMixin, generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Cidade
    template_name = "bases/cidades_list.html"
    context_object_name = "obj"
    login_url = "bases:login"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Lista de Cidades"
        context['entity'] = "Cidade"
        context['breadcrumb'] = "Cidades"
        context['list_url'] = reverse_lazy("bases:cidade_list")
        context['add_url'] = reverse_lazy("bases:cidade_new")
        context['table_id'] = 'tabela_cidades'
        return context
    

class CidadeNew(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Cidade
    template_name = 'bases/cidade_form.html'
    context_object_name = "obj"
    form_class = CidadeForm
    success_url = reverse_lazy("bases:cidade_list")
    login_url = "bases:login"
    success_message = "Cidade criado com sucesso!"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.instance.usuario_criou = self.request.user
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nova Cidade"
        context['entity'] = "Cidade"
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

  
class CidadeEdit(SuccessMessageMixin, generic.UpdateView):
    model = Cidade
    template_name = 'bases/cidade_form.html'
    context_object_name = 'obj'
    form_class = CidadeForm
    success_url = reverse_lazy("bases:cidade_list")
    login_url='bases:login'
    success_message = "Cidade atualizada com sucesso!"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                form.instance.usuario_modificou_id = self.request.user.id
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Cidade"
        context['entity'] = "Cidade"
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context
        
"""     def form_valid(self, form):
        form.instance.usuario_modificou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)
 """


class CidadeDelete(LoginRequiredMixin, generic.DeleteView):
    model = Cidade
    template_name = 'bases/cidade_delete.html'
    success_url = reverse_lazy('bases:cidade_list')
    #permission_required = 'delete_pais'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('entrou no post')
        print(request.POST)
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Apagar uma Cidade'
        context['entity'] = 'Cidade'
        context['list_url'] = self.success_url
        return context


class OrgaoPublicoView(LoginRequiredMixin, generic.ListView):
    #permission_required = "inv.view_categoria"
    model = OrgaoPublico
    template_name = "bases/orgaospublicos_list.html"
    context_object_name = "obj"
    login_url = "bases:login"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Lista de Órgãos Publicos"
        context['entity'] = "Órgão Público"
        context['breadcrumb'] = "Órgãos Públicos"
        context['list_url'] = reverse_lazy("bases:orgaopublico_list")
        context['add_url'] = reverse_lazy("bases:orgaopublico_new")
        context['table_id'] = 'tabela_orgaospublicos'
        return context
    

class OrgaoPublicoNew(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = OrgaoPublico
    template_name = 'bases/orgaopublico_form.html'
    context_object_name = "obj"
    form_class = OrgaoPublicoForm
    success_url = reverse_lazy("bases:orgaopublico_list")
    login_url = "bases:login"
    success_message = "Órgão Público criado com sucesso!"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.instance.usuario_criou = self.request.user
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novo Órgão Público"
        context['entity'] = "Órgão Publico"
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


""" class PaisEdit(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    def form_valid(self, form):
        form.instance.usuario_criou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)
 """
  
class OrgaoPublicoEdit(SuccessMessageMixin, generic.UpdateView):
    model = OrgaoPublico
    template_name = 'bases/orgaopublico_form.html'
    context_object_name = 'obj'
    form_class = OrgaoPublicoForm
    success_url = reverse_lazy("bases:orgaopublico_list")
    login_url='bases:login'
    success_message = "Órgão Público atualizado com sucesso!"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                form.instance.usuario_modificou_id = self.request.user.id
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Órgão Publico"
        context['entity'] = "Órgão Público"
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context
        
"""     def form_valid(self, form):
        form.instance.usuario_modificou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)
 """


class OrgaoPublicoDelete(LoginRequiredMixin, generic.DeleteView):
    model = OrgaoPublico
    template_name = 'bases/orgaopublico_delete.html'
    success_url = reverse_lazy('bases:orgaopublico_list')
    #permission_required = 'delete_pais'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('entrou no post')
        print(request.POST)
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Apagar um Órgão Público'
        context['entity'] = 'Órgão Público'
        context['list_url'] = self.success_url
        return context


class ImovelView(LoginRequiredMixin, generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Imovel
    template_name = "bases/imoveis_list.html"
    context_object_name = "obj"
    login_url = "bases:login"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Lista de Imóveis"
        context['entity'] = "Imóvel"
        context['breadcrumb'] = "Imóveis"
        context['list_url'] = reverse_lazy("bases:imovel_list")
        context['add_url'] = reverse_lazy("bases:imovel_new")
        context['table_id'] = 'tabela_imoveis'
        return context
    

class ImovelNew(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Imovel
    template_name = 'bases/imovel_form.html'
    context_object_name = "obj"
    form_class = ImovelForm
    success_url = reverse_lazy("bases:imovel_list")
    login_url = "bases:login"
    success_message = "Imóvel criado com sucesso!"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.instance.usuario_criou = self.request.user
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novo Imóvel"
        context['entity'] = "Imóvel"
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

  
class ImovelEdit(SuccessMessageMixin, generic.UpdateView):
    model = Imovel
    template_name = 'bases/imovel_form.html'
    context_object_name = 'obj'
    form_class = ImovelForm
    success_url = reverse_lazy("bases:imovel_list")
    login_url='bases:login'
    success_message = "Imóvel atualizado com sucesso!"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                form.instance.usuario_modificou_id = self.request.user.id
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Imóvel"
        context['entity'] = "Imóvel"
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context


class ImovelDelete(LoginRequiredMixin, generic.DeleteView):
    model = Imovel
    template_name = 'bases/imovel_delete.html'
    success_url = reverse_lazy('bases:imovel_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('entrou no post')
        print(request.POST)
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Apagar um Imóvel'
        context['entity'] = 'Imóvel'
        context['list_url'] = self.success_url
        return context


class TipoObraView(LoginRequiredMixin, generic.ListView):
    #permission_required = "inv.view_categoria"
    model = TipoObra
    template_name = "bases/tiposobra_list.html"
    context_object_name = "obj"
    login_url = "bases:login"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Lista de Tipos de obra"
        context['entity'] = "Tipo de obra"
        context['breadcrumb'] = "Tipos de obra"
        context['list_url'] = reverse_lazy("bases:tiposobra_list")
        context['add_url'] = reverse_lazy("bases:tiposobra_new")
        context['table_id'] = 'tabela_tiposobra'
        return context
    

class TipoObraNew(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = TipoObra
    template_name = 'bases/tiposobra_form.html'
    context_object_name = "obj"
    form_class = TipoObraForm
    success_url = reverse_lazy("bases:tiposobra_list")
    login_url = "bases:login"
    success_message = "Tipo de obra criado com sucesso!"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.instance.usuario_criou = self.request.user
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novo Tipo de obra"
        context['entity'] = "Tipo de obra"
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

  
class TipoObraEdit(SuccessMessageMixin, generic.UpdateView):
    model = TipoObra
    template_name = 'bases/tiposobra_form.html'
    context_object_name = 'obj'
    form_class = TipoObraForm
    success_url = reverse_lazy("bases:tiposobra_list")
    login_url='bases:login'
    success_message = "Tipo de obra atualizado com sucesso!"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                form.instance.usuario_modificou_id = self.request.user.id
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Tipo de obra"
        context['entity'] = "Tipo de obra"
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context


class TipoObraDelete(LoginRequiredMixin, generic.DeleteView):
    model = TipoObra
    template_name = 'bases/tiposobra_delete.html'
    success_url = reverse_lazy('bases:tiposobra_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('entrou no post')
        print(request.POST)
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Apagar um Tipo de obra'
        context['entity'] = 'Tipo de obra'
        context['list_url'] = self.success_url
        return context


class ProjetoView(LoginRequiredMixin, generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Projeto
    template_name = "bases/projetos_list.html"
    context_object_name = "obj"
    login_url = "bases:login"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Lista de Projetos"
        context['entity'] = "Projeto"
        context['breadcrumb'] = "Projetos"
        context['list_url'] = reverse_lazy("bases:projeto_list")
        context['add_url'] = reverse_lazy("bases:projeto_new")
        context['table_id'] = 'tabela_projetos'
        return context
    

class ProjetoNew(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Projeto
    template_name = 'bases/projeto_form.html'
    context_object_name = "obj"
    form_class = ProjetoForm
    success_url = reverse_lazy("bases:projeto_list")
    login_url = "bases:login"
    success_message = "Projeto criado com sucesso!"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        arquivos = request.FILES.getlist('arquivos')
        print(arquivos)
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.instance.usuario_criou = self.request.user
                data = form.save()
                projeto = data
                print('data depois de gravar', data)
                data = model_to_dict(data)
                print('data depois model dict', data)

                for arquivo in arquivos:
                    anexo = ProjetoAnexo.objects.create(
                        projeto=projeto,
                        arquivo=arquivo,
                    )



            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novo Projeto"
        context['entity'] = "Projeto"
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

  
class ProjetoEdit(SuccessMessageMixin, generic.UpdateView):
    model = Projeto
    template_name = 'bases/projeto_form.html'
    context_object_name = 'obj'
    form_class = ProjetoForm
    success_url = reverse_lazy("bases:projeto_list")
    login_url='bases:login'
    success_message = "Projeto atualizado com sucesso!"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                form.instance.usuario_modificou_id = self.request.user.id
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Projeto"
        context['entity'] = "Projeto"
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context


class ProjetoDelete(LoginRequiredMixin, generic.DeleteView):
    model = Projeto
    template_name = 'bases/projeto_delete.html'
    success_url = reverse_lazy('bases:projeto_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('entrou no post')
        print(request.POST)
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Apagar um Projeto'
        context['entity'] = 'Projeto'
        context['list_url'] = self.success_url
        return context


class ObraView(LoginRequiredMixin, generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Obra
    template_name = "bases/obras_list.html"
    context_object_name = "obj"
    login_url = "bases:login"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Lista de Obras"
        context['entity'] = "Obra"
        context['breadcrumb'] = "Obras"
        context['list_url'] = reverse_lazy("bases:obra_list")
        context['add_url'] = reverse_lazy("bases:obra_new")
        context['table_id'] = 'tabela_obras'
        return context


class ObraDetail(LoginRequiredMixin, generic.DetailView):
    model = Obra
    template_name = "bases/obra_detail.html"
    context_object_name = "obj"
    login_url = "bases:login"
    

class ObraNew(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Obra
    template_name = 'bases/obra_form.html'
    context_object_name = "obj"
    form_class = ObraForm
    success_url = reverse_lazy("bases:obra_list")
    login_url = "bases:login"
    success_message = "Obra criada com sucesso!"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.instance.usuario_criou = self.request.user
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nova Obra"
        context['entity'] = "Obra"
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

  
class ObraEdit(SuccessMessageMixin, generic.UpdateView):
    model = Obra
    template_name = 'bases/obra_form.html'
    context_object_name = 'obj'
    form_class = ObraForm
    success_url = reverse_lazy("bases:obra_list")
    login_url='bases:login'
    success_message = "Obra atualizada com sucesso!"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                form.instance.usuario_modificou_id = self.request.user.id
                data = form.save()
                data = model_to_dict(data)
            else:
                data['error'] = 'Não foi informado uma ação'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Obra"
        context['entity'] = "Obra"
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context


class ObraDelete(LoginRequiredMixin, generic.DeleteView):
    model = Obra
    template_name = 'bases/obra_delete.html'
    success_url = reverse_lazy('bases:obra_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('entrou no post')
        print(request.POST)
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Apagar uma Obra'
        context['entity'] = 'Obra'
        context['list_url'] = self.success_url
        return context


# def UploadView(request):
#     if request.method == 'POST':
#         form = ArquivoForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.instance.usuario_criou = request.user
#             form.save()
#             return HttpResponse('The file is saved')
#     else:
#         form = ArquivoForm()
#         context = {
#             'form':form,
#         }
#     return render(request, 'bases/upload_arquivo.html', context)