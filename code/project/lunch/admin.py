from django.contrib import admin
from lunch.models import UserProfile, Menu, Recipe

# Register your models here.
admin.site.register([UserProfile, Menu, Recipe])
