from django.urls import path
from . import views

app_name = 'mapaguapi'

urlpatterns = [
    
    path('', views.map_view, name='map_view'),
    path('problems/<int:id>', views.problem, name='problems'),
    path('home/', views.home, name='home'),
]