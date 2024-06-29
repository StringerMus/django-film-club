from . import views
from django.urls import path
from .views import post_film, FilmList


urlpatterns = [
    path("", views.post_film, name='post_film'),
    path("", post_film, name='post_film'),
    path('films/', views.FilmList.as_view(), name='film-list'),
    path('delete_movie/<int:movie_id>', views.film_delete, name='film_delete'),
    path('edit_film/<int:movie_id>', views.film_edit, name='film_edit'),
]