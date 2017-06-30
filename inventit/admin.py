from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CountHeaderAdmin(admin.ModelAdmin):
	list_display = ('pk','count_date', 'description')

admin.site.register(CountHeader,CountHeaderAdmin)

class CountLinesAdmin(admin.ModelAdmin):
	list_display = ('item_code', 'count_1', 'count_2', 'count_3', 'count_theoretical',)
	list_filter = ('count_header__description',)
	search_fields = ['item_code']

admin.site.register(CountLines, CountLinesAdmin)
