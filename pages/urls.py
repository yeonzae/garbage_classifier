from django.urls import path

from .views import HomePageView, AboutPageView
from .views import upload_image

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("upload/", upload_image, name="upload_image"),
]
