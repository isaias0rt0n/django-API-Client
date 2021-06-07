from django.http import Http404

from ..models import Client


def list_clients():
    clients = Client.objects.all()
    return clients


def register_client(client):
    client_bd = Client.objects.create(name=client.name, email=client.email, cpf=client.cpf)
    client_bd.save()

    return client_bd


def list_client_id(id):
    try:
        return Client.objects.get(id=id)
    except Client.DoesNotExist:
        raise Http404
