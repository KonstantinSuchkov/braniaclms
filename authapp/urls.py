from authapp.apps import AuthappConfig
from django.urls import path
from authapp.views import CustomLoginView, RegisterView, CustomLogoutView, EditView

app_name = AuthappConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit/', EditView.as_view(), name='edit'),
]