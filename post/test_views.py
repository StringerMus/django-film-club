from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from film.models import Movie
from .forms import FilmForm


class TestPostViews(TestCase):

    #create a user
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="adminUser",
            password="adminPass",
            email="admin@film.com"
        )

    #test post film renders with film and film catalogue
    def test_render_post_film_page_with_film_form(self):
        response = self.client.get(reverse(
            'post_film', args=['post_film']))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context['film_form'], ReviewForm)