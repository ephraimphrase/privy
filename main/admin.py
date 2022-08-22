from django.contrib import admin
from .models import chatRoom, Message

# Register your models here.
admin.site.register(chatRoom)
admin.site.register(Message)