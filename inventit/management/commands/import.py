from django.core.management.base import BaseCommand, CommandError
from inventit.models import *
import csv
import os
from django.conf import settings

class Command(BaseCommand):

	help = "Import CountLines"

	def handle(self, *args, **options):

		with open(os.path.join(settings.ROOT_PATH, '../inventit/data/import.csv'), 'rb') as file:
			rows = csv.reader(file, delimiter=",", quotechar='"')

			for row in rows:

				if rows.line_num == 1:
					continue

				#print "item_code: " + row[0]
				#print "count_theoretical:  " + row[1]

				db_row = CountLines(item_code=row[0], count_theoretical=row[1], count_header_id=1)
				db_row.save()

			# dump entire table
			for count_lines in CountLines.objects.all():
				print count_lines


