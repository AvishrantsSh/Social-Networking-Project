from django.urls import path

from backend.views import HomeView, LoginView, LogoutView

urlpatterns = [
    path("", HomeView, name="home"),
    path("login", LoginView, name="login"),
    path("logout", LogoutView, name="logout"),
]
