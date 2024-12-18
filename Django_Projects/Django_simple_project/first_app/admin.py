from django.contrib import admin
from first_app.models import Topic_class, Web_Access_Record, Web_page_class

# Register your models here.
admin.site.register(Topic_class)
admin.site.register(Web_Access_Record)
admin.site.register(Web_page_class)
