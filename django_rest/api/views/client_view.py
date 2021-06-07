from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import client_services
from ..serializers import client_serializer
from ..entidades import clients


class ClientList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        pagination = PageNumberPagination()
        clients = client_services.list_clients()

        result = pagination.paginate_queryset(clients, request)
        serializer = client_serializer.ClientSerializer(result, many=True)

        return pagination.get_paginated_response(serializer.data)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = client_serializer.ClientSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data["name"]
            email = serializer.validated_data["email"]
            cpf = serializer.validated_data["cpf"]

            new_client = clients.Client(name=name, email=email, cpf=cpf)
            client_services.register_client(new_client)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        client = client_services.list_client_id(id)
        serializer = client_serializer.ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
