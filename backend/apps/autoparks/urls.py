from django.urls import path

from apps.autoparks.views import AutoParkListCreateView, AutoParkCreateListCarsView


urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_parks_get_post'),
    path('/<int:pk>/cars', AutoParkCreateListCarsView.as_view(), name='auto_parks_get_post_cars'),
]
