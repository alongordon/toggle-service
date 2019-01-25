from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CountHeaderAdmin(admin.ModelAdmin):
	list_display = ('pk','count_date', 'description')


class CountLinesAdmin(admin.ModelAdmin):
	list_display = ('item_code', 'count_1', 'count_2', 'count_3', 'count_theoretical',)
	list_filter = ('count_header__description',)
	search_fields = ['item_code']


class ProfileInline(admin.TabularInline):
	model = Profile
	extra = 1


class TeamAdmin(admin.ModelAdmin):
	list_display = ('name',)
	inlines = [ProfileInline]


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'team',)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'count_1', 'count_2', 'count_3',)


admin.site.register(CountHeader, CountHeaderAdmin)
admin.site.register(CountLines, CountLinesAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)


