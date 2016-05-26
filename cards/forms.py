from django.forms import ModelForm

from cards.models import Card


class CardForm(ModelForm):

    class Meta:
        model = Card
        fields = '__all__'