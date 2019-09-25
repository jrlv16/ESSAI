from django.contrib import admin, auth
from django.urls import path, include
from django.conf.urls import url

from . import views
from . views import *

urlpatterns = [
    path('pdf/<int:Letter_id>', views.letter_PDF),
]
