from django.shortcuts import render

# Create your views here.

from django.views import generic

class Home(generic.TemplateView):
    template_name = 'base.html'