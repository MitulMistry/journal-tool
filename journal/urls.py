from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('register', views.register_user, name='register_user'),
    path('edit', views.edit_user, name='edit_user'),
    path('delete', views.delete_user, name='delete_user'),
    path('entries', views.entries, name='entries'),
    path('entries/new', views.new_entry, name='new_entry'),
    path('entries/<int:id>', views.entry, name='entry'),
    path('entries/<int:id>/edit', views.edit_entry, name='edit_entry'),
    path('entries/<int:id>/delete', views.delete_entry, name='delete_entry'),
    path('distortions', views.distortions, name='distortions'),
    path('activities/new', views.new_activity, name='new_activity'),
    path('activities/edit', views.edit_activities, name='edit_activities'),
    path('activities/<int:id>/edit', views.edit_activity, name='edit_activity'),
    path('activities/<int:id>/delete', views.delete_activity, name='delete_activity'),
    path('profile', views.user_profile, name='user_profile')
]