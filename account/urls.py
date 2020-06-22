from django.urls import path

from .views import (
    UserCreateView,
    LoginView
)

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('login/', LoginView.as_view())
]