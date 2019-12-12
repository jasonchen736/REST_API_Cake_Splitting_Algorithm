from django.db import models


class Cake(models.Model):
    id = models.AutoField(primary_key=True)
    pattern = models.CharField(max_length=200, blank=False, db_index=True)
    size = models.IntegerField(blank=False)
    smallest_repeating_segment = models.CharField(max_length=200, blank=False)
    smallest_repeating_segment_size = models.IntegerField(blank=False)
    repetitions = models.IntegerField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
