# server configurations

import os

class Configs(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://luke@localhost:5432/citeExplore'
    DEBUG = True
    SECRET_KEY = 'TEMPTEMPTEMP'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
