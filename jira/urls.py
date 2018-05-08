
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^saveToFile', views.saveToFile , name='saveToFile'),
	url(r'^trainBot', views.trainBot , name='trainBot'),
	url(r'^runJiraUtil', views.runJiraUtil , name='runJiraUtil'),
]
