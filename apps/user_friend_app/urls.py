
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^showall$', views.showall),
    url(r'^currentfriend$', views.currentfriend),    
    url(r'^makefriend$', views.makefriend),
    url(r'^clear$',views.clear),
    url(r'^goHome$', views.goHome),

    ]
