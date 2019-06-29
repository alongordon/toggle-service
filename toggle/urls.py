from django.urls import path
from django.contrib import admin
from inventit import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/", views.summary, name="summary"),
    path("capture1", views.capture1, name="capture1"),
    path("capture2", views.capture2, name="capture2"),
    path("capture3", views.capture3, name="capture3"),
    path("save_data/", views.save_data, name="save_data"),
    path("save_count_summary/", views.save_count_summary, name="save_count_summary"),
    path("export", views.export, name="export"),
]
