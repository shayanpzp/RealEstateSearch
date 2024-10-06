from django.contrib import admin
from django.urls import path
from properties import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
    path('search/', views.search, name='search'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)