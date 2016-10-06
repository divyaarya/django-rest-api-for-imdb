from django.conf.urls import patterns, url

urlpatterns = patterns(
    'movies.views',
    url(r'movies_info/', 'movie_get', name='movie_get'),
    url(r'movies/$', 'movie_create', name='movie_create'),
    url(r'movies/(?P<pk>\d+)$', 'movie_edit', name='movie_edit'),
    # url(r'movies/', 'movie_edit', name='movie_edit'),
)
