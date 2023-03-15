from rest_framework import viewsets
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from agent.models import Agent



class CustomerCreate(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        agent = Agent.objects.get(pk = pk)
        serializer.save(created_by = agent)


class CustomerList(generics.ListAPIView):
    serializer_class = CustomerSerializer
    #permission_classes = [IsAuthenticated]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Customer.objects.filter(created_by = pk)
    
    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer