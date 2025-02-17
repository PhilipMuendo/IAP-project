from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),  
    path('event/add/', views.add_event, name='add_event'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),  
]
