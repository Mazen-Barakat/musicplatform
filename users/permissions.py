from rest_framework import permissions

class IsTheAllowedUser(permissions.BasePermission):
    def object_permission(self, request, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id