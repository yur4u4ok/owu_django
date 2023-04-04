
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('auth', include('apps.auth.urls')),
    path('autoparks', include('apps.autoparks.urls')),
    path('users', include('apps.users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
