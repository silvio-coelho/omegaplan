from django.contrib import admin

from bases.models import Pais, Estado, Cidade
# Register your models here.

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ("pais", "ddi", "sigla")


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ("pais", "estado", "uf")


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ("estado", "cidade", "codigo_municipio")