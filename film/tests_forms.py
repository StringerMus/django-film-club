from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        review_form = ReviewForm({
            'title': 'Snap',
            'content': 'Good film'
            })

        self.assertTrue(review_form.is_valid(), msg='Form is invalid')


    def test_form_is_invalid(self):
        review_form = ReviewForm({
            'title': '',
            'content': 'Good film'
            })

        self.assertFalse(review_form.is_valid(), msg='Form is valid')


    def test_form_is_invalid(self):
        review_form = ReviewForm({
            'title': 'Snap',
            'content': ''
            })

        self.assertFalse(review_form.is_valid(), msg='Form is valid')


    def test_form_is_invalid(self):
        review_form = ReviewForm({
            'title': '',
            'content': ''
            })

        self.assertFalse(review_form.is_valid(), msg='Form is valid')