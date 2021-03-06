# drf_sandbox

A sandbox to explore DRF features

## Installation

1. Create a virtualenv and run `pip install -r requirements.txt`
2. Setup your database with `python manage.py migrate`
3. Run a dev server with `python manage.py runserver`

## file_manager

A simple app to upload files via DRF which are stored in the media folder of this directory

No authentication is used

Use the DRF HTML form to test with [http://127.0.0.1:8000/file_manager/](http://127.0.0.1:8000/file_manager/)

Use httpie with `http -f POST http://127.0.0.1:8000/file_manager/ name='some file' file@~/Desktop/file.txt`

Obtain the path of the first uploaded file:

    >>> from file_manager.models import FileManager
    >>> files = FileManager.objects.all()
    >>> files[0].file.name
    u'uploads/my_file.txt'

Use a script to upload a file:

    $ export DJANGO_SETTINGS_MODULE=drf_sandbox.settings
    $ python save_a_file_to_a_model.py