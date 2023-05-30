from django.contrib import admin

from .forms import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'Priorities', 'group', 'status', 'date_of_creation']
    form = TaskForm


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = GroupForm


class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'group']
    form = NotesForm


admin.site.register(Task, TaskAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Notes, NotesAdmin)
