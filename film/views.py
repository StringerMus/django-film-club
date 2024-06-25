from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Movie, Review
from .forms import ReviewForm
from post.forms import FilmForm


# Create your views here.
class FilmList(generic.ListView):
    queryset = Movie.objects.all()
    template_name = "film/index.html"
    paginate_by = 3


#post reviews
def film_detail(request, slug):
    queryset = Movie.objects.all()
    film = get_object_or_404(queryset, slug=slug)
    reviews = film.reviews.all().order_by("-created_on")
    review_count = film.reviews.filter().count()

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

    review_form = ReviewForm()

    return render(
        request,
        "film/film_detail.html",
        {
            "film": film,
            "review": reviews,
            "review_count": review_count,
            "review_form": review_form,
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


def add_movie(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_film.html')
    else:
        form = MovieForm()
    return render(request, 'post_film.html', {'form': form})