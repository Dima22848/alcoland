from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'alcogol', AlcogolViewSet)

urlpatterns = [
    path('', Menu, name='main'),
    path('<slug:slug>/<int:pk>/', AlcogolSolo, name='alcogol-solo'),
    path('contatc/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/alcogol/
    # path('api/v1/alcogollist', AlcogolViewSet.as_view({'get': 'list'})),
    # path('api/v1/alcogollist/<int:pk>/', AlcogolViewSet.as_view({'get': 'retrieve'})),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)