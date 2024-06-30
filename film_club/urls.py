from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path("post/", include("post.urls"), name="post-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("", include("film.urls"), name="film-urls"),
]
