from django.contrib import admin
from .models import Vehicle, Driver


class AdminDriver(admin.ModelAdmin):
    list_display = ['fullname', 'category', 'get_school', 'get_vehicle', 'get_city']

    def get_school(self, obj):
        return obj.school.nameschool

    def get_vehicle(self, obj):
        return ", ".join([v.typevehicle for v in obj.vehicle.all()])

    def get_city(self, obj):
        return obj.city.state

    get_school.short_description = 'escola'
    get_vehicle.short_description = 'Veiculos'
    get_city.short_description = 'cidade'


class AdminVehicle(admin.ModelAdmin):
    list_display = ['typevehicle', 'capacity']
    list_filter = ['capacity', 'typevehicle']
    ordering = ['capacity', 'typevehicle']


admin.site.register(Vehicle, AdminVehicle)
admin.site.register(Driver, AdminDriver)

