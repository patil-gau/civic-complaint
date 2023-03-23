from django.db import models
from datetime import date, datetime


# Create your models here.
class Complaints(models.Model):
    comp_id = models.AutoField(primary_key=True)
    comp_title = models.CharField(max_length=80)
    comp_desc = models.TextField(null=False)
    comp_by = models.ForeignKey('users.Users',db_column='comp_by',on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city_id = models.ForeignKey('state_city.Cities', db_column='city_id',on_delete= models.CASCADE)
    state_id = models.ForeignKey('state_city.States', db_column='state_id',on_delete= models.CASCADE)
    country = models.CharField(max_length=20,default="India")
    status = models.CharField(max_length=20,default="not started")
    action_taken = models.CharField(max_length=90,default="none")
    progress = models.IntegerField(default=0)
    comp_date = models.DateField(auto_now=True,editable=False)
    comp_image = models.ImageField(upload_to="images",null=True,blank=True)
    comp_video = models.FileField(upload_to="videos",null=True,blank=True)
    
    class Meta: 
        db_table = 'complaints'  