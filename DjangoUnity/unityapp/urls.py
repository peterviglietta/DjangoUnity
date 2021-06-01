from django.conf.urls import url

from . import views

app_name = 'unityapp'

urlpatterns = [
    # ex: /unityapp/
    url(r'^$', views.Quirklist, name='index'),
]

#This was the URLconf you used to just load the 
#GetPatient call into a blank webpage at localhost:8000/unityappp
"""
urlpatterns = [
    # ex: /unityapp/
    url(r'^$', views.falcon, name='index'),
]
"""
