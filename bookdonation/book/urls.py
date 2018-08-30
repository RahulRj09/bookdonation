from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.Home, name="home"),
    url(r'^mybook/$', views.Mybook, name='mybook'),
    url(r'^book/$', views.addbook, name='addnewbook'),
    #url(r'^userreq/$', views.userinfo, name='myuserinfo'),
    url(r'^bookk/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^account/logout/$', views.Logout),
]