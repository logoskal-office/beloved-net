from typing import Any
from django.core.management.base import BaseCommand
from posts.models import *

class Command(BaseCommand):
    titles = ['The Heart', 
              'The Mind', 
              'The Soul', 
              'A Warrior', 
              'Stand Up', 
              'Faith', 
              'Do You Believe', 
              'Not Random',
              'The Truth',
              'The Eternal Life', 
              'The Water Of Life',
              'Eyes That See', 
              'Eyes That See pt. 2'
              'The Truth pt. 2',
              'Goodness',
              'Mercy',
              'Truth and Life']
    help = 'Generate A Set Of Test Values.'
    remember = 'Pain is inevitable but suffering is optional  - sunainagogoi93/YouTube'

    def handle(self, *args, **kwargs):
        for title in titles:
