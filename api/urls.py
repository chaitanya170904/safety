from django.urls import path
from .views import check_tweet

urlpatterns = [
    path('check_tweet/', check_tweet, name='check_tweet'),
]