from django.contrib.auth.decorators import login_required
from django.urls import path
from users.views import UserLoginView, UserRegistrationView, UserProfileView, LogoutUserView, EmailConfirmationView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('email-confirmation/<str:email>/<uuid:code>/', EmailConfirmationView.as_view(), name='email-confirmation'),
]
