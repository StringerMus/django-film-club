from django.shortcuts import render
from django.views import generic
from .models import Movie

# Create your views here.


class FilmList(generic.ListView):
    queryset = Movie.objects.all()
    template_name = "film/index.html"
    paginate_by = 6