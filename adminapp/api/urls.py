from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api import views

app_name = 'api'

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('users/<int:user_id>/', views.user, name='user'),
    path('users/list/', views.user_list, name='user_list'),
    path('files/make_dump/', views.files_make_dump, name='files_make_dump'),
    path('files/preview/', views.files_preview, name='files_preview'),
    path('files/save/', views.files_save, name='files_save'),
    path('files/delete/', views.files_delete, name='files_delete'),
    path('release_notes/', views.release_notes, name='release_notes'),
    path('release_notes/show', views.release_notes_show,
         name='release_notes_show'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
