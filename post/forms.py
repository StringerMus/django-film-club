from film.models import Movie
from django import forms

class FilmForm(forms.ModelForm):
    year = forms.IntegerField(
        min_value=1000,
        max_value=9999,
        error_messages={
            'min_value': 'Year must be a four-digit number.',
            'max_value': 'Year must be a four-digit number.'
        }
    )

    class Meta:
        model = Movie
        fields = (
            'title',
            'year',
            'genre',
            'featured_image',
            'synopsis',
            'director',)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)