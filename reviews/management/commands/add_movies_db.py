from django.core.management.base import BaseCommand
from reviews.models import reviews
import os
import json

class Command(BaseCommand):
    help= 'Load movies from movie_descriptions.json into the Reviews model'

    def handle(self,*args, **kwargs):
        json_file_path= "reviews/management/commands/movies.json"
        with open(json_file_path, 'r') as file:
            movies= json.load(file)

        for i in range(100):
            movie = movies[i]
            exist = reviews.objects.filter(title= movie['title'])
            if not exist:
                reviews.objects.create(
                    title=movie['title'],
                    image='reviews/images/default.jpg',
                    genre=movie['genre'],
                    year=movie['year'])
