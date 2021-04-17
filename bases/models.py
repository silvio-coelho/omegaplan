from django.db import models

# Create your models here.
from django.contrib.auth.models import User
#from django_userforeignkey.models.fields import UserForeignKey


class ClasseModelo(models.Model):
    ativo = models.BooleanField(default=True)
    data_criou = models.DateTimeField(auto_now_add=True)
    data_editou = models.DateTimeField(auto_now=True)
    usuario_criou = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificou = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True #para o django não levar em consideração essa classe nas migrações


class Pais(ClasseModelo):
    pais = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}'.format(self.pais)

    """ def save(self):
        self.pais = self.pais.upper()
        super(Pais, self).save() """

    class Meta:
        verbose_name_plural = 'Paises'        


class Estado(ClasseModelo):
    estado = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}' .format(self.estado)
    
    def save(self):
        self.estado = self.estado.upper()
        super(Estado, self).save()
    
    class Meta:
        verbose_name_plural = 'Estados'


class Cidade(ClasseModelo):
    cidade = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}' .format(self.cidade)
    
    def save(self):
        self.cidade = self.cidade.upper()
        super(Cidade, self).save()
    
    class Meta:
        verbose_name_plural = 'Cidades'