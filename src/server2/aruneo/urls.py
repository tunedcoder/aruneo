from django.urls import path
from . import views

#urls
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('res/', views.res_dash, name='resident'),
    path('soc/', views.soc_dash, name='society'),
    path('data/', views.data_enter, name='data'),
]