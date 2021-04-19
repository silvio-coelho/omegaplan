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
        super(Cidade, self).save()
    
    class Meta:
        verbose_name_plural = 'Cidades'


class OrgaoPublico(ClasseModelo):
    orgao_publico = models.CharField(max_length=100, unique=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return '{}' .format(self.orgao_publico + 'de' + self.cidade.__str__())
    
    def save(self):
        self.orgao_publico = self.orgao_publico.upper()
        super(OrgaoPublico, self).save()
    
    class Meta:
        verbose_name_plural = 'Órgãos Públicos'
    

class Imovel(ClasseModelo):
    imovel = models.CharField(max_length=100, unique=True)
    orgao_publico = models.ForeignKey(OrgaoPublico, on_delete=models.PROTECT)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return '{}' .format(self.imovel + 'de' + self.orgao_publico.__str__())
    
    def save(self):
        self.imovel = self.imovel.upper()
        super(Imovel, self).save()
    
    class Meta:
        verbose_name_plural = 'Imóveis'


class TipoProjeto(ClasseModelo):
    tipo_projeto = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}' .format(self.tipo_projeto)
    
    def save(self):
        self.tipo_projeto = self.tipo_projeto.upper()
        super(TipoProjeto, self).save()
    
    class Meta:
        verbose_name_plural = 'Tipos de Projetos'


class Projeto(ClasseModelo):
    projeto = models.CharField(max_length=100, unique=True)
    imovel = models.ForeignKey(Imovel, on_delete=models.PROTECT)
    tipo_projeto = models.ForeignKey(TipoProjeto, on_delete=models.PROTECT)

    def __str__(self):
        return '{}' .format(self.projeto + 'de' + self.imovel.__str__())
    
    def save(self):
        self.projeto = self.projeto.upper()
        super(Projeto, self).save()
    
    class Meta:
        verbose_name_plural = 'Projetos'


class Obra(ClasseModelo):
    EXECUCAO = 'Exe'
    FINALIZADA = 'Fin'
    PARALIZADA = 'Par'

    obra = models.CharField(max_length=100, unique=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)

    STATUS_OBRA_CHOICES = [
        (EXECUCAO, 'Em execução'),
        (FINALIZADA, 'Finalizada'),
        (PARALIZADA, 'Paralizada'),
    ]
    status_obra = models.CharField(max_length=3, choices=STATUS_OBRA_CHOICES)

    def __str__(self):
        return '{}' .format(self.obra + 'de' + self.projeto.__str__())
    
    def save(self):
        self.obra = self.obra.upper()
        super(Obra, self).save()
    
    class Meta:
        verbose_name_plural = 'Obras'
    
    
class Arquivo(ClasseModelo):
    titulo = models.CharField(max_length=100, unique=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='arquivos')

    def __str__(self):
        return '{}' .format(self.titulo + 'de' + self.projeto.__str__())
    
    def save(self):
        self.titulo = self.titulo.upper()
        super(Arquivo, self).save()
    
    class Meta:
        verbose_name_plural = 'Arquivos'