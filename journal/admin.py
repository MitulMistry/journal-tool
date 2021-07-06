from django.contrib import admin
from .models import User, Entry, Activity, Distortion

# Register your models here.
admin.site.register(User)
admin.site.register(Entry)
admin.site.register(Activity)
admin.site.register(Distortion)