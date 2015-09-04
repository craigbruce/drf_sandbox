import django
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from file_manager.models import FileManager


django.setup()


def savefile():
    # Create a local file
    f = NamedTemporaryFile()
    f.write('I am contents')
    new_file = FileManager.objects.create(name='test file')
    # Save local file to FileField in our model
    new_file.file.save('new file name', File(f))
    f.close()

if __name__ == "__main__":
    savefile()
