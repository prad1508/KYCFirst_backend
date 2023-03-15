from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    company_id  = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=90,unique=True)
    gst_no = models.CharField(max_length=50)
    emailID = models.EmailField()
    mobile_no = PhoneNumberField()
    Address = models.TextField()
    country = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    pincode = models.IntegerField()
    logo = models.ImageField(upload_to='company_logo')
    status = models.BooleanField(default=False)

    def __str__(self):
       return str(self.company_name)


class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name="company", null=True)
    branch_name = models.CharField(max_length=80)
    Address = models.TextField()
    emailID = models.EmailField()
    mobile_no = PhoneNumberField()

    def __str__(self):
       return f'{self.company}-{self.branch_name}'

