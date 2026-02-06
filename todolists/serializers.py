from rest_framework import serializers
from .models import Todolist
from notes.models import Note


class TodolistWriteSerializer(serializers.ModelSerializer):
    note = serializers.PrimaryKeyRelatedField(
        queryset=Note.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Todolist
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }


class TodolistReadSerializer(serializers.ModelSerializer):
    note = serializers.SerializerMethodField()

    class Meta:
        model = Todolist
        fields = '__all__'

    def get_note(self, obj):
        if not obj.note:
            return None
        return {
            "id": obj.note.id,
            "content": obj.note.content,
            "created_at": obj.note.created_at
        }

