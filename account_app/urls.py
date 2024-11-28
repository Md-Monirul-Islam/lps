from django.urls import path
from .views import login, SignupView, UserProfileView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', login, name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
