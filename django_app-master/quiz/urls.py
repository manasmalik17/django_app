from django.contrib import admin
from django.urls import path, include
from dj import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dj.urls')),
]
