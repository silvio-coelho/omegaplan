from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

from django.views import generic
from django.urls import reverse_lazy

from . models import *
from . forms import *

class Home(generic.TemplateView):
    template_name = 'parciais/dashboard.html'


class PaisView(generic.ListView):
    #permission_required = "inv.view_categoria"
    model = Pais
    template_name = "bases/paises_list.html"
    context_object_name = "obj"
    #login_url = "bases:login"    


class PaisNew(SuccessMessageMixin, generic.CreateView):
    model =Pais
    template_name='bases/pais_form.html'
    context_object_name="obj"
    form_class=PaisForm
    success_url=reverse_lazy("bases:pais_list")
    #login_url="bases:login"
    success_message="País criado com sucesso!"


    """     def dispatch(self, request, *args, **kwargs):
            #self.obj = self.get_object()
            return super().dispatch(request, *args, **kwargs)

        def form_invalid(self, form):
            response = super().form_invalid(form)
            if self.request.accepts('text/html'):
                return response
            else:
                return JsonResponse(form.errors, status=400)
    """
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = self.get_form()
            form.instance.usuario_criou = self.request.user
            data = form.save()
            data = {'mensagem': 'gravou'}
        except Exception as e:
            data['error'] = str(e)
            #messages.add_message(request, messages.INFO, data['error'])
            #print('aaaaaaaaaaaaaa', data['error'])
            messages.success(request, 'erro')
        #return JsonResponse(data)  
        #return HttpResponse(data['error'])
        #return HttpResponseRedirect(reverse_lazy('bases:pais_list'))
        return redirect(self.success_url)


    

class PaisEdit(SuccessMessageMixin, generic.UpdateView):
    model=Pais
    template_name='bases/pais_form.html'
    context_object_name='obj'
    form_class=PaisForm
    success_url=reverse_lazy("bases:pais_list")
    #login_url='bases:login'
    success_message="País atualizado com sucesso!"

    def form_valid(self, form):
        form.instance.usuario_modificou = self.request.user.id #aqui não está relacionado por isso o id
        return super().form_valid(form)        
