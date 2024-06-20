from . import views
from django.urls import path


urlpatterns = [
    path("", views.FilmList.as_view(), name='home'),
    path('<slug:slug>/', views.film_detail, name='film_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
]