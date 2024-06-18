from . import views
from django.urls import path


urlpatterns = [
    path("", views.FilmList.as_view(), name='home'),
    path('<slug:slug>/', views.film_detail, name='film_detail'),
]