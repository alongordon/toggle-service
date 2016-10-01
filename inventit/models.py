from __future__ import unicode_literals

from django.db import models

class CountHeader(models.Model):
    count_date = models.DateTimeField(db_index=True, auto_now_add=True)
    description = models.TextField(null=True)
    
    def __unicode__(self):
        return '%s' % self.count_date
        
class CountLines(models.Model):
    count_header = models.ForeignKey(CountHeader)
    item_code = models.CharField(max_length=100)
    count_1 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count_2 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count_3 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count_theoretical = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __unicode__(self):
        return '%s' % self.item_code

    def save(self):
        if self.count_1 == self.count_2:
            self.count_3 = self.count_1

        super(CountLines, self).save()