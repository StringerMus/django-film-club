from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from film.models import Movie
from .forms import FilmForm


class FilmList(generic.ListView):
    model = Movie
    template_name = "post/post_film.html"
    #This makes sure the context name is movie_list
    context_object_name = "movie_list"


def post_film(request):
    queryset = Movie.objects.all()

    if request.method == "POST":
        film_form = FilmForm(request.POST, request.FILES)
        if film_form.is_valid():
            film_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'The film has been added to the film catalogue.'
            )

    film_form = FilmForm()
    movie_list = Movie.objects.all() #.order_by('-added_on').first()

    return render(
        request,
        "post/post_film.html",
        {
            "post": post_film,
            "film_form": film_form,
            "movie_list": movie_list,
        },
    )


#delete films
def film_delete(request, slug, movie_id):

    queryset = Movie.objects.all()
    film = get_object_or_404(queryset, slug=slug)
    movie = get_object_or_404(Movie, pk=movie_id)

    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Film deleted!')
    
    return HttpResponseRedirect(reverse('post_film', args=[slug]))