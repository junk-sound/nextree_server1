from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    my_safe_method = []
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        if request.method in self.my_safe_method:
            return True
        return obj.user == request.user
