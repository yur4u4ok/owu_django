from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    ActivateUserView,
    AuthRegisterView,
    CheckUserAndGetEmailForRecovery,
    GetLoginUserView,
    RecoveryPassword,
)

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register'),
    path('/me', GetLoginUserView.as_view(), name='auth_me'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='activate_user'),
    path('/recovery', CheckUserAndGetEmailForRecovery.as_view(), name='get_email_for_password'),
    path('/recovery/<str:token>', RecoveryPassword.as_view(), name='recovery_password'),

]
