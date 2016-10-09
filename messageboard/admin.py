from django.contrib import admin
from .models import Message
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'pub_time']
    ordering = ['pub_time']

admin.site.register(Message, MessageAdmin)
