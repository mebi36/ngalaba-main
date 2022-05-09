from django.contrib import admin

from .models import Author, Post, Post_Section, Post_Category
# Register your models here.
class Post_Section_Inline(admin.TabularInline):
    model = Post_Section
    extra = 2
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post Author', {'fields': ['author']}),
        ('Post Details', {'fields': ['post_title','post_date', 'post_categories']})
    ]
    inlines = [Post_Section_Inline]


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Post_Category)