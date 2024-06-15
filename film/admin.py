from django.contrib import admin
from .models import Review, Comment, Movie
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class FilmAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'year', 'genre')
    search_fields = ['title', 'genre']
    list_filter = ()
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Review)
admin.site.register(Comment)

