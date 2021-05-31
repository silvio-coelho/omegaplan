from django.urls import path
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from bases.views import Home, PaisNew, PaisView, PaisEdit, PaisDelete, \
    EstadoNew, EstadoView, EstadoEdit, EstadoDelete, CidadeNew, CidadeView, \
    CidadeEdit, CidadeDelete, OrgaoPublicoNew, OrgaoPublicoView, OrgaoPublicoEdit, \
    OrgaoPublicoDelete, ImovelNew, ImovelView, ImovelEdit, ImovelDelete, TipoObraNew, \
    TipoObraView, TipoObraEdit, TipoObraDelete, ProjetoNew, ProjetoView, ProjetoEdit, \
    ProjetoDelete, ObraNew, ObraView, ObraEdit, ObraDelete, UploadView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/login.html'), name='logout'),    

    path('paises/', PaisView.as_view(), name='pais_list'),
    path('paises/new', PaisNew.as_view(), name='pais_new'),
    path('paises/edit/<int:pk>', PaisEdit.as_view(), name='pais_edit'),
    path('paises/delete/<int:pk>', PaisDelete.as_view(), name='pais_delete'),

    path('estados/', EstadoView.as_view(), name='estado_list'),
    path('estados/new', EstadoNew.as_view(), name='estado_new'),
    path('estados/edit/<int:pk>', EstadoEdit.as_view(), name='estado_edit'),
    path('estados/delete/<int:pk>', EstadoDelete.as_view(), name='estado_delete'),

    path('cidades/', CidadeView.as_view(), name='cidade_list'),
    path('cidades/new', CidadeNew.as_view(), name='cidade_new'),
    path('cidades/edit/<int:pk>', CidadeEdit.as_view(), name='cidade_edit'),
    path('cidades/delete/<int:pk>', CidadeDelete.as_view(), name='cidade_delete'),

    path('orgaospublicos/', OrgaoPublicoView.as_view(), name='orgaopublico_list'),
    path('orgaospublicos/new', OrgaoPublicoNew.as_view(), name='orgaopublico_new'),
    path('orgaospublicos/edit/<int:pk>', OrgaoPublicoEdit.as_view(), name='orgaopublico_edit'),
    path('orgaospublicos/delete/<int:pk>', OrgaoPublicoDelete.as_view(), name='orgaopublico_delete'),

    path('imovel/', ImovelView.as_view(), name='imovel_list'),
    path('imovel/new', ImovelNew.as_view(), name='imovel_new'),
    path('imovel/edit/<int:pk>', ImovelEdit.as_view(), name='imovel_edit'),
    path('imovel/delete/<int:pk>', ImovelDelete.as_view(), name='imovel_delete'),

    path('tipoobra/', TipoObraView.as_view(), name='tiposobra_list'),
    path('tipoobra/new', TipoObraNew.as_view(), name='tiposobra_new'),
    path('tipoobra/edit/<int:pk>', TipoObraEdit.as_view(), name='tiposobra_edit'),
    path('tipoobra/delete/<int:pk>', TipoObraDelete.as_view(), name='tiposobra_delete'),

    path('projeto/', ProjetoView.as_view(), name='projeto_list'),
    path('projeto/new', ProjetoNew.as_view(), name='projeto_new'),
    path('projeto/edit/<int:pk>', ProjetoEdit.as_view(), name='projeto_edit'),
    path('projeto/delete/<int:pk>', ProjetoDelete.as_view(), name='projeto_delete'),

    path('obra/', ObraView.as_view(), name='obra_list'),
    path('obra/new', ObraNew.as_view(), name='obra_new'),
    path('obra/edit/<int:pk>', ObraEdit.as_view(), name='obra_edit'),
    path('obra/delete/<int:pk>', ObraDelete.as_view(), name='obra_delete'),

    path('arquivo/upload', UploadView, name ='upload_view')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)