from rest_framework import serializers
from .models import Agent
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.hashers import make_password

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        username = serializers.CharField(max_length=50)
        email = serializers.CharField(max_length=50)
        Checker = serializers.BooleanField()
        Maker = serializers.BooleanField()
        Approver = serializers.BooleanField()
        first_name = serializers.CharField(max_length=50)
        last_name = serializers.CharField(max_length=50)
        gender = serializers.CharField(max_length=50)
        location = serializers.CharField(max_length=50)
        company = serializers.CharField(max_length=50)
        document_type = serializers.CharField(max_length=50)
        document_no = serializers.CharField(max_length=50)
        document_image = serializers.ImageField()
        biometric_details = serializers.ImageField()
        photograph = serializers.ImageField()
        mobile_no = PhoneNumberField
        aadhar_no = serializers.CharField(max_length=50)
        front_img = serializers.ImageField()
        back_img = serializers.ImageField()
        password = serializers.CharField(write_only=True)
                
        model = Agent
        fields = ['id','username', 'email','password','Checker','Maker','Approver','first_name', 'last_name','gender','company','location','document_type','mobile_no','biometric_details']
     
    # def create(self, validated_data):
    #     user = Agent(
    #     username=validated_data['username'],
    #     password=validated_data['password']
    #         )
    #     print(user.password)
    #     user.set_password(make_password(validated_data['password']))
    #     user.save()
    #     return user
    
    # def create(self, validated_data):
    #     return Agent.objects.create_user(**validated_data)

       
class AgentSerializerWithToken(AgentSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Agent
        fields = ['id','username', 'email','password','Checker','Maker','Approver','first_name', 'last_name','gender','company','location','document_type','token']
    
  
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)