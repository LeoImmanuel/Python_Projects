from django.contrib import admin
from user_app.models import Author_class, Book_class, Book_published

# Register your models here.
admin.site.register(Author_class)
admin.site.register(Book_class)
admin.site.register(Book_published)