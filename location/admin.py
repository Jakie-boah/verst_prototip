from django.contrib import admin
from .models import Locations
# Register your models here.


class LocationTabularInline(admin.TabularInline):
    model = Locations
