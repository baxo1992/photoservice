from django.contrib import admin

from .models import Profile, UserFilesUpload


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'phone_number']


@admin.register(UserFilesUpload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['owner', 'session_type', 'uploaded_by', 'upload_date']
