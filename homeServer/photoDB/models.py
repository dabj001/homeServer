from django.db import models
from . import addedfunctions

# Create your models here.
class photo_old(models.Model):
    location = models.ImageField()
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date captured')

    def __str__(self):
        return self.name

class photo(models.Model):
    url = models.CharField(max_length=300)

    @property
    def exifs(self):
        return addedfunctions.get_exif(self.url)

    @property
    def date(self):
        return self.exifs['DateTime']