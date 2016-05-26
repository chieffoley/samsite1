from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
import os


# Create your models here.

class CardPack(models.Model):
    vendor = models.CharField(max_length=100)
    pack_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    comments = models.CharField(max_length=2000, blank=True)
    acquired_date = models.DateTimeField('date acquired', default=timezone.now)
    def __str__(self):
        return self.pack_name
    

def get_image_path(instance, filename):
    return os.path.join('card_photos', str(instance.id), filename)

class Card(models.Model):
    card_name = models.CharField(max_length=200)
    player_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    year = models.IntegerField(default=2015)
    condition = models.FloatField(default = 10.0)
    value = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    comments = models.CharField(max_length=2000, blank=True)
    rookie_card = models.BooleanField(default=False)
    auto = models.BooleanField(default=False)
    patch = models.BooleanField(default=False)
    double_auto = models.BooleanField(default=False)
    double_patch = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'card-photos', blank=True, null=True)
    acquired_date = models.DateTimeField('date acquired', default=timezone.now)
    card_pack = models.ForeignKey(CardPack, null=True)
    
    
    def __str__(self):
        return self.card_name
    
    def was_acquired_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_acquired_recently.admin_order_field = 'acquired_date'
    was_acquired_recently.boolean = True
    was_acquired_recently.short_description = 'acquired recently?'
    
