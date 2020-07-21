from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('maintenance', views.maintenanceBoard, name='maintenance'),
    path('maintenance_plus', views.saveAgain, name='save_again')
]
