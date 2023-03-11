from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated
        elif request.method == 'PUT':
            return  request.user.is_authenticated
        elif request.method == 'DELETE':
            return  request.user.is_authenticated
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.method == 'GET':
            return True
        elif request.method == 'PUT':
            return obj == request.user and request.user.is_authenticated
        elif request.method == 'DELETE':
            return obj == request.user and request.user.is_authenticated
        else:
            return False