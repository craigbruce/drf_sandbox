from rest_framework import serializers
from file_manager.models import FileManager


class FileManagerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FileManager
        fields = ('id', 'url', 'name', 'file')
