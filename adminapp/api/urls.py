from django.urls import path

from api import views

app_name = 'api'

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
]
