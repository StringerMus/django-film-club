from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm


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

    comments_obj = Comment.objects.all()
    comments = comments_obj.all().order_by("-created_on")
    #review_count = film.reviews.filter().count()
    comment_form = CommentForm()
    review_form = ReviewForm()

    return render(
        request,
        "film/film_detail.html",
        {
            "movie": film,
            "review": reviews,
            "review_count": review_count,
            "review_form": review_form,
            "comments": comments,
            #"review_count": review_count,
            "comment_form": comment_form,
        },
    )