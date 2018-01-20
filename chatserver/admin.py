from django.contrib import admin
from .models import chats

# Register your models here.

class chatsAdmin(admin.ModelAdmin):
	class Meta:
		model = chats

admin.site.register(chats, chatsAdmin)