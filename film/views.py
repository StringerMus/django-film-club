from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie, Review


# Create your views here.
class FilmList(generic.ListView):
    queryset = Movie.objects.all()
    template_name = "film/index.html"
    paginate_by = 3


def film_detail(request, slug):
    queryset = Movie.objects.all()
    film = get_object_or_404(queryset, slug=slug)
    reviews = film.reviews.all().order_by("-created_on")
    review_count = film.reviews.filter().count()

    return render(
        request,
        "film/film_detail.html",
        {
            "movie": film,
            "review": reviews,
            "review_count": review_count,
        },
    )