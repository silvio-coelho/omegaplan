from django.db import models

# Create your models here.
from django.contrib.auth.models import User
#from django_userforeignkey.models.fields import UserForeignKey


class ClaseModelo(models.Model):
    ativo = models.BooleanField(default=True)
    data_criou = models.DateTimeField(auto_now_add=True)
    data_editou = models.DateTimeField(auto_now=True)
    usuario_criou = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificou = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract=True #para o django não levar em consideração essa classe nas migrações


class Pais(ClaseModelo):
    descricao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}'.format(self.descricao)

    def save(self):
        self.descricao = self.descricao.upper()
        super(Pais, self).save()

    class Meta:
        verbose_name_plural = 'Paises'        