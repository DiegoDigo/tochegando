from django.contrib import admin
from .models import Parent, Child, School, City


class AdminParent(admin.ModelAdmin):
    list_display = ['fullname', 'get_city']

    def get_city(self, obj):
        return obj.city.state

    get_city.short_description = 'cidade'


class AdminChild(admin.ModelAdmin):
    list_display = ['fullname', 'age', 'period']
    list_filter = ['period', 'age']


class AdminSchool(admin.ModelAdmin):
    list_display = ['nameschool', 'address', 'addressNumber', 'get_city']

    def get_city(self, obj):
        return obj.city.state

    get_city.short_description = 'cidade'


class AdminCity(admin.ModelAdmin):
    list_display = ['state', 'uf']
    list_filter = ['uf', 'state']


admin.site.register(Parent, AdminParent)
admin.site.register(Child, AdminChild)
admin.site.register(School, AdminSchool)
admin.site.register(City, AdminCity)