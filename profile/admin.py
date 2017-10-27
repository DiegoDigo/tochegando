from django.contrib import admin
from .models import Parent, Child


class AdminParent(admin.ModelAdmin):
    list_display = ['fullname', 'city']
    list_filter = ['city']


class AdminChild(admin.ModelAdmin):
    list_display = ['fullname', 'age', 'period']
    list_filter = ['period', 'age']


admin.site.register(Parent, AdminParent)
admin.site.register(Child, AdminChild)