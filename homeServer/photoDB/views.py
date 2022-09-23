from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms


# Create your views here.

def index(request):
    list_images = models.photo.objects.all
    list_images2 = models.photo.objects.all
    context = {'image_list1':list_images,'image_list2':list_images2}
    return render(request, 'photoDB/index.html',context)

def upload(request):
    if request.method == 'POST':
        form = forms.PhotoUpload(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = forms.PhotoUpload
    return render(request,'photoDB/upload.html',{'form':form})