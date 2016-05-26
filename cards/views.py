from django.views import generic
from django.utils import timezone

from .models import Card

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_card_list'
    
    def get_queryset(self):
        '''return the last five acquired cards.'''
        return Card.objects.filter(acquired_date__lte=timezone.now()).order_by('-acquired_date')[:5]

class DetailView(generic.DetailView):
    model = Card
    template_name = 'cards/detail.html'
    
    def get_queryset(self):
        return Card.objects.filter(acquired_date__lte=timezone.now())

