from rest_framework import viewsets
from file_manager.models import FileManager
from file_manager.serializer import FileManagerSerializer


class FileManagerViewSet(viewsets.ModelViewSet):
    queryset = FileManager.objects.all()
    serializer_class = FileManagerSerializer