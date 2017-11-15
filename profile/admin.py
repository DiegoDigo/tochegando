from django.contrib import admin
from .models import Parent, Child, School


class AdminParent(admin.ModelAdmin):
    list_display = ['fullname', 'city']
    list_filter = ['city']


class AdminChild(admin.ModelAdmin):
    list_display = ['fullname', 'age', 'period']
    list_filter = ['period', 'age']


class AdminSchool(admin.ModelAdmin):
    list_display = ['nameschool', 'address', 'addressNumber']


admin.site.register(Parent, AdminParent)
admin.site.register(Child, AdminChild)
admin.site.register(School, AdminSchool)