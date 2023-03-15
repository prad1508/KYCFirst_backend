from django.db import models
from agent.models import Agent

status = [('Active', 'Active'),('Inactive', 'Inactive'),]
class Product(models.Model):
    product = models.CharField(max_length=60)
    logo_Image = models.ImageField()
    product_name = models.CharField(max_length=60)
    status = models.CharField(max_length=20,choices=status,default='Active')
    created_by = models.ForeignKey(Agent, on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(verbose_name='product added at', auto_now_add=True)