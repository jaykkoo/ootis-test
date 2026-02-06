from rest_framework import serializers
from .models import Note
from todolists.models import Todolist

class TodolistMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ['id', 'title', 'status', 'created_at']

class NoteSerializer(serializers.ModelSerializer):

    todolists = TodolistMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }