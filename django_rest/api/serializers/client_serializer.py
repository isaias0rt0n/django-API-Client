from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import *


class ClientSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'cpf', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('client-details', kwargs={'id': obj.pk}, request=request)
        }
