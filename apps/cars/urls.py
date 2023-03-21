from django.urls import path

from apps.cars.views import CarsGetPost, CarGetUpdateDelete

urlpatterns = [
    path('', CarsGetPost.as_view(), name='cars_get_post'),
    path('/<int:pk>', CarGetUpdateDelete.as_view(), name="cars_get_update_delete")
]