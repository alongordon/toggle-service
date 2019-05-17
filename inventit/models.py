from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class CountHeader(models.Model):
    count_date = models.DateTimeField(db_index=True, auto_now_add=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.DO_NOTHING, related_name="profiles"
    )
    team = models.ForeignKey(
        to=Team, on_delete=models.DO_NOTHING, related_name="profiles"
    )

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    count_1 = models.ForeignKey(
        to=Team, on_delete=models.DO_NOTHING, related_name="categories_count_1"
    )
    count_2 = models.ForeignKey(
        to=Team, on_delete=models.DO_NOTHING, related_name="categories_count_2"
    )
    count_3 = models.ForeignKey(
        to=Team, on_delete=models.DO_NOTHING, related_name="categories_count_3"
    )

    def __str__(self):
        return self.name


class Inventory(models.Model):
    item_code = models.CharField(max_length=100)
    count_theoretical = models.DecimalField(max_digits=9, decimal_places=2)
    count_summary = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return self.item_code

    def save(self, *args, **kwargs):
        count_lines = CountLines.objects.filter(inventory__item_code=self.item_code)

        sum = 0

        for count_line in count_lines:
            if count_line.count_3:
                sum += count_line.count_3

        self.count_summary = sum
        super(Inventory, self).save(*args, **kwargs)


class CountLines(models.Model):
    count_header = models.ForeignKey(CountHeader)
    category = models.ForeignKey(
        to=Category, on_delete=models.DO_NOTHING, related_name="count_lines"
    )
    inventory = models.ForeignKey(
        to=Inventory, on_delete=models.DO_NOTHING, related_name="count_lines"
    )
    count_1 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count_2 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count_3 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return "%s" % self.inventory.item_code

    def save(self):
        if self.count_1 == self.count_2:
            self.count_3 = self.count_1

        super(CountLines, self).save()
