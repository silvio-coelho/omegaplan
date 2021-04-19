from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import \
LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

from django.views import generic
from django.urls import reverse_lazy
from . models import Pais, Estado, Cidade
from . forms import PaisForm, EstadoForm, CidadeForm


class Home(generic.TemplateView):
    template_name = 'parciais/dashboard.html'


class PaisView(generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Pais
    template_name = "bases/paises_list.html"
    context_object_name = "obj"
    #login_url = "bases:login"    


class PaisNew(SuccessMessageMixin, generic.CreateView):
    model = Pais
    template_name = 'bases/pais_form.html'
    context_object_name = "obj"
    form_class = PaisForm
    success_url = reverse_lazy("bases:pais_list")
    #login_url = "bases:login"
    success_message = "País criado com sucesso!"


    def form_valid(self, form):
        form.instance.usuario_criou = self.request.user #aqui não está relacionado por isso o id
        return super().form_valid(form)

  
class PaisEdit(SuccessMessageMixin, generic.UpdateView):
    model = Pais
    template_name = 'bases/pais_form.html'
    context_object_name = 'obj'
    form_class = PaisForm
    success_url = reverse_lazy("bases:pais_list")
    #login_url='bases:login'
    success_message = "País atualizado com sucesso!"

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