from django.contrib import admin

from .models import *

class CountHeaderAdmin(admin.ModelAdmin):
	list_display = ('count_date', 'description')
    
class CountLinesAdmin(admin.ModelAdmin):
	list_display = ('item_code', 'count_1', 'count_2', 'count_3', 'count_theoretical')
	#list_filter = ('item_code',)

admin.site.register(CountHeader,CountHeaderAdmin)
admin.site.register(CountLines, CountLinesAdmin)
