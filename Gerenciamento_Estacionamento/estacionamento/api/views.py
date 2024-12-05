from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from estacionamento.api.serializers import ClienteSerializer, VeiculoSerializer, EstacionamentoSerializer
from estacionamento.models import Cliente, Veiculo, Estacionamento


class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


class VeiculoViewSet(ModelViewSet):
    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()


class EstacionamentoViewSet(ModelViewSet):
    serializer_class = EstacionamentoSerializer
    queryset = Estacionamento.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        data = response.data
        
        return Response(data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
      
        response = super().update(request, *args, **kwargs)
        
        return response
