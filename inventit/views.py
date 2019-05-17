from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from inventit.models import *
import json
from decimal import *
import csv
from django.conf import settings


@login_required()
def capture1(request):
    template = "inventit/capture.html"

    profile = Profile.objects.get(user=request.user)

    # my allowed categories
    categories = Category.objects.filter(count_1=profile.team)

    count_header = CountHeader.objects.filter(is_active=True)

    count_lines = CountLines.objects.filter(
        Q(count_header=count_header.first()) & Q(category__in=categories)
    )

    context = {"count_headers": count_header, "lines": count_lines, "count": 1}

    return render(request, template, context)


@login_required()
def capture2(request):
    template = "inventit/capture.html"

    profile = Profile.objects.get(user=request.user)

    # my allowed categories
    categories = Category.objects.filter(count_2=profile.team)

    count_header = CountHeader.objects.filter(is_active=True)

    count_lines = CountLines.objects.filter(
        Q(count_header=count_header.first()) & Q(category__in=categories)
    )

    context = {"count_headers": count_header, "lines": count_lines, "count": 2}

    return render(request, template, context)


@login_required()
def capture3(request):
    template = "inventit/capture.html"

    profile = Profile.objects.get(user=request.user)

    # my allowed categories
    categories = Category.objects.filter(count_3=profile.team)

    count_header = CountHeader.objects.filter(is_active=True)

    count_lines = CountLines.objects.filter(
        Q(count_header=count_header.first()) & Q(category__in=categories)
    )
    context = {"count_headers": count_header, "lines": count_lines, "count": 3}

    return render(request, template, context)


@login_required()
def summary(request):
    template = "inventit/summary.html"

    count_header = CountHeader.objects.filter(is_active=True)

    inventory = (
        Inventory.objects.all()
    )  # CountLines.objects.filter(count_header=count_header.first())

    summary_count1 = (
        CountLines.objects.filter(count_header=count_header.first())
        .filter(count_1__gte=0)
        .count()
    )
    summary_count2 = (
        CountLines.objects.filter(count_header=count_header.first())
        .filter(count_2__gte=0)
        .count()
    )
    summary_count3 = (
        CountLines.objects.filter(count_header=count_header.first())
        .filter(count_3__gte=0)
        .count()
    )
    total = CountLines.objects.filter(count_header=count_header.first()).count()

    summary_count1Percentage = 0
    summary_count2Percentage = 0
    summary_count3Percentage = 0

    if summary_count1Percentage:
        summary_count1Percentage = round(
            (float(summary_count1) / float(total)) * 100, 1
        )
    if summary_count2Percentage:
        summary_count2Percentage = round(
            (float(summary_count2) / float(total)) * 100, 1
        )
    if summary_count3Percentage:
        summary_count3Percentage = round(
            (float(summary_count3) / float(total)) * 100, 1
        )

    counts = {
        "summary_count1": summary_count1,
        "summary_count2": summary_count2,
        "summary_count3": summary_count3,
        "summary_count1Percentage": summary_count1Percentage,
        "summary_count2Percentage": summary_count2Percentage,
        "summary_count3Percentage": summary_count3Percentage,
        "total": total,
    }

    context = {"count_headers": count_header, "inventory": inventory, "counts": counts}

    return render(request, template, context)


@login_required()
def save_count_summary(request):
    if request.method == "POST":
        pk = request.POST.get("pk")
        value = request.POST.get("value")

        inventory = Inventory.objects.get(pk=pk)
        inventory.count_summary = value
        inventory.save()

        response_data = {"result": "Saved!!!"}

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json",
        )


@login_required()
def save_data(request):
    if request.method == "POST":
        pk = request.POST.get("pk")
        count = request.POST.get("count")
        count_type = request.POST.get("count_type")

        response_data = {}

        if count_type == "1":
            line = CountLines.objects.filter(pk=pk)

            if line.values()[0].get("count_2") == Decimal(count):
                line.update(count_1=count, count_3=count)
            else:
                line.update(count_1=count)

        elif count_type == "2":
            line = CountLines.objects.filter(pk=pk)

            # import pdb; pdb.set_trace();
            if line.values()[0].get("count_1") == Decimal(count):
                line.update(count_2=count, count_3=count)
            else:
                line.update(count_2=count)

        else:
            line = CountLines.objects.filter(pk=pk)
            line.update(count_3=count)

        # Update the Inventory count summary
        count_lines = CountLines.objects.filter(inventory__item_code=line.first().inventory.item_code)

        sum = 0
        for count_line in count_lines:
            if count_line.count_3:
                sum += count_line.count_3

        inventory = Inventory.objects.filter(item_code=line.first().inventory.item_code).first()

        if inventory:
            inventory.count_summary = sum
            inventory.save()

        response_data["result"] = "Saved!!!"

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json",
        )


@login_required()
def export(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    writer.writerow(["Item Code", "Count 1", "Count 2", "Count 3", "Theoretical"])

    count_header = CountHeader.objects.filter(is_active=True)

    for countLine in CountLines.objects.filter(count_header=count_header.first()):
        writer.writerow(
            [
                countLine.item_code,
                countLine.count_1,
                countLine.count_2,
                countLine.count_3,
                countLine.count_theoretical,
            ]
        )

    return response
