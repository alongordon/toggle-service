from .models import *
from django.contrib import admin


class CountHeaderAdmin(admin.ModelAdmin):
    list_display = ('count_date', 'description', 'is_active')
    list_filter = ('is_active',)


class CountLinesAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'category', 'count_1', 'count_2', 'count_3',)
    list_filter = ('count_header__description', 'category')
    search_fields = ['inventory__item_code']
    save_as = True


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


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'count_theoretical', 'count_summary')


admin.site.register(CountHeader, CountHeaderAdmin)
admin.site.register(CountLines, CountLinesAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventory, InventoryAdmin)
