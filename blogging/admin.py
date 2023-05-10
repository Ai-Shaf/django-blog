from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):  # altered for Lesson 7
    model = Category.post.through


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ["post"]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

