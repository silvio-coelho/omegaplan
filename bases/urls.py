from django.urls import path

from bases.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
