from django.db import models

# Create your models here.
class States(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=30,unique=True)
    
    class Meta:
        db_table = 'states'

class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30)
    state_id = models.ForeignKey('states',db_column='state_id', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'cities'