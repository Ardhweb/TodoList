from django.contrib import admin

# Register your models here.
from .models import TodoListItem

@admin.register(TodoListItem)
class TodoListItemAdmin(admin.ModelAdmin):
    list_display =['content']