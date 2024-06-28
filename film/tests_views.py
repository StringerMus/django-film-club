from django.contrib.auth.models import User
from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Movie, Review
from .forms import ReviewForm
from post.forms import FilmForm


class TestFilmViews(TestCase):

    #create a user
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="adminUser",
            password="adminPass",
            email="admin@film.com"
        )
        #film subject
        self.film = Movie(title=" Film title",
                        slug="film-title",
                        year="2024",
                        genre="action",
                        synopsis="Film about",
                        director="John Doe",
                        added_on ="2024-06-01T09:43:19.754Z"
                         )
        self.film.save()

    #film details - should be film review form details?
    def test_render_film_detail_page_with_review_form(self):
        response = self.client.get(reverse(
            'film_detail', args=['film-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Film title", response.content)
        self.assertIn(b"2024", response.content)
        self.assertIn(b"action", response.content)
        self.assertIn(b"Film about", response.content)
        self.assertIn(b"John Doe", response.content)
        self.assertIn(b"2024-06-01T09:43:19.754Z", response.content)
        self.assertIsInstance(
            response.context['review_form'], ReviewForm)