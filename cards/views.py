from django.views import generic
from django.utils import timezone
from django.shortcuts import render

from .forms import CardForm

from .models import Card

class BaseView(generic.ListView):
    template_name = 'cards/base.html'
    context_object_name = 'latest_card_list'
    def get_queryset(self):
        '''return the last five acquired cards.'''
        return Card.objects.filter(acquired_date__lte=timezone.now()).order_by('-acquired_date')[:5]


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

class CreateCardView(generic.FormView):
    template_name = 'cards/post_edit_card.html'
    form_class = CardForm
    success_url = '/cards/'
    
    def form_valid(self, form):
        form.save()
        return super(CreateCardView, self).form_valid(form)
    
    
    '''
    template_name = 'cards/post_edit_card.html'
    form_class = CardForm
    def form_valid(self, form):
        return super(CreateCardView, self).form_valid(form)
    '''


