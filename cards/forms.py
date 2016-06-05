from django.forms import ModelForm

from cards.models import Card
from crispy_forms.helper import FormHelper

class CardForm(ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Card
        fields = '__all__'