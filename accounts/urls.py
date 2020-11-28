from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

from .views import check_role


urlpatterns = [
    path('token', TokenObtainPairView.as_view()),
    path('check-role', check_role)
]
