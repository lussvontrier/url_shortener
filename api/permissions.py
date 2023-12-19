from rest_framework import permissions


class HasCodePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # The or not permission_code can be omitted if you dont plan on
        # sending requests from Djangos api web form but only pure api requests
        if request.method in ('PATCH', 'PUT'):
            permission_code = request.data.get('permission_code')
            return permission_code == 'SECRET_CODE' or not permission_code

        return True
