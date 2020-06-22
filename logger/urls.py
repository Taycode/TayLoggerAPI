from django.urls import path

from .views import CreateLogGroup

urlpatterns = [
    path("group/create", CreateLogGroup.as_view())
]
