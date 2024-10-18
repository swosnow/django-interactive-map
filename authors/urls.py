from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/problem/new/', views.dashboard_problem_new, name='dashboard_problem_new'),
    path('dashboard/problem/<int:id/delete/', views.dashboard_problem_delete, name='dashboard_problem_delete'),
    path(
        'dashboard/problem/<int:id>/edit/',
        views.DashboardProblem.as_view(),
        name='dashboard_problem_edit'
    ),

]
