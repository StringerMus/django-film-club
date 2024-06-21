from .models import Movie, Review, Comment
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('review', 'body',)

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'genre', 'featured_image', 'synopsis', 'director',)