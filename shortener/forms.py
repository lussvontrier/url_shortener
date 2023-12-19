from django.forms import ModelForm

from shortener.models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ('long_url',)
