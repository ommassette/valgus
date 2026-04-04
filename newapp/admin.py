from django.contrib import admin
from .models import Contact, Creative

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')

@admin.register(Creative)
class CreativeAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'role', 'profile_image_filename')