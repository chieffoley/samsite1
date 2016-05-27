from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.IndexView.as_view(), name='index'),
    #ex /cards/5
   url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
   url(r'^base$', views.BaseView.as_view(), name='base')
]