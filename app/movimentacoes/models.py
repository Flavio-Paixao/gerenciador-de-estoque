from django.db import models
from produtos.models import Produto

class Movimentacao(models.Model):
    TIPOS = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, 
                                related_name='movimentacoes')
    tipo = models.CharField(max_length=10, choices=TIPOS)
    quantidade = models.IntegerField()
    observacao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.produto.nome} - {self.quantidade}"

    def save(self, *args, **kwargs):
        if self.tipo == 'entrada':
            self.produto.quantidade += self.quantidade
        elif self.tipo == 'saida':
            self.produto.quantidade -= self.quantidade
        self.produto.save()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-criado_em']