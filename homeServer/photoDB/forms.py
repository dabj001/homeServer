from django import forms
from . import models

class PhotoUpload(forms.ModelForm):

    class Meta:
        model = models.photo
        fields = ['url']
