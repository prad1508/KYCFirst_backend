from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('agents/',views.AgentsApi.as_view(), name ='agents'),
    path('agent/<int:pk>/',views.AgentApi.as_view(), name='agent'),
    path('registerAgent/',views.RegisterAgent.as_view(), name ='registerAgent'),
]
