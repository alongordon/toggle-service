from django.core.management.base import BaseCommand, CommandError
from inventit.models import *
import csv
import os
from django.conf import settings

class Command(BaseCommand):

	help = "Import CountLines"

	def handle(self, *args, **options):

		with open(os.path.join(settings.ROOT_PATH, '../inventit/data/Jan2019_count.csv'), 'r') as file:
			rows = csv.reader(file, delimiter=",", quotechar='"')
			count_header = CountHeader.objects.filter(is_active=True).first()

			for row in rows:

				if rows.line_num == 1:
					continue

				#print "item_code: " + row[0]
				#print "count_theoretical:  " + row[1]

				# inventory = Inventory.objects.create(item_code=row[0], count_theoretical=row[1])

				# category = Category.objects.filter(name=row[2]).first()
				#db_row = CountLines(category=category, inventory=inventory, count_header=count_header)
				# db_row.save()

			# dump entire table
			for count_lines in CountLines.objects.filter(count_header=count_header):
				print(count_lines)


