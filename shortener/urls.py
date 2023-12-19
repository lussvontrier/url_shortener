from django.urls import path, include

from shortener.views import index, redirect_to_long_url

urlpatterns = [
    path('', index, name='index'),
    path('go/<slug:short_url>/',
         redirect_to_long_url,
         name='redirect_to_long_url'),
]
