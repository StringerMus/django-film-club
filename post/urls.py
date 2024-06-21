from . import views
from django.urls import path


urlpatterns = [
    path("", views.post_film, name='post_film'),
    path('<slug:slug>/', views.post_film, name='post'),
]