from django.contrib import admin
from .models import Room, Request

# Register your models here.

@admin.register(Room)
class Room_Admin(admin.ModelAdmin):
    pass

@admin.register(Request)
class Request_Admin(admin.ModelAdmin):
    pass