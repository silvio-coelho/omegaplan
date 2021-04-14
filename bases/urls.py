from django.urls import path
from bases.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('paises/', PaisView.as_view(), name='pais_list'),
    path('paises/new', PaisNew.as_view(), name='pais_new'),
    path('paises/edit/<int:pk>', PaisEdit.as_view(), name='pais_edit'),
]
