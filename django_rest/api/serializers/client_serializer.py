from rest_framework import serializers
from ..models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'cpf')
