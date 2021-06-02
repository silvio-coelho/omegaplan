from django.contrib import admin

from bases.models import Pais, Estado, Cidade, OrgaoPublico, Imovel, TipoObra, Projeto, Obra, ProjetoAnexo#, Arquivo
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


@admin.register(OrgaoPublico)
class OrgaoPublicoAdmin(admin.ModelAdmin):
    list_display = ("cidade", "orgao_publico")


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ("orgao_publico", "imovel", "rua")


admin.site.register(TipoObra)


@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ("imovel", "tipo_obra", "status_obra")


class ArquivosInline(admin.StackedInline):
    model = ProjetoAnexo
    extra = 1


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("projeto", "obra")
    inlines = [ArquivosInline,]


# @admin.register(Arquivo)
# class ArquivoAdmin(admin.ModelAdmin):
#     list_display = ("projeto", "titulo", "arquivo")