from django.contrib import admin
from .models import Service, Advantage, Counter, Contact


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date_created', 'date_modified')
    search_fields = ('title', )
    list_filter = ('date_created', )


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date_created', 'date_modified')
    search_fields = ('title', )
    list_filter = ('date_created', )


class CounterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count', 'date_created', 'date_modified')
    search_fields = ('title', )
    list_filter = ('date_created', )


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'type_of_service', 'date_created', 'date_modified')
    search_fields = ('full_name', 'phone')
    list_filter = ('date_created', 'type_of_service')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(Counter, CounterAdmin)
admin.site.register(Contact, ContactAdmin)
