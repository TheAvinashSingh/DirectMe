from django.contrib import admin

from .models import Inventory, Profile


class InventoryModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'count')


admin.site.register(Inventory, InventoryModelAdmin)


class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience', 'island', 'fcm_token', 'cumulative_ship_level', 'last_seen')


admin.site.register(Profile, ProfileModelAdmin)
