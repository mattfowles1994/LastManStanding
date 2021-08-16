from django.urls import path

from pages.views import (
    home_view,
)

urlpatterns = [
    path('home/', home_view, name='home'),
]