from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
