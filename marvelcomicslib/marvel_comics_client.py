# -*- coding: utf-8 -*-

"""
    marvelcomicslib.marvel_comics_client

    This file was automatically generated by APIMATIC BETA v2.0 on 09/23/2016
"""

from .http import *
from .models import *
from .exceptions import *
from .decorators import *
from .controllers import *

class MarvelComicsClient(object):

    @lazy_property
    def stories(self):
        return StoriesController()

    @lazy_property
    def series(self):
        return SeriesController()

    @lazy_property
    def events(self):
        return EventsController()

    @lazy_property
    def creators(self):
        return CreatorsController()

    @lazy_property
    def comics(self):
        return ComicsController()

    @lazy_property
    def characters(self):
        return CharactersController()


    def __init__(self, 
                 referer = None,
                 apikey = None):

        Configuration.referer = referer
        Configuration.apikey = apikey


