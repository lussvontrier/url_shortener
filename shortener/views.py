from django.shortcuts import render

from shortener.forms import UrlForm


def index(request):
    form = UrlForm(request.POST or None)
    if form.is_valid():
        url = form.save(commit=False)
        url.short_url = '123'
        url.save()
    return render(request, 'shortener/index.html')
