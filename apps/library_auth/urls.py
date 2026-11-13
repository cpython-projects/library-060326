from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView
from .views import (RegisterView,
                    LoginView,
                    RefreshView,
                    LogoutView,
                    LogoutAllView,
                    )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-all/', LogoutAllView.as_view(), name='logout_all'),
    path('token/refresh/', RefreshView.as_view(), name='token_refresh'),
    # path('password/change/', PasswordChangeView.as_view(), name='password_change'),
]