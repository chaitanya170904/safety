from django.urls import path
from .views import ImageAnalyzerAPI

urlpatterns = [
    path('analyze/', ImageAnalyzerAPI.as_view(), name='analyze-image'),
]