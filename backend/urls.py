from django.urls import path

from backend.views.registration import LoginView, LogoutView, SignUpView
from backend.views.main import AddPostView, HomeView

urlpatterns = [
    path("", HomeView, name="home"),
    path("login", LoginView, name="login"),
    path("signup", SignUpView, name="signup"),
    path("logout", LogoutView, name="logout"),
    path("add_post", AddPostView, name="add_post"),
]
