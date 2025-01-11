from django.contrib import admin
from .models import User, Category, Listing, Bid, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "category", "creator", "timestamp", "is_active")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "user", "amount", "timestamp")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "user", "listing", "timestamp")

admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)