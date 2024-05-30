# core/permissions.py

from rest_framework.permissions import BasePermission
from permissions.models import RolePermission
from roles.models import UserRole
from roles.serializers import UserRolesSerializer
from permissions.models import RolePermission
from permissions.serializers import RolePermissionSerializer

POST_COMMENT = 'posts.comment'
class HasPermissionToComment(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        user_id = request.user.id
        # seatch the permission with the name POST_COMMENT
        user_roles = UserRole.objects.filter(user=user_id)
        
        
        
        # Check if any of the user's roles has the required permission
        for user_role in user_roles:
            role_permissions = RolePermission.objects.filter(role=user_role.role)
            role_permission_serializer = RolePermissionSerializer(role_permissions, many=True)
            print(role_permission_serializer.data)
            for role_permission in role_permissions:
                if role_permission.permission.name == POST_COMMENT and role_permission.allowed:
                    return True
        return False