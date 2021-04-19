from django.urls import path
from bases.views import PaisNew, Home, PaisView, PaisEdit, EstadoNew, EstadoView, EstadoEdit, CidadeNew, CidadeView, CidadeEdit


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('paises/', PaisView.as_view(), name='pais_list'),
    path('paises/new', PaisNew.as_view(), name='pais_new'),
    path('paises/edit/<int:pk>', PaisEdit.as_view(), name='pais_edit'),

    path('estados/', EstadoView.as_view(), name='estado_list'),
    path('estados/new', EstadoNew.as_view(), name='estado_new'),
    path('estados/edit/<int:pk>', EstadoEdit.as_view(), name='estado_edit'),

    path('cidades/', CidadeView.as_view(), name='cidade_list'),
    path('cidades/new', CidadeNew.as_view(), name='cidade_new'),
    path('cidades/edit/<int:pk>', CidadeEdit.as_view(), name='cidade_edit'),
]
