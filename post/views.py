from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from film.models import Movie
from .forms import MovieForm

# Create your views here.
def post_film(request):
    """
    Renders the Admin page
    """
    if request.method == "POST":
        admin_form = AdminForm(data=request.POST)
        if admin_form.is_valid():
            admin_form.save()
            messages.add_message(
            request, messages.SUCCESS,
            'The film has been added to the film catalogue.'
            )

    movie = Movie.objects.all().order_by('-updated_on').first()
    admin_form = AdminForm()

    return render(
        request,
        "film/post_film.html",
        {
            "admin": admin,
            "admin_form": admin_form,
        },
    )