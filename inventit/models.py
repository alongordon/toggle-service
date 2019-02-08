from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

#comment

class CountHeader(models.Model):
    count_date = models.DateTimeField(db_index=True, auto_now_add=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" % self.count_date

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


class CountLines(models.Model):
    count_header = models.ForeignKey(CountHeader)
    item_code = models.CharField(max_length=100)
    category = models.ForeignKey(
        to=Category, on_delete=models.DO_NOTHING, related_name="count_lines"
    )
    count_1 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count_2 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count_3 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count_theoretical = models.DecimalField(max_digits=9, decimal_places=2)

    def __unicode__(self):
        return "%s" % self.item_code

    def save(self):
        if self.count_1 == self.count_2:
            self.count_3 = self.count_1

        super(CountLines, self).save()
