from django.apps import apps
from django.contrib import admin

movie_app = apps.get_app_config('movies')
for model in movie_app.get_models():
    admin.site.register(model)
