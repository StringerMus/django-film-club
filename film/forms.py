from .models import Review
from django.core.exceptions import ValidationError
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content',)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Review.objects.filter(title=title).exists():
            raise ValidationError('A review with this title already exists.')
        return title