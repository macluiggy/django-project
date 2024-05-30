# core/permissions.py

from rest_framework.permissions import BasePermission

class HasPermissionToComment(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        return True
        
    # search the table user_roles for the user_id