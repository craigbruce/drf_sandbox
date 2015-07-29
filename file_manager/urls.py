from django.conf.urls import url, include
from file_manager import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'file_manager', views.FileManagerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
