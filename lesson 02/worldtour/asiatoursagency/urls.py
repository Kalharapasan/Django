from django.urls import path
from . import views

#Define list of url patterns
urlpatterns = [
    path("",views.index)
]
