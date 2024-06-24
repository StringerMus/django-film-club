from film.models import Movie
from django import forms


class FilmForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'genre', 'featured_image', 'synopsis', 'director',)
        prepopulated_fields = {'slug': ('title',)}