from django.shortcuts import render, HttpResponse

# Create your views here.
from .forms import PhotoForm
from photos.models import Photo


def index(request):
    if request.method == "POST":
        photo_model_form = PhotoForm(request.POST, request.FILES)
        print(photo_model_form.is_valid(), photo_model_form, request.POST)

        if photo_model_form.is_valid():
            photo_model_form.save()

    else:
        photo_model_form = PhotoForm()

    photos = Photo.objects.all().order_by("-created_at")
    context = {
        'photos': photos,
        'photo_model_form': photo_model_form
    }

    return render(request, 'photos/index.html', context)
