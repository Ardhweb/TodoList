from django.contrib import admin
from django.urls import path


from .views import index,add,deleteView
from todoapp import views


urlpatterns = [
    path('',views.index,name="index"),
    path('add/',add),
    path(r'delete/<int:i>/', deleteView),   # here r' is for record in database  and int:i for objects id int for digit and i for id
    #url(r'^delete/(?P<i>\d+)/$', deleteView),

    
]
