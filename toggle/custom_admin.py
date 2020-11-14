from django.urls import reverse
from django.contrib.admin import AdminSite


class CustomAdmin(AdminSite):
    def login(self, request, extra_context=None):
        data = request.POST.copy()
        data['next'] = reverse('capture1')
        request.POST = data
        return super(CustomAdmin, self).login(request, extra_context=None)
