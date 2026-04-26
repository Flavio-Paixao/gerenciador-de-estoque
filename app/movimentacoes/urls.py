from rest_framework.routers import DefaultRouter
from .views import MovimentacaoViewSet

router = DefaultRouter()
router.register('movimentacoes', MovimentacaoViewSet)

urlpatterns = router.urls