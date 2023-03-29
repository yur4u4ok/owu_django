from django.urls import path

from .views import CarsGetPost, CarRetrieveUpdateDelete

urlpatterns = [
    path('', CarsGetPost.as_view(), name='cars_get_post'),
    path('/<int>', CarRetrieveUpdateDelete.as_view(), name='cars_get_update_delete')
]
