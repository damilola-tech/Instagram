from django.shortcuts import render, HttpResponse

# Create your views here.
from photos.models import Photo


def index(request):
    photos = Photo.objects.all()

    context = {
        "photos": photos
    }
    return render(request, 'photos/index.html', context)
