from rest_framework import viewsets
from rest_framework.response import Response
from .models import Agent
from .serializers import AgentSerializer,AgentSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, APIView
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .permissions import AdminReadOnly



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['Agent Username'] = user.username
        return token
    
    
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        
        serializer = AgentSerializerWithToken(self.user).data
        
        for k,v in serializer.items():
            data[k] = v

        return data  
    """
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class AgentsApi(APIView):
    def get(self, request):
                agents = Agent.objects.all()
                serializer = AgentSerializer(agents, many = True)
                return Response(serializer.data)
    #permission_classes = [IsAdminUser]
    
    
class AgentApi(APIView):
    permission_classes = [AdminReadOnly]
    def get(self, request, pk):
        try:
            agent = Agent.objects.get(pk = pk)
            serializer = AgentSerializer(agent)
            return Response(serializer.data)
        except Agent.DoesNotExist:
            return Response(data={'msg': 'Agent You are looking for doesnot exist'})
    
    
    def put(self, request, pk):
        agent = Agent.objects.get(pk=pk)
        
        serializer = AgentSerializer(agent, data=request.data)
        if serializer.is_valid():
            # agent.password=make_password(agent.password)
            # print(agent.password)
            # agent.save()
            password = serializer.validated_data.get('password')
            serializer.validated_data['password']=make_password(password)
            serializer.save()
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        agent = Agent.objects.get(pk=pk)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
      
    
class RegisterAgent(APIView):
    def post(self, request):
        data = request.data
        
        agent = Agent.objects.create(
            username = data['username'],
            email = data['email'],
            password = make_password(data['password']),
            #biometric_details = data['biometric_details'],
            mobile_no = data['mobile_no'],
        )   
        serializer = AgentSerializerWithToken(agent, many=False)
        return Response(data=serializer.data)
                   

