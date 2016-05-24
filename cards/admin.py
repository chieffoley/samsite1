from django.contrib import admin

# Register your models here.
from .models import Card,CardPack

admin.site.register(Card)
admin.site.register(CardPack)