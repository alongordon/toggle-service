from django.core.management.base import BaseCommand, CommandError
from inventit.models import *
import csv
import os
from django.conf import settings


class Command(BaseCommand):
    help = "Import CountLines"

    def handle(self, *args, **options):

        with open(
            os.path.join(settings.ROOT_PATH, "../inventit/data/count_lines_append.csv"),
            "r",
        ) as file:
            rows = csv.reader(file, delimiter=",", quotechar='"')
            count_header = CountHeader.objects.filter(is_active=True).first()

            for row in rows:
                if rows.line_num == 1:
                    continue

                inventory = Inventory.objects.filter(
                    item_code=row[0].replace(" ", "")
                ).first()

                if not inventory:
                    print("cannot find inventory -- ", row[0])
                    continue

                category = Category.objects.filter(name=row[1].strip()).first()

                if not category:
                    print("cannot find category -- ", row[1])
                    continue
                db_row = CountLines(
                    category=category, inventory=inventory, count_header=count_header
                )
                db_row.save()
