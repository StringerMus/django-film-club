from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from film.models import Movie
from .forms import FilmForm


# Create your views here.
class FilmList(generic.ListView):
    queryset = Movie.objects.all()
    template_name = "post/post_film.html"
    #paginate_by = 3


def post_film(request):
    queryset = Movie.objects.all()

    if request.method == "POST":
        film_form = FilmForm(data=request.POST)
        if film_form.is_valid():
            film_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'The film has been added to the film catalogue.'
            )

    film = Movie.objects.all().order_by('-added_on').first()
    film_form = FilmForm()

    return render(
        request,
        "post/post_film.html",
        {
            "post": post_film,
            "film_form": film_form,
        },
    )