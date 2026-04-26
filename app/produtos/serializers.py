from rest_framework import serializers
from .models import Produto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'codigo', 'nome', 'descricao', 'preco', 'quantidade', 
          'quantidade_minima', 'categoria', 'categoria_nome', 
          'estoque_baixo', 'criado_em', 'atualizado_em']


class ProdutoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    estoque_baixo = serializers.BooleanField(read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'quantidade', 
                  'quantidade_minima', 'categoria', 'categoria_nome', 
                  'estoque_baixo', 'criado_em', 'atualizado_em']