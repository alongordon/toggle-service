from .models import *
from django.contrib import admin
from django.contrib import messages
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CountHeaderAdmin(admin.ModelAdmin):
    list_display = ("count_date", "description", "is_active")
    list_filter = ("is_active",)


class CountLinesAdmin(ImportExportModelAdmin):
    list_display = ("inventory", "category", "count_1", "count_2", "count_3")
    list_filter = ("count_header__description", "category")
    search_fields = ["inventory__item_code"]
    save_as = True
    actions = ['delete_all']

    def delete_all(self, request, queryset):
        CountLines.objects.all().delete()
    delete_all.short_description = "Delete all"

    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'delete_all':
            data = request.POST.copy()
            data['select_across'] = '1'
            request.POST = data
            response = self.response_action(request, queryset=self.get_queryset(request))
            if response:
                return response

        return super(CountLinesAdmin, self).changelist_view(request, extra_context)


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [ProfileInline]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "team")


class CategoryAdmin(ImportExportModelAdmin):
    list_display = ("name", "count_1", "count_2", "count_3")


class CountLinesInline(admin.TabularInline):
    model = CountLines
    extra = 1


class InventoryAdmin(ImportExportModelAdmin):
    list_display = ("item_code", "count_theoretical", "count_summary")
    actions = ['delete_all']
    inlines = [CountLinesInline]
    search_fields = ["item_code"]

    def delete_all(self, request, queryset):
        queryset = Inventory.objects.all()
        if queryset.filter(count_lines__isnull=False):
            messages.error(request, 'First remove all count lines')
        else:
            queryset.all().delete()
    delete_all.short_description = "Delete all"

    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'delete_all':
            data = request.POST.copy()
            data['select_across'] = '1'
            request.POST = data
            response = self.response_action(request, queryset=self.get_queryset(request))
            if response:
                return response

        return super(InventoryAdmin, self).changelist_view(request, extra_context)


class CountLinesResource(resources.ModelResource):
    class Meta:
        model = CountLines


admin.site.register(CountHeader, CountHeaderAdmin)
admin.site.register(CountLines, CountLinesAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventory, InventoryAdmin)
