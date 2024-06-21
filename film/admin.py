from django.contrib import admin
from .models import Review, Comment, Movie
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class FilmAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'year', 'genre', 'director')
    search_fields = ['title', 'genre']
    list_filter = ('added_on', 'genre',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('synopsis',)


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('title', 'film', 'author', 'created_on', 'updated_on')
    search_fields = ['title', 'film', 'author']
    list_filter = ('film', 'created_on', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('review', 'author', 'created_on')
    search_fields = ['review', 'author']
    list_filter = ('review', 'created_on',)
    prepopulated_fields = {}
    summernote_fields = ('body',)
