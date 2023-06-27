from django.shortcuts import render
from rest_framework import viewsets,filters
from clientes.models import Cliente
from clientes.serializer import ClienteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    ordering_fields = ['nome']
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filterset_fields = ['ativo']
    search_fields = ['nome','cpf']



