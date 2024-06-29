from film.models import Movie
from django import forms


class FilmForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'genre', 'featured_image', 'synopsis', 'director',)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Movie.objects.filter(title=title).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("A film with this title already exists.")
        return title