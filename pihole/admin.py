from django.contrib import admin
from .models import FTL
import socket

# Register your models here.

class ClientFilter(admin.SimpleListFilter):
    title = 'Client'
    parameter_name = 'client'

    def lookups(self, request, model_admin):
        list_of_clients =[]
        queryset = FTL.objects.values_list('client').distinct()
        for client in queryset:
            list_of_clients.append((str(client[0]),client[0]))
        return sorted(list_of_clients, key= lambda item: socket.inet_aton(item[0]))

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(client=self.value())
        return queryset

class StatusFilter(admin.SimpleListFilter):
    title = 'Action'
    parameter_name = 'action'

    def lookups(self, request, model_admin):
        status = [(1,'Blocked'),(2,'Forwarded'),(3,'Cached'),(4,'Answered (Forwarded or Cached)')]
        return sorted(status)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset


class FTLAdmin(admin.ModelAdmin):
    list_display = ('time', 'new_status', 'domain', 'client')
    search_fields = ('domain', 'client')
    list_filter = (ClientFilter,StatusFilter,)


admin.site.register(FTL, FTLAdmin)
