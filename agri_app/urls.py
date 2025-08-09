from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('schemes/', views.schemes, name='schemes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('feedback/', views.feedback_submit, name='feedback'),
    path('disease-scan/', views.disease_scan, name='disease_scan'),
]
