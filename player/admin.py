from django.contrib import admin

from .models import Inventory, Profile, Leaderboard


class InventoryModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'count')


admin.site.register(Inventory, InventoryModelAdmin)


class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience', 'island', 'fcm_token')


admin.site.register(Profile, ProfileModelAdmin)

admin.site.register(Leaderboard)