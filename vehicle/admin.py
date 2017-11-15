from django.contrib import admin
from .models import Vehicle, Driver


class AdminDriver(admin.ModelAdmin):
    list_display = ['fullname', 'category', 'getSchool', 'getVehicle']

    def getSchool(self, obj):
        return obj.School.name

    def getVehicle(self, obj):
        return obj.Vehicle.typevehicle


class AdminVehicle(admin.ModelAdmin):
    list_display = ['typevehicle', 'capacity']


admin.site.register(Vehicle, AdminVehicle)
admin.site.register(Driver, AdminDriver)

