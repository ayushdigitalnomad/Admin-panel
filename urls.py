from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_instance/', views.add_instance, name='add_instance'),
    path('list_instances/', views.list_instances, name='list_instances'),
    path('create_user/', views.create_user, name='create_user'),
    path('list_users/', views.list_users, name='list_users'),
    path('change_password/<int:user_id>/', views.change_password, name='change_password'),
    path('remove_user/<int:user_id>/', views.remove_user, name='remove_user'),
    path('assign_role/', views.assign_role, name='assign_role'),
    path('restricted/', views.restricted_view, name='restricted_view'),
    path('remove_database/<int:database_id>/', views.remove_database, name='remove_database'),
    path('remove_user_access/<int:user_id>/<int:database_id>/', views.remove_user_access, name='remove_user_access'),
    path('assign_user_to_database/', views.assign_user_to_database, name='assign_user_to_database'),
]

