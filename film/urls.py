from . import views
from django.urls import path


urlpatterns = [
    path('', views.FilmList.as_view(), name='home'),
]