from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .forms import FilmForm


class TestFilmForm(TestCase):

    def test_form_is_valid(self):
        """ Test all fields"""
        film_form = FilmForm({
            'title': 'James Bond',
            'year': '2020',
            'genre': 'action',
            'featured_image': SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            'synopsis': 'Bond must find Gold Finger',
            'director': 'David Gold',
        })
        self.assertTrue(film_form.is_valid(), msg="Form is not valid")


    def test_form_is_invalid(self):
        """ Test title field"""
        film_form = FilmForm({
            'title': '',
            'year': '2020',
            'genre': 'action',
            'featured_image': SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            'synopsis': 'Bond must find Gold Finger',
            'director': 'David Gold',
        })
        self.assertFalse(film_form.is_valid(), msg="Missing title - Form is valid")


    def test_form_is_invalid(self):
        """ Test year field - letters are invalid"""
        film_form = FilmForm({
            'title': 'James Bond',
            'year': 'abcd',
            'genre': 'action',
            'featured_image': SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            'synopsis': 'Bond must find Gold Finger',
            'director': 'David Gold',
        })
        self.assertFalse(film_form.is_valid(), msg="Letters in year field - Form is valid")


    def test_form_is_valid(self):
        """ Test year field - letters are invalid"""
        film_form = FilmForm({
            'title': 'James Bond',
            'year': '20204',
            'genre': 'action',
            'featured_image': SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            'synopsis': 'Bond must find Gold Finger',
            'director': 'David Gold',
        })
        self.assertTrue(film_form.is_valid(), msg="Letters in year field - Form is valid")


    def test_form_is_invalid(self):
        """ Test year field"""
        film_form = FilmForm({
            'title': 'James Bond',
            'year': '',
            'genre': 'action',
            'featured_image': SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            'synopsis': 'Bond must find Gold Finger',
            'director': 'David Gold',
        })
        self.assertFalse(film_form.is_valid(), msg="Missing year - Form is valid")


    def test_form_is_invalid(self):
        """ Test year field"""
        film_form = FilmForm({
            'title': 'James Bond',
            'year': '2020',
            'genre': '',
            'featured_image': SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            'synopsis': 'Bond must find Gold Finger',
            'director': 'David Gold',
        })
        self.assertFalse(film_form.is_valid(), msg="Missing genre - Form is valid")


    def test_form_is_valid(self):
        """ Test missing image field - missing image fields has placeholder images"""
        film_form = FilmForm({
            'title': 'James Bond',
            'year': '2020',
            'genre': 'action',
            'synopsis': 'Bond must find Gold Finger',
            'director': 'David Gold',
        })
        self.assertTrue(film_form.is_valid(), msg="Missing image - Form is invalid")


    def test_form_is_invalid(self):
        """ Test synopsis field"""
        film_form = FilmForm({
            'title': 'James Bond',
            'year': '2020',
            'genre': 'action',
            'featured_image': SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            'synopsis': '',
            'director': 'David Gold',
        })
        self.assertFalse(film_form.is_valid(), msg="Missing synopsis - Form is valid")


    def test_form_is_invalid(self):
        """ Test year field"""
        film_form = FilmForm({
            'title': 'James Bond',
            'year': '2020',
            'genre': 'action',
            'featured_image': SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            'synopsis': 'Bond must find Gold Finger',
            'director': '',
        })
        self.assertFalse(film_form.is_valid(), msg="Missing Genre - Form is valid")