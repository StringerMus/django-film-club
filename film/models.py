from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
import datetime
import uuid

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
    ('crime','CRIME'),
)


class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default=uuid.uuid4) #editable=False
    year = models.IntegerField(('year'), default=datetime.datetime.now().year)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES, default='horror')
    featured_image = CloudinaryField('image', default='placeholder')
    synopsis = models.TextField()
    director = models.CharField(max_length=200, unique=False)
    added_on = models.DateTimeField(auto_now_add=True)

    # Generate the slug based on title and id
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
            if self.id:
                self.slug += '-' + str(self.id)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-added_on"]

    def __str__(self):
        return f"{self.title} | {self.year}"


class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    film = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_author")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | by {self.author}"