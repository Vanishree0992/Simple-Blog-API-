from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from posts.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),   # browsable login
]
