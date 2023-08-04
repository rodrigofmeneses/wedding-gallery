from django.urls import path
from .views import RegisterUserView, PhotosViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix="photos", viewset=PhotosViewset)

urlpatterns = [
    path('register', RegisterUserView.as_view()),
    *router.urls
]
