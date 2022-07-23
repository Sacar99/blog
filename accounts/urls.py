from .views import SignUpView
from django.urls import path, include

urlpatterns = [
    path("accounts/", SignUpView.as_view(), name="signup"),
]