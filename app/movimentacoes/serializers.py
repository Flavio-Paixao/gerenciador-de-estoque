from rest_framework import serializers
from .models import Movimentacao

class MovimentacaoSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = Movimentacao
        fields = ['id', 'produto', 'produto_nome', 'tipo', 
                  'tipo_display', 'quantidade', 'observacao', 'criado_em']