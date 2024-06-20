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
    comment_count = comments.filter().count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted.'
            )
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment has been submitted, pending approval.'
            )

    review_form = ReviewForm()
    comment_form = CommentForm()

    return render(
        request,
        "film/film_detail.html",
        {
            "movie": film,
            "review": reviews,
            "review_count": review_count,
            "review_form": review_form,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )