from django.urls import path

from .views import *#user, user_list, files_make_dump

app_name = 'api'

urlpatterns = [
    path('users/<int:user_id>/', user, name='user'),
    path('users/list/', user_list, name='user_list'),
    path('files/make_dump/', files_make_dump, name='files_make_dump'),
    path('files/preview/', files_preview, name='files_preview'),
    path('files/save/', files_save, name='files_save'),
    path('files/delete/', files_delete, name='files_delete'),
    path('realese_notes/', release_notes, name='release_notes'),
    path('realese_notes/show', release_notes_show, name='release_notes_show'),
]