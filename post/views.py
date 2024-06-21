from django.shortcuts import render
from django.contrib import messages
from film.models import Movie
from .forms import FilmForm


# Create your views here.


def post_film(request):
    """
    Renders the Posts page
    """
    if request.method == "POST":
        film_form = FilmForm(data=request.POST)
        if film_form.is_valid():
            film_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'The film has been added to the film catalogue.'
            )

    movie = Movie.objects.all().order_by('-updated_on').first()
    film_form = FilmForm()

    return render(
        request,
        "post/post_film.html",
        {
            "post": post,
            "film_form": film_form,
        },
    )