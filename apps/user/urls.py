from django.urls import path
from .views import UsersView, CreateUserView, HomeView, UpdateUserView

urlpatterns = [
    path('users-json/', HomeView.as_view(), name='users-json'),
    path('users/', UsersView.as_view(), name='users'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('update-user/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
]