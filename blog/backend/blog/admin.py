from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published')
    list_display_links = ('id', 'title', 'author', 'published')
    search_fields = ('title', 'published', 'author')
    list_filter = ('published', 'author')

    def has_add_permission(self, request):
        return True
