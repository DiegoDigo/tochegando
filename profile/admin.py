from django.contrib import admin
from .models import Parent, Child


class AdminParent(admin.ModelAdmin):
    list_display = ['fullname', 'city']
    list_filter = ['city']


class AdminChild(admin.ModelAdmin):
    list_display = ['fullname', 'age', 'period', 'get_parent']
    list_filter = ['period', 'age']

    def get_parent(self, obj):
        return obj.parent.fullname

    get_parent.short_description = 'Responsaveu'


admin.site.register(Parent, AdminParent)
admin.site.register(Child, AdminChild)