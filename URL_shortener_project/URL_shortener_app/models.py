from django.db import models
from datetime import datetime

# Create your models here.

#by convention you should use a singluar name for your class because it creates one instance
class Short_Cut(models.Model):
    original_url = models.TextField(unique=True)
    shortcut = models.TextField(unique=True, primary_key=True)
    created_date = models.DateTimeField(default=datetime.now())

    # once you have set up a class you have to run a migrations with python \manage.py makemigrations doDoApp. Once this is successful you should have a 0001_initial in yoru omigrations folder. After any changes to models you must make another migration. this creates instructions for migrating. python manage.py migrate then actually migrates things to the app.

    def __str__(self):
        return self.shortcut
