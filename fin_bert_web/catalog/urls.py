from django.urls import path
from . import views


urlpatterns = [
    path('', views.report, name='report')
    #path('report', views.report, name='report')
]



