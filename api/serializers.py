from rest_framework import serializers

from shortener.models import Url
from shortener.generate_short_code import generate_short_code


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'


class CreateUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('long_url',)

    def create(self, validated_data):
        long_url = validated_data.get('long_url')
        return Url.objects.create(
            long_url=long_url,
            short_url=generate_short_code()
        )

    def to_representation(self, instance):
        return UrlSerializer(instance).data


class UpdateUrlSerializer(serializers.ModelSerializer):
    permission_code = serializers.CharField()

    class Meta:
        model = Url
        fields = ('long_url', 'short_url', 'permission_code')

    def to_representation(self, instance):
        return UrlSerializer(instance).data
