from django.urls import path
from .views import CustomerDetail, CustomerList, CustomerCreate

urlpatterns = [
    path('agent/<int:pk>/cust-create/', CustomerCreate.as_view(), name='customer-create'),
    path('agent/<int:pk>/cust/', CustomerList.as_view(), name='customer-list'),
    path('cust/<int:pk>/',CustomerDetail.as_view() , name='customer-detail'),
    
]