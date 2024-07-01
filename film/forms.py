from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        self.film = kwargs.pop('film', None)
        super().__init__(*args, **kwargs)
