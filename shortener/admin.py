from django.contrib import admin

from shortener.models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'long_url', 'pub_date', 'count_clicks')
    list_filter = ('pub_date',)
    search_fields = ('short_url', 'long_url')
    empty_value_display = 'Empty'
    readonly_fields = ('count_clicks',)
