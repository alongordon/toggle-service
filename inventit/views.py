from django.http import HttpResponse
from django.shortcuts import render
from inventit.models import *
import json
from decimal import *

def capture1(request):

    template = "inventit/capture.html"

    count_headers = CountHeader.objects.all()

    count_lines = CountLines.objects.all()

    context = {'count_headers': count_headers, 'lines': count_lines, 'count': 1}

    return render(request, template, context)

def capture2(request):

    template = "inventit/capture.html"

    count_headers = CountHeader.objects.all()

    count_lines = CountLines.objects.all()

    context = {'count_headers': count_headers, 'lines': count_lines, 'count': 2}

    return render(request, template, context)

def summary(request):

	template = "inventit/summary.html"
    
	count_headers = CountHeader.objects.all()

	count_lines = CountLines.objects.all()

	summary_count1 = CountLines.objects.all().filter(count_1__gte=0).count()
	summary_count2 = CountLines.objects.all().filter(count_2__gte=0).count()
	summary_count3 = CountLines.objects.all().filter(count_3__gte=0).count()
	total = CountLines.objects.all().count()

	summary_count1Percentage = round((float(summary_count1) / float(total)) * 100, 1)
	summary_count2Percentage = round((float(summary_count2) / float(total)) * 100, 1)
	summary_count3Percentage = round((float(summary_count3) / float(total)) * 100, 1)

	counts = {
		'summary_count1': summary_count1,
		'summary_count2': summary_count2,
		'summary_count3': summary_count3,
		'summary_count1Percentage': summary_count1Percentage,
		'summary_count2Percentage': summary_count2Percentage,
		'summary_count3Percentage': summary_count3Percentage,
		'total':  total
	}
	

	context = {'count_headers': count_headers, 'lines': count_lines, 'counts': counts}

	return render(request, template, context)

def save_data(request):
	if request.method == 'POST':
		item_code = request.POST.get('item_code')
		count = request.POST.get('count')
		count_type = request.POST.get('count_type')

		response_data = {}
 
		if count_type == '1': 
			line = CountLines.objects.filter(item_code=item_code)

			if line.values()[0].get('count_2') == Decimal(count):
				line.update(count_1=count, count_3=count)
			else:
				line.update(count_1=count)


		if count_type == '2':
			line = CountLines.objects.filter(item_code=item_code)

			#import pdb; pdb.set_trace();
			if line.values()[0].get('count_1') == Decimal(count):
				line.update(count_2=count, count_3=count)
			else:
				line.update(count_2=count)

		if count_type == '3':
			CountLines.objects.filter(item_code=item_code).update(count_3=count)

		response_data['result'] = item_code + " saved!!!"

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)
