from django.urls import path

from .views import CreateLogGroup, CreateLog

urlpatterns = [
    path("group/create/", CreateLogGroup.as_view()),
    path("log/create/", CreateLog.as_view())
]
