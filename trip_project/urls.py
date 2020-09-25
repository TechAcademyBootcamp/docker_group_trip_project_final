"""trip_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('',include('Main.urls',namespace='main')),
    path('tours/',include('Tours.urls', namespace='tours')),
    path('account/',include('Account.urls', namespace='account')),
    path('api/v1.0/',include('Main.api.urls',namespace='api_main')),
    path('hotels/',include('Hotels.urls',namespace='hotels_app')),
    path('', include('social_django.urls', namespace="social")),
    path('restaurants/',include('Restaurants.urls',namespace='restaurants_app')),
    path('places/',include('Places.urls',namespace='places_app')),
    path('api/v1.0/restaurants/',include('Restaurants.api.urls',namespace='api_restaurant'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
