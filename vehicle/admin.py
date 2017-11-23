from django.contrib import admin
from .models import Vehicle, Driver


class AdminDriver(admin.ModelAdmin):
    list_display = ['fullname', 'get_school', 'get_city']

    def get_school(self, obj):
        return obj.school.nameschool

    def get_city(self, obj):
        return obj.city.state

    get_school.short_description = 'escola'
    get_city.short_description = 'cidade'


class AdminVehicle(admin.ModelAdmin):
    list_display = ['typevehicle', 'capacity', 'isDeficiente']
    ordering = ['capacity', 'typevehicle']


admin.site.register(Vehicle, AdminVehicle)
admin.site.register(Driver, AdminDriver)

