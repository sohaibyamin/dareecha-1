from django.contrib import admin
from django.contrib.admin import ModelAdmin

from baham.models import VehicleModel, UserProfile


# Register your models here.
@admin.register(VehicleModel)
class VehicleModelAdmin(ModelAdmin):
    # Define the fields to display in main view
    list_display = ('vendor', 'type', 'capacity')
    # Define the fields that can be used to filter records
    list_filter = ('vendor', 'type', 'model')

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ('user', 'gender', 'type', 'town')
    list_filter = ('type', 'town')

    def has_delete_permission(self, request, obj=None):
        return False
