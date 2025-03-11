# from .views import demo,remo,sumo,hi,hlo,Beast,Task1
from .views import UserCreateView,Duck,Goat,Beast
from django.urls import path

urlpatterns = [
    # path("demo/",demo,name='demo'),
    #  path('remo/', remo, name='remo'),
    # path("sumo/<int:id>",sumo),
    # path("hi/<str:firstname>/",hi),
    # path("hlo/",hlo,name='hlo'),
    path("post/",Beast.as_view()),
    # # path("get/<str:firstname>/",Master.as_view()),
    # path("task1/",Task1.as_view()),
    path("new/",UserCreateView.as_view()),
    path("duck/<int:pk>/",Duck.as_view()),
    path("goat/",Goat.as_view())
]