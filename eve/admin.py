from django.contrib import admin
from .models import File


# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'cloudUrl', 'prediction', 'isCorrect', 'userSuggestion']


admin.site.register(File, FileAdmin)
