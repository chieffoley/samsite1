from django.views import generic
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.shortcuts import render

from .forms import CardForm

from .models import Card
from .models import CardTable
from django_tables2 import SingleTableView

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

class DbShowView(SingleTableView):
    model = Card
    template_name = 'cards/db_show.html'
    table_class = CardTable
    #context_object_name = 'card_list'
    
''' def get_context_data(self, **kwargs):
        context = super(DbShowView, self).get_context_data(**kwargs)
        context['table'] = CardTable(Card.objects.all().order_by('player_name'))

    def get_queryset(self):
        return Card.objects.all().order_by('player_name')
'''
    
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
    
class UpdateCardView(generic.UpdateView):
    model = Card
    #form_class = UpdateCardForm
    fields =    ['card_pack',
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
                ]
    template_name_suffix = '_update_form'
    success_url = '/cards/'
    
    def form_valid(self, form):
        form.save()
        return super(UpdateCardView, self).form_valid(form)
    
class DeleteCardView(DeleteView):
    model = Card
    success_url = '/cards/'
    
    
    '''
    template_name = 'cards/post_edit_card.html'
    form_class = CardForm
    def form_valid(self, form):
        return super(CreateCardView, self).form_valid(form)
    '''


