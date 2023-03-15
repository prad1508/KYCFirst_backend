
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from agent.views import  MyTokenObtainPairView
from company.views import CompanyApi, LocationApi
from product.views import ProductApi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework.decorators import api_view

router=DefaultRouter()
#router.register('agent',AgentAPI,basename='agent')
router.register('comp',CompanyApi, basename='comp')
router.register('loc',LocationApi, basename='loc')
router.register('prod',ProductApi, basename='prod')

@api_view(['GET'])
def getroutes(request):
    routes = [
        '/api/login/',
        '/api/agents/',
        '/api/agent/<int:pk>/',
        '/api/registerAgent/',
        '/api/comp/',
        '/api/loc/',
        '/api/prod/',
    ]
    return Response(routes)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("api-auth/", include("rest_framework.urls")), 
    path('api/', include('agent.urls')),
    path('api/', include('customer.urls')),
    path('api/', include(router.urls)),
    path('', getroutes),
    #path('api/access_token/', MyTokenObtainPairView.as_view()),
    path('api/refresh_token/', TokenRefreshView.as_view())
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

