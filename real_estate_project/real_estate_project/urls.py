from django.contrib import admin
from django.urls import path, include
from properties import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from properties.views import PropertyViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
    path('search/', views.search, name='search'),
    path('api/', include(router.urls)),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)