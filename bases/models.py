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
    ddi = models.CharField(max_length=4)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return '{}'.format(self.pais)

    def save(self):
        self.pais = self.pais.upper()
        self.sigla = self.sigla.upper()
        super(Pais, self).save()

    class Meta:
        verbose_name_plural = 'Paises'        


class Estado(ClasseModelo):
    estado = models.CharField(max_length=100, unique=True)
    uf = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return '{}' .format(self.estado)
    
    def save(self):
        self.estado = self.estado.upper()
        self.uf = self.uf.upper()
        super(Estado, self).save()
    
    class Meta:
        verbose_name_plural = 'Estados'


class Cidade(ClasseModelo):
    cidade = models.CharField(max_length=100, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    ddd = models.CharField(max_length=3)
    sigla = models.CharField(max_length=5)
    codigo_municipio = models.IntegerField("Código Municipio (IBGE)", default=0, help_text="Necessário para emitir NFS-e.")

    def __str__(self):
        return '{}' .format(self.cidade)
    
    def save(self):
        self.cidade = self.cidade.upper()
        self.sigla = self.sigla.upper()
        super(Cidade, self).save()
    
    class Meta:
        verbose_name_plural = 'Cidades'


class OrgaoPublico(ClasseModelo):
    orgao_publico = models.CharField(max_length=100, unique=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{}' .format(self.orgao_publico + ' DE ' + self.cidade.__str__())
    
    def save(self):
        self.orgao_publico = self.orgao_publico.upper()
        super(OrgaoPublico, self).save()
    
    class Meta:
        verbose_name_plural = 'Órgãos Públicos'
    

class Imovel(ClasseModelo):
    imovel = models.CharField(max_length=100, unique=True)
    orgao_publico = models.ForeignKey(OrgaoPublico, on_delete=models.PROTECT)
    cep = models.CharField(max_length=10)
    numero = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    

    def __str__(self):
        return '{}' .format(self.imovel + ' DE ' + self.orgao_publico.__str__())
    
    def save(self):
        self.imovel = self.imovel.upper()
        self.rua = self.rua.upper()
        self.bairro = self.bairro.upper()
        self.complemento = self.complemento.upper()
        super(Imovel, self).save()
    
    class Meta:
        verbose_name_plural = 'Imóveis'


class TipoObra(ClasseModelo):
    tipo_obra = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}' .format(self.tipo_obra)
    
    def save(self):
        self.tipo_obra = self.tipo_obra.upper()
        super(TipoObra, self).save()
    
    class Meta:
        verbose_name_plural = 'Tipos de Obra'


class Obra(ClasseModelo):

    FUTURA = 'Fut'
    EXECUCAO = 'Exe'
    FINALIZADA = 'Fin'
    PARALIZADA = 'Par'
    
    STATUS_OBRA_CHOICES = [
        (FUTURA, 'Obra Futura'),
        (EXECUCAO, 'Em execução'),
        (FINALIZADA, 'Finalizada'),
        (PARALIZADA, 'Paralizada'),
    ]

    obra = models.CharField(max_length=100, unique=True)
    imovel = models.ForeignKey(Imovel, on_delete=models.PROTECT)
    tipo_obra = models.ForeignKey(TipoObra, on_delete=models.PROTECT)
    status_obra = models.CharField(max_length=10, choices=STATUS_OBRA_CHOICES)

    def __str__(self):
        return '{}' .format(self.obra + ' DE ' + self.imovel.__str__())
    
    def save(self):
        self.obra = self.obra.upper()
        super(Obra, self).save()
    
    class Meta:
        verbose_name_plural = 'Obras'


class ObraAnexo(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.SET_NULL, null=True, blank=True)
    arquivo = models.FileField(upload_to='arquivos_de_projeto', null=True, blank=True)
    

class Projeto(ClasseModelo):
    projeto = models.CharField(max_length=100, unique=True)
    obra = models.ForeignKey(Obra, on_delete=models.PROTECT)

    def __str__(self):
        return '{}' .format(self.obra + ' DE ' + self.projeto.__str__())
    
    def save(self):
        self.projeto = self.projeto.upper()
        super(Projeto, self).save()
    
    class Meta:
        verbose_name_plural = 'Obras'
    
    
class Arquivo(ClasseModelo):
    titulo = models.CharField(max_length=100)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='arquivos_de_projeto/')

    def __str__(self):
        return '{}' .format(self.titulo + ' DE ' + self.projeto.__str__())
    
    def save(self):
        self.titulo = self.titulo.upper()
        super(Arquivo, self).save()
    
    class Meta:
        verbose_name_plural = 'Arquivos'