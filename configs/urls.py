
from django.urls import path, include

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('auth', include('apps.auth.urls')),
    path('autoparks', include('apps.autoparks.urls')),
]
