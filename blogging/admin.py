""" script blogging/admin.py """

# imports
from django.contrib import admin
from django.contrib.sites.models import Site
from blogging.models import Post, Category, Review 
# ----------------------------------------

admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class ReviewInline(admin.TabularInline):
    model = Review


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ReviewInline]
    list_display = ("title", "author", "created_date")


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

# ---------------------------------------
admin.site.register(Site, SiteAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
