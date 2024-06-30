from django.test import TestCase
from .forms import ReviewForm


# Checks if forms valid if/not input correctly
class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        """ Test all fields"""
        review_form = ReviewForm({
            'title': 'Snap',
            'content': 'Good film'
            })

        self.assertTrue(review_form.is_valid(), msg='Form is invalid')

    def test_form_is_invalid(self):
        """ Test title field"""
        review_form = ReviewForm({
            'title': '',
            'content': 'Good film'
            })

        self.assertFalse(review_form.is_valid(), msg='Form is valid')

    def test_form_is_invalid(self):
        """ Test content field"""
        review_form = ReviewForm({
            'title': 'Snap',
            'content': ''
            })

        self.assertFalse(review_form.is_valid(), msg='Form is valid')

    def test_form_is_invalid(self):
        """ Test all null fields"""
        review_form = ReviewForm({
            'title': '',
            'content': ''
            })

        self.assertFalse(review_form.is_valid(), msg='Form is valid')
