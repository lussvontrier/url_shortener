from rest_framework.viewsets import ModelViewSet

from shortener.models import Url
from api.serializers import (
    UrlSerializer, CreateUrlSerializer,
    UpdateUrlSerializer
    )
from api.permissions import HasCodePermission


class UrlViewSet(ModelViewSet):
    queryset = Url.objects.all()
    permission_classes = (HasCodePermission,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUrlSerializer
        if self.action in ('partial_update', 'update'):
            return UpdateUrlSerializer
        return UrlSerializer
