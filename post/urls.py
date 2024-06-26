from . import views
from django.urls import path
from .views import post_film, FilmList


urlpatterns = [
    path("", views.post_film, name='post_film'),
    #path('<slug:slug>/', views.post_film, name='post'),
    path("", post_film, name='post_film'),
    path('films/', views.FilmList.as_view(), name='film-list'),
    path('delete_movie/<int:movie_id>', views.film_delete, name='film_delete'),
    path('edit_review/<int:review_id>', views.review_edit, name='film_edit'),
]