# posts urls
from django.urls import path

from .views import HomePageView

# url pattern
urlpatterns = [
    path('', HomePageView.as_view(), name='posts')
]
