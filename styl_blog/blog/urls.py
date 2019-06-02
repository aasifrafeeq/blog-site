from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.newblog,name='newblog'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/<str:heads>/',views.content,name='content'),
    path('done/',views.add,name='add')
]
