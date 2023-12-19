from django.db import models
from django.conf import settings


class Url(models.Model):
    long_url = models.URLField(
        max_length=settings.MAX_LENGTH_LONG_URL,
        help_text='Please input the full url which needs to be shortened.')
    short_url = models.SlugField(
        max_length=settings.MAX_LENGTH_SHORT_URL,
        unique=True
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
    count_clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.short_url} was clicked {self.count_clicks} times.'
