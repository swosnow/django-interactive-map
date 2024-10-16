from django.urls import path
from . import views

app_name = 'mapaguapi'

urlpatterns = [
    
    path('', views.home, name='home'),
    path('problems/<int:id>', views.problem, name='problems'),
    path('map_view/', views.map_view, name='map_view'),
]