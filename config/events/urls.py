from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.register_event, name='register_event_home'),
    path('register/', views.register_event, name='register_event'),
]
