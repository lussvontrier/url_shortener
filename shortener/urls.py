from django.urls import path, include

from shortener.views import index

urlpatterns = [
    path('', index, name='index'),
]
