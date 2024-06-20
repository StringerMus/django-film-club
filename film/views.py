from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm


# Create your views here.
class FilmList(generic.ListView):
    queryset = Movie.objects.all()
    template_name = "film/index.html"
    paginate_by = 3


#post reviews and comments
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
            review = review_form.save(commit=False)
            review.author = request.user
            review.film = film
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
            comment.film = film
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
            "film": film,
            "review": reviews,
            "review_count": review_count,
            "review_form": review_form,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


#edit reviews
def review_edit(request, slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Movie.objects.all()
        film = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.film = film
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('film_detail', args=[slug]))


#edit comments
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        film = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.film = film
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('film_detail', args=[slug]))


#delete reviews
def review_delete(request, slug, review_id):
    """
    view to review comment
    """
    queryset = Movie.objects.all()
    film = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('film_detail', args=[slug]))


#delete comments
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Movie.objects.all()
    film = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('film_detail', args=[slug]))