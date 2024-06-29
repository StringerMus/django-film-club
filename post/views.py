from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from film.models import Movie
from .forms import FilmForm


class FilmList(generic.ListView):
    model = Movie
    template_name = "post/post_film.html"
    context_object_name = "movie_list"


def post_film(request):
    queryset = Movie.objects.all()

    if request.method == "POST":
        film_form = FilmForm(request.POST, request.FILES)
        if film_form.is_valid():
            film_form.save()
            messages.add_message(request, messages.SUCCESS,
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

#edit films
def film_edit(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "POST":
        film_form = FilmForm(data=request.POST, files=request.FILES, instance=movie)
        
        if film_form.is_valid():
            film_form.save()
            messages.add_message(request, messages.SUCCESS, 'Film updated!')
            return HttpResponseRedirect(reverse('post_film'))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating film!')
    else:
        film_form = FilmForm(instance=movie)

    return render(
        request,
        "post/post_film.html",
        {
            "film_form": film_form,
            "movie_list": Movie.objects.all(),
        },
    )

#delete films
def film_delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Film deleted!')
    
    return HttpResponseRedirect(reverse('post_film'))