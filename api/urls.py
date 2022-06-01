from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from api.views import create_user_view

from . import views
# from .views import api_home


urlpatterns = [
    path('auth/', obtain_auth_token),
    path('register/', create_user_view),
    # path('', views.api_home)  # localhost:8000/api/
    path('', views.product_list_create_view, name='product-list'),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view),
    path("rating/", views.rating_list_create_view),
]
