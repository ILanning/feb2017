from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from ..wishlist.models import List

def redir(request):
    if "user_id" in request.session:
        return redirect("Wishlist:Index")
    return redirect("Login:Index")

def index(request): #GET
    return render(request, "login/register.html")

def register(request): #POST
    result = User.objects.addUser(request.POST)

    if not result["valid"]:
        for message in result["messages"]:
            messages.error(request, message)
        return redirect("Login:Index")
    else:
        result["user"].wishlist = List.objects.create(creator = result["user"])
        request.session["user_id"] = result["user"].id
        return redirect("Wishlist:Index")

def login(request): #POST
    result = User.objects.login(request.POST)

    if not result["valid"]:
        for message in result["messages"]:
            messages.error(request, message)
        return redirect("Login:Index")
    else:
        request.session["user_id"] = result["user"].id
        return redirect("Wishlist:Index")

def logout(request): #Either
    if "user_id" in request.session:
        request.session.pop("user_id")
    return redirect("Login:Index")

# Create your views here.
