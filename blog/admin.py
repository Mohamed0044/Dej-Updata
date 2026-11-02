from django.contrib import admin

# Register your models here.

from .models import Post, User, Category, Comment

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'title_id')
    list_filter = ('author', 'title', 'title_id')
    search_fields = ('title', 'author','title_id')
    ordering = ('title','title_id','author',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'post', 'created_at', 'updated_at')
    search_fields = ('content', 'author__username', 'post__title')
    ordering = ('-created_at',)    