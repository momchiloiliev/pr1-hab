from django.contrib import admin
from .models import *
# Register your models here.

class AirLinePilotAdmin(admin.TabularInline):
    model = AirLinePilot
    extra = 0

class AirLineAdmin(admin.ModelAdmin):
    inlines = [AirLinePilotAdmin,]
    list_display = ("name",)

admin.site.register(AirLine, AirLineAdmin)

class FlightAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Flight, FlightAdmin)
admin.site.register(Balloon)

class PilotAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")

admin.site.register(Pilot, PilotAdmin)

