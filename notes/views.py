from rest_framework.viewsets import ModelViewSet
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class NoteView(ModelViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
            return Note.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
