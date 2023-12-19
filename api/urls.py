from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import UrlViewSet

router = DefaultRouter()
router.register('urls', UrlViewSet, basename='urls')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
