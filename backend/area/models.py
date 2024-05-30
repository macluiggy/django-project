from django.db import models

from country.models import Country

# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'area'
        unique_together = ('name', 'country')

    def __str__(self):
        return self.name