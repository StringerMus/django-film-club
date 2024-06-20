from . import views
from django.urls import path


urlpatterns = [
    path("", views.FilmList.as_view(), name='home'),
    path('<slug:slug>/', views.film_detail, name='film_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]