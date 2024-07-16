from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'deadline', 'done')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('done',)

    def has_add_permission(self, request):
        return True
