from __future__ import unicode_literals
from django.db import models
from ..login.models import User

class ItemManager(models.Manager):
    def makeItem(self, postData, userID):
        result = { "valid" : True, "messages" : [] }

        #Validations
        if len(postData["name"]) == 0:
            messages.append("Must provide a name!")
        elif len(postData["name"]) < 4:
            messages.append("Name must be at least 4 characters long!")

        if len(result["messages"]) > 0:
            result["valid"] = False
        else:
            user = User.objects.get(id = userID)
            item = self.create(name = postData["name"], creator = user)
            print item.id
            user.wishlist.items.add(item)
            print user.wishlist.items.all()
            result["item"] = item

        return result

class Item(models.Model):
    name = models.CharField(max_length = 255)
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ItemManager()

class ListManager(models.Manager):
    pass

class List(models.Model):
    creator = models.OneToOneField(User, related_name = "wishlist")
    items = models.ManyToManyField(Item, related_name = "on_lists")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ListManager()
