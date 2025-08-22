"""
URL configuration for agrigenius project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from marketplace.views import CropViewSet, ListingViewSet, OrderViewSet
from dashboard.views import UserActivityViewSet, SalesAnalyticsViewSet
from schemes.views import SchemeViewSet
from disease_detection.views import DiseaseDetectionRequestViewSet


from .frontend_view import FrontendAppView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'crops', CropViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'user-activity', UserActivityViewSet)
router.register(r'sales-analytics', SalesAnalyticsViewSet)
router.register(r'schemes', SchemeViewSet)
router.register(r'disease-detection', DiseaseDetectionRequestViewSet)

urlpatterns = [
    path('', FrontendAppView.as_view(), name='react-frontend-root'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('users.urls')),
    # Catch-all for React frontend (after all API and admin routes)
    path('<path:path>', FrontendAppView.as_view(), name='react-frontend'),
]
