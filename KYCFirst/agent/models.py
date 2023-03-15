from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from company.models import Company, Location


class AgentManager(BaseUserManager):

    def _create_user(self, email, username, password=None):

        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')
        
        user = self.model(email = self.normalize_email(email), username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password=None):
        user = self._create_user(
            email = self.normalize_email(email), 
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

gender = [('MALE', 'MALE'),('FEMALE', 'FEMALE'),('TRANSGENDER','TRANSGENDER')]
documents = [('AADHAR CARD', 'AADHAR CARD'),('DRIVING LICENSE', 'DRIVING LICENSE'),('VOTER ID','VOTER ID')]
class Agent(AbstractUser):
    
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    Checker = models.BooleanField(default=False)
    Maker = models.BooleanField(default=False)
    Approver = models.BooleanField(default=False)
    first_name = models.CharField(max_length=70, default='')
    last_name = models.CharField(max_length=70, default='')
    gender = models.CharField(max_length=20,choices=gender,default='MALE')
    mobile_no = PhoneNumberField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    biometric_details = models.ImageField(upload_to='biometric_details',null=True)
    photograph  = models.ImageField(upload_to='agent_photograph', blank=True)
    document_type = models.CharField(max_length=20,choices=documents,default='AADHAR CARD')
    document_no = models.CharField(max_length=50)
    document_image  = models.ImageField(upload_to='agent_document',blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    

    objects = AgentManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username