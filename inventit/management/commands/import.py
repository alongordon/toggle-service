from django.core.management.base import BaseCommand, CommandError
from inventit.models import *
import csv
import os
from django.conf import settings


class Command(BaseCommand):
    help = "Import CountLines"

    def handle(self, *args, **options):

        CountLines.objects.all().delete()
        Inventory.objects.all().delete()
        # Category.objects.all().delete()

        with open(
            os.path.join(settings.ROOT_PATH, "../inventit/data/inventory.csv"), "r"
        ) as file:
            rows = csv.reader(file, delimiter=",", quotechar='"')

            for row in rows:
                if rows.line_num == 1:
                    continue
                Inventory.objects.create(item_code=row[0], count_theoretical=row[1])

        # CATEGORIES
        # team = Team.objects.all().first()
        # with open(
        #     os.path.join(settings.ROOT_PATH, "../inventit/data/categories.csv"), "r"
        # ) as file:
        #     rows = csv.reader(file, delimiter=",", quotechar='"')
        #
        #     for row in rows:
        #         if rows.line_num == 1:
        #             continue
        #         Category.objects.create(
        #             name=row[0], count_1=team, count_2=team, count_3=team
        #         )

        with open(
            os.path.join(settings.ROOT_PATH, "../inventit/data/count_lines.csv"), "r"
        ) as file:
            rows = csv.reader(file, delimiter=",", quotechar='"')
            count_header = CountHeader.objects.filter(is_active=True).first()

            for row in rows:
                if rows.line_num == 1:
                    continue

                # print "item_code: " + row[0]
                # print "count_theoretical:  " + row[1]

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

        # dump entire table
        # for count_lines in CountLines.objects.filter(count_header=count_header):
        # 	print(count_lines)
