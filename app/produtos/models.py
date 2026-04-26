from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Produto(models.Model):
    
    codigo = models.CharField(max_length=50, unique=True, blank=True, null=True) 
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    quantidade_minima = models.IntegerField(default=5)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, 
                                  null=True, related_name='produtos')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    @property
    def estoque_baixo(self):
        return self.quantidade <= self.quantidade_minima

    class Meta:
        ordering = ['nome']