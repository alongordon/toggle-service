from django.http import HttpResponse
from django.shortcuts import render
from inventit.models import *

def capture(request):

    template = "inventit/capture.html"
    
    count_headers = CountHeader.objects.all()

    context = {'count_headers': count_headers}

    return render(request, template, context)