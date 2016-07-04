from django.forms import ModelForm

from cards.models import Card
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

class CardForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset (
                    'CardInfo',
                    'card_pack',
                    'player_name',
                    'team',
                    'year',
                    'condition',
                    'value',
                    'rookie_card',
                    'auto',
                    'patch',
                    'double_auto',
                    'double_patch',
                    'image',
                    'comments',
                    'card_name',
                    'acquired_date',
                    ),
                )
        

    class Meta:
        model = Card
        fields = '__all__'
        
        
class UpdateCardForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset (
                    'CardInfo',
                    'card_pack',
                    'player_name',
                    'team',
                    'year',
                    'condition',
                    'value',
                    'rookie_card',
                    'auto',
                    'patch',
                    'double_auto',
                    'double_patch',
                    'image',
                    'comments',
                    'card_name',
                    'acquired_date',
                    ),
                )
        

    class Meta:
        model = Card
        fields = '__all__'
        
        


    