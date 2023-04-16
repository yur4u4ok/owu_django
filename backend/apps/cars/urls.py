from django.urls import path

from .views import CarRetrieveUpdateDelete, CarsListView

urlpatterns = [
    path('', CarsListView.as_view(), name='cars_get_post'),
    path('/<int:pk>', CarRetrieveUpdateDelete.as_view(), name='cars_get_update_delete')
]
