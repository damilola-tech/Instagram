from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index')
    # path('', include('photos.url'))
]