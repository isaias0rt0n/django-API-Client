from django.urls import path
from .views import client_view, user_view

urlpatterns = [
    path('clients/', client_view.ClientList.as_view(), name="client-list"),
    path('clients/<int:id>', client_view.ClientDetails.as_view(), name="client-details"),

    path('user/', user_view.UserList.as_view(), name="user-list"),
]
