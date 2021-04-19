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
from . models import Pais, Estado, Cidade
from . forms import PaisForm, EstadoForm, CidadeForm


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


class PaisEdit(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    def form_valid(self, form):
        form.instance.usuario_criou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)

  
class PaisEdit(SuccessMessageMixin, generic.UpdateView):
    model = Pais
    template_name = 'bases/pais_form.html'
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
                form.instance.usuario_modificou = self.request.user.id
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
    def form_valid(self, form):
        form.instance.usuario_modificou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)


class EstadoView(generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Estado
    template_name = "bases/estados_list.html"
    context_object_name = "obj"
    #login_url = "bases:login"    


class EstadoNew(SuccessMessageMixin, generic.CreateView):
    model = Estado
    template_name = 'bases/estado_form.html'
    context_object_name = "obj"
    form_class = EstadoForm
    success_url = reverse_lazy("bases:estado_list")
    #login_url = "bases:login"
    success_message = "Estado criado com sucesso!"


    def form_valid(self, form):
        form.instance.usuario_criou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)

  
class EstadoEdit(SuccessMessageMixin, generic.UpdateView):
    model = Estado
    template_name = 'bases/estado_form.html'
    context_object_name = 'obj'
    form_class = EstadoForm
    success_url = reverse_lazy("bases:estado_list")
    #login_url='bases:login'
    success_message = "Estado atualizado com sucesso!"

    def form_valid(self, form):
        form.instance.usuario_modificou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)

    
class CidadeView(generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Cidade
    template_name = "bases/cidades_list.html"
    context_object_name = "obj"
    #login_url = "bases:login"    


class CidadeNew(SuccessMessageMixin, generic.CreateView):
    model = Cidade
    template_name = 'bases/cidade_form.html'
    context_object_name = "obj"
    form_class = CidadeForm
    success_url = reverse_lazy("bases:cidade_list")
    #login_url = "bases:login"
    success_message = "Cidade criado com sucesso!"


    def form_valid(self, form):
        form.instance.usuario_criou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)

  
class CidadeEdit(SuccessMessageMixin, generic.UpdateView):
    model = Cidade
    template_name = 'bases/cidade_form.html'
    context_object_name = 'obj'
    form_class = CidadeForm
    success_url = reverse_lazy("bases:cidade_list")
    #login_url='bases:login'
    success_message = "Cidade atualizado com sucesso!"

    def form_valid(self, form):
        form.instance.usuario_modificou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)
