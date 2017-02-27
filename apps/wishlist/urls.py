from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^dashboard$", views.index, name = "Index"),
    url(r"^wish_items/create$", views.createPage, name = "Create"),
    url(r"^wish_items/additem$", views.makeItem, name = "MakeItem"),
    url(r"^wish_items/destroyitem$", views.destroyItem, name = "DestroyItem"),
    url(r"^wish_items/(?P<id>\d*)$", views.viewItem, name = "View"),
    url(r"^addtolist$", views.addToList, name = "AddToList"),
    url(r"^removefromlist$", views.removeFromList, name = "RemoveFromList")
]
