from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('entries/new', views.new_entry, name='new_entry'),
    path('entries/<int:id>', views.entry, name='entry'),
    path('entries/<int:id>/edit', views.edit_entry, name='edit_entry'),
    path('entries/<int:id>/delete', views.delete_entry, name='delete_entry'),
    path('distortions', views.distortions, name='distortions'),
    path('activities/new', views.new_activity, name='new_activity'),
    path('activities/<int:id>/edit', views.edit_activity, name='edit_activity'),
    path('activities/<int:id>/delete', views.delete_activity, name='delete_activity'),
    path('users/<int:id>', views.user_profile, name='user_profile')
]