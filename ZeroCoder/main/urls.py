from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('lev', views.lev,name='leverage'),
    path('down', views.down,name='downside'),
    path('new', views.new,name='page2'),

]