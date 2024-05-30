from django.db import models
from roles.models import Role

# Create your models here.
class Permission(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    allowed = models.BooleanField(default=True)

    class Meta:
        unique_together = ('role', 'permission')