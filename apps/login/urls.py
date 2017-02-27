from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.redir, name = "Front"),
    url(r"^main$", views.index, name = "Index"),
    url(r"^users/register$", views.register, name = "Register"),
    url(r"^users/login$", views.login, name = "Login"),
    url(r"^users/logout$", views.logout, name = "Logout")
]
