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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Lista de Países"
        context['entity'] = "País"
        context['breadcrumb'] = "Países"
        context['list_url'] = reverse_lazy("bases:pais_list")
        return context
    


class PaisNew(SuccessMessageMixin, generic.CreateView):
    model = Pais
    template_name = 'bases/pais_form.html'
    context_object_name = "obj"
    form_class = PaisForm
    success_url = reverse_lazy("bases:pais_list")
    #login_url = "bases:login"
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
    template_name = 'bases/pais_form.html'
    context_object_name = 'obj'
    form_class = PaisForm
    success_url = reverse_lazy("bases:pais_list")
    #login_url='bases:login'
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
