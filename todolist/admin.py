from django.contrib import admin
from .models import Item
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	list_display = ('title','begin','end','priority','text','finished')
	search_fields = ['title','text']

admin.site.register(Item,ItemAdmin)