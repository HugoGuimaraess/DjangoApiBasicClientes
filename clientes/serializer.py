from rest_framework import serializers
from clientes.models import Cliente
from clientes.validator import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields = '__all__'


        def validate(self,data):
            if not valida_nome(data['nome']):
                raise serializers.ValidationError({'nome':'Não inclua números neste campo'})
            if not valida_rg(data['rg']):
                raise serializers.ValidationError({'rg':'O RG deve ter 9 dígitos'})
            if not valida_cpf(data['cpf']):
                raise serializers.ValidationError({'cpf': "Número de CPF inválido"})
            if not valida_celular(data['celular']):
                raise serializers.ValidationError({'celular': "O número de celular deve seguir este modelo: 11 91234-1234 (respeitando os espaços e traço)"})
            return data
