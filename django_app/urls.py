# urls.py

from django.urls import path
from .views import signup_view, login_view,home_view,hello_user_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'), 
    path('hello_user/<str:username>/', hello_user_view, name='hello_user'),
    # Add other URLs as needed
]
