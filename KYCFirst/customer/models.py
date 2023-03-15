from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from agent.models import Agent
import uuid


gender = [('MALE', 'MALE'),('FEMALE', 'FEMALE'),('TRANSGENDER','TRANSGENDER')]
class Customer(models.Model):
    created_by = models.ForeignKey(Agent, on_delete=models.CASCADE,related_name="user")
    cus_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=70,default='')
    lname = models.CharField(max_length=70, default='')
    gender = models.CharField(max_length=20,choices=gender,default='MALE')
    mobile_no = PhoneNumberField()
    Is_Checked = models.BooleanField(default=False)
    Is_approved = models.BooleanField(default=False)
    aadhar_no = models.IntegerField(default='0')
    front_img  = models.ImageField(upload_to='adhar_front',blank=True)
    back_img  = models.ImageField(upload_to='adhar_back', blank=True)
    pan_no = models.CharField(max_length=70,blank=True)
    pan_img  = models.ImageField(upload_to='pan_img',blank=True)
    voter_id = models.CharField(max_length=70,blank=True)
    voter_img  = models.ImageField(upload_to='voter_img',blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True, unique=True, default = uuid.uuid4())

    def __str__(self):
        return f'{self.fname} {self.lname}'

