from django.shortcuts import render, redirect
from .models import List, Item
from ..login.models import User

def index(request):
    loggedInUser = User.objects.get(id = request.session["user_id"])
    print loggedInUser.wishlist.items.all()
    context = {
        "user" : loggedInUser,
        "myList" : loggedInUser.wishlist.items.all(),
        "otherList" : Item.objects.all().exclude(creator = loggedInUser)
    }
    return render(request, "wishlist/index.html", context)

def createPage(request):
    return render(request, "wishlist/create.html")

def makeItem(request):
    result = Item.objects.makeItem(request.POST, request.session["user_id"])
    if result["valid"]:
        return redirect("Wishlist:View", result["item"].id)
    else:
        for message in messages:
            messages.error(request, message)
        return redirect("Wishlist:Create")

def destroyItem(request):
    item = Item.objects.get(id = request.POST["item_id"])
    item.delete()
    return redirect("Wishlist:Index")

def viewItem(request, id):
    context = {
        "item" : Item.objects.get(id = id),
        "listed_by" : Item.objects.get(id = id).on_lists.all()
    }
    return render(request, "wishlist/listing.html", context)

def addToList(request):
    User.objects.get(id = request.session["user_id"]).wishlist.items.add(Item.objects.get(id = request.POST["item_id"]))
    return redirect("Wishlist:Index")

def removeFromList(request):
    User.objects.get(id = request.session["user_id"]).wishlist.items.remove(Item.objects.get(id = request.POST["item_id"]))
    return redirect("Wishlist:Index")
