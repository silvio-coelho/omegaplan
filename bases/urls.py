from django.urls import path
from django.contrib.auth import views as auth_views
from bases.views import PaisNew, Home, PaisView, PaisEdit


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('paises/', PaisView.as_view(), name='pais_list'),
    path('paises/new', PaisNew.as_view(), name='pais_new'),
    path('paises/edit/<int:pk>', PaisEdit.as_view(), name='pais_edit'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/login.html'), name='logout'),    
]
