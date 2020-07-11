from django.urls import path

from .views import CreateLogGroup, CreateLog, GetLog

urlpatterns = [
    path("group/create/", CreateLogGroup.as_view()),
    path("log/create/", CreateLog.as_view()),
    path("log/<int:pk>/", GetLog.as_view())
]
