from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from products.views import create_user_view

from . import views
# from .views import api_home


urlpatterns = [
    path('auth/', obtain_auth_token),
    path('register/', create_user_view),
    path('', views.api_home)  # localhost:8000/api/
]
