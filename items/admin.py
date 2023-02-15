from django.contrib import admin
from .models import TestItemModel
from location.admin import LocationTabularInline
# Register your models here.


class TestItemModelAdmin(admin.ModelAdmin):
    inlines = [LocationTabularInline]

    class Meta:
        model = TestItemModel


admin.site.register(TestItemModel, TestItemModelAdmin)

