""" script blogging/admin.py """

# imports
from django.contrib import admin
from blogging.models import Post, Category
# ----------------------------------------

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]
    list_display = ("title", "author", "created_date")

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

# ---------------------------------------

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
