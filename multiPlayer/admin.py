from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Admin Displays

class GroupAdmin(admin.ModelAdmin):
  readonly_fields = ['uuid_group']
  list_display = ['name', 'id']

class RoomAdmin(admin.ModelAdmin):
  list_per_page = 15
  list_max_show_all = 50
  list_display = ['room_name', 'id', 'is_research']
  readonly_fields = ['password', 'is_research']

class GameSettingAdmin(admin.ModelAdmin):
  list_display = ['room', 'host', 'arithmetic', 'difficulty', 'speed', 'lvl']
  readonly_fields = ['room', 'host', 'arithmetic', 'difficulty', 'speed', 'lvl']

 # s
# Register your models here.
admin.site.register(Group, GroupAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(GameSetting, GameSettingAdmin)

