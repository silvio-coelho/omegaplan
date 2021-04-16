from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import \
LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

from django.views import generic
from django.urls import reverse_lazy
from . models import Pais
from . forms import PaisForm


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

    """ def post(self, request, *args, **kwargs):
        print(request.POST)
        print(self.request.user.id) """


    def form_valid(self, form):
        print(self.request.user.id)
        form.instance.usuario_criou_id = self.request.user.id #aqui não está relacionado por isso o id
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



  
class PaisEdit(SuccessMessageMixin, generic.UpdateView):
    model = Pais
    template_name = 'bases/pais_form.html'
    context_object_name = 'obj'
    form_class = PaisForm
    success_url = reverse_lazy("bases:pais_list")
    #login_url='bases:login'
    success_message = "País atualizado com sucesso!"

    def form_valid(self, form):
        form.instance.usuario_modificou = self.request.user.id #aqui não está relacionado por isso o id
        return super().form_valid(form)
