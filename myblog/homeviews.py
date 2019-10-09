from django.shortcuts import render
from gallery.models import Gallery

def index(request):
    gallerys = Gallery.objects.all()
    return render(request,'home.html',{'gaall':gallerys})
