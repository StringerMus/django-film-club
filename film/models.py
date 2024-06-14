from django.db import models
from django.contrib.auth.models import User
import datetime

STATUS = ((0, "Draft"), (1, "Published"))

GENRE_CHOICES = (
    ('horror','HORROR'),
    ('drama', 'DRAMA'),
    ('action','ACTION'),
    ('comedy','COMEDY'),
    ('sci-fi','SCI-FI'),
    ('western','WESTERN'),
    ('thriller', 'THRILLER'),
    ('documentary','DOCUMENTARY'),
    ('fantasy','FANTASY'),
    ('romance','ROMANCE'),
)

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    year = models.IntegerField(('year'), default=datetime.datetime.now().year)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES, default='horror')
    synopsis = models.TextField()
    director = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_on"]

    def __str__(self):
        return f"{self.title} | {self.year}"


class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    film = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review_subject")
    slug = models.SlugField(max_length=200, unique=True)
    #rating = 
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_author"
        )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | by {self.author}"


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_author")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.body} | by {self.author}"