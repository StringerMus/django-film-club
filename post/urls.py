from . import views
from django.urls import path


urlpatterns = [
    path("", views.post_film, name='post_film'),
]