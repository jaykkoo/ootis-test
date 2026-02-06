from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Todolist
from .serializers import TodolistWriteSerializer, TodolistReadSerializer


class TodolistView(ModelViewSet):
    def get_queryset(self):
        return Todolist.objects.filter(user=self.request.user).select_related('note')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TodolistReadSerializer
        return TodolistWriteSerializer