from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['nome', 'descricao', 'categoria__nome']
    filterset_fields = ['categoria']
    ordering_fields = ['nome', 'preco', 'quantidade']

    @action(detail=False, methods=['get'])
    def estoque_baixo(self, request):
        produtos = Produto.objects.filter(
            quantidade__lte=models.F('quantidade_minima')
        )
        serializer = self.get_serializer(produtos, many=True)
        return Response(serializer.data)