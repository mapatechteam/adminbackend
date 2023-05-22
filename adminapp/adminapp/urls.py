from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lectonic_admin/api/', include('api.urls')),
]
