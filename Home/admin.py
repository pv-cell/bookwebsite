from django.contrib import admin
from Home.models import Contact
from Home.models import Sell
from Home.models import Book

# Register your models here.
admin.site.register(Contact)
admin.site.register(Sell)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')

# admin.site.register(User)
