from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.IndexView.as_view(), name='index'),
    #ex /cards/5
   url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
   url(r'^base$/', views.BaseView.as_view(), name='base'),
   url(r'^create/$', views.CreateCardView.as_view(), name='post_new_card'),
   url(r'^update/(?P<pk>[0-9]+)/$', views.UpdateCardView.as_view(), name='card_update_form'),
   url(r'^delete/$', views.DeleteCardView.as_view(), name='delete_card'),
   url(r'^db_show/$', views.DbShowView.as_view(), name='db_show'),
]