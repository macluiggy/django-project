from django.db import models
from country.models import Country
from area.models import Area
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'roles'
        unique_together = ('name', 'country')

    def __str__(self):
        return self.name
    
class UserRole(models.Model):
    
    class Meta:
        db_table = 'user_roles'
        unique_together = ('user', 'role', 'area')
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)