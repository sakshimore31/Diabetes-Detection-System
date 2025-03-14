from django.urls import path
from .views import home,register, login, predict, logout, result,display_csv

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('predict/', predict, name='predict'),
    path('result/', result, name='result'),
    path('display_csv/', display_csv, name='display_csv'),
    path('logout/', logout, name='logout'),
]
