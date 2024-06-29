from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        self.film = kwargs.pop('film', None)
        super().__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if self.film and Review.objects.filter(film=self.film, title=title).exists():
            raise forms.ValidationError("A review with this title already exists.")
        return title