from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from shortener.forms import UrlForm
from shortener.models import Url
from shortener.generate_short_code import generate_short_code


def index(request):
    form = UrlForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        url = form.save(commit=False)
        url.short_url = generate_short_code()
        while url.exists_short_url():
            url.short_url = generate_short_code()
        url.save()

        context.update(
            {'short_url': f'{settings.BASE_URL}/go/{url.short_url}'}
        )
    return render(request, 'shortener/index.html', context)


def redirect_to_long_url(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    url.count_clicks += 1
    url.save()

    return redirect(url.long_url)
