from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Card(models.Model):
    card_name = models.CharField(max_length=200)
    acquired_date = models.DateTimeField('date acquired')
    player_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    year = models.IntegerField(default=2015)
    condition = models.FloatField(default = 10.0)
    rookie_card = models.BooleanField(default=False)
    auto = models.BooleanField(default=False)
    patch = models.BooleanField(default=False)
    double_auto = models.BooleanField(default=False)
    double_patch = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.card_name
    
    def was_acquired_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_acquired_recently.admin_order_field = 'acquired_date'
    was_acquired_recently.boolean = True
    was_acquired_recently.short_description = 'acquired recently?'
    

    