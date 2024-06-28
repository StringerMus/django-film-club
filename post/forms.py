from film.models import Movie
from django.core.exceptions import ValidationError
from django import forms


class FilmForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'genre', 'featured_image', 'synopsis', 'director',)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Movie.objects.filter(title=title).exists():
            raise ValidationError('A movie with this title already exists.')
        return title