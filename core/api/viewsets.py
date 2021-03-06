from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """class PontoTuristicoViewSet(ModelViewSet):
        queryset = PontoTuristico.objects.all()
        serializer_class = PontoTuristicoSerializer"""

    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter, ]
    permission_classes = [DjangoModelPermissions, ]
    #permission_classes = [IsAuthenticatedOrReadOnly, ]
    #permission_classes = [IsAuthenticated, ]
    #permission_classes = [IsAdminUser, ]
    authentication_classes = (TokenAuthentication, )
    search_fields = ['nome', 'descricao', 'enderecos__linha1']

    def get_queryset(self):
        # return PontoTuristico.objects.filter(aprovado=True)

        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
        return queryset

    def list(self, request, *args, **kwargs):
        # return Response({'Teste: 123'})
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # return Response({'Hello': request.data['nome']})
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # pass
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass




