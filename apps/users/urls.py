from django.urls import path

from .views import AdminToUserView, GetAllUsersView, UserBlock, UserUnblock

urlpatterns = [
    path('', GetAllUsersView.as_view(), name='all_users_get'),
    path('/<int:pk>/admin_to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/block', UserBlock.as_view(), name='block_user'),
    path('/<int:pk>/unblock', UserUnblock.as_view(), name='unblock_user'),
]
