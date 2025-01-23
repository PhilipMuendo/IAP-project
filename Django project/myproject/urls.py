from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.event_list, name='event_list'),  
    path('event/<int:id>/', views.event_detail, name='event_detail'), 
    path('create/', views.create_event, name='create_event'),  
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
