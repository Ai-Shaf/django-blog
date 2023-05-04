from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.post.through

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # inlines = [
    #     CategoryInline,
    # ]
    exclude = ["post"]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

