from django.contrib import admin


from .models import Category, News, Contact, Comment

# admin.site.register(Category)
# admin.site.register(News)

admin.site.register(Contact)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'status']
    list_filter = ['status', 'publish_time', 'category']
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

# 1-usul
# admin.site.register(Comment)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', "body", "created_time", "active"]
    list_filter = ["active", "created_time"]
    search_fields = ["user", "body"]


    def dicable_comments(self, request, queryset):
        queryset.update(avtive=False)

    def active_comments(self, request, queryset):
        queryset.update(active=True)

# admin.site.register(Comment, CommentAdmin)