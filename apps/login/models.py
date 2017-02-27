from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def addUser(self, postData):
        result = { "valid" : True, "messages" : [] }
        messages = result["messages"]

        #Validations
        if len(postData["name"]) == 0:
            messages.append("Must provide a name!")
        elif len(postData["name"]) < 3:
            messages.append("Name is not long enough!")

        if len(postData["username"]) == 0:
            messages.append("Must provide a username!")
        elif len(postData["username"]) < 3:
            messages.append("Username is not long enough!")

        if len(postData["password"]) == 0:
            messages.append("Must provide a password!")
        elif len(postData["password"]) < 8:
            messages.append("Password must be at least 8 characters long!")
        elif postData["passconf"] != postData["password"]:
            messages.append("Password and confirmation must match!")

        if len(result["messages"]) > 0:
            result["valid"] = False
        else:
            user = self.create(name = postData["name"], username = postData["username"], password = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt()))
            result["user"] = user

        return result

    def login(self, postData):
        result = { "valid" : True, "messages" : [] }
        messages = result["messages"]
        user = None

        #Validations
        if len(postData["username"]) == 0:
            messages.append("Must provide a username!")
        else:
            user = self.filter(username = postData["username"])
            if len(user) == 0:
                messages.append("User by that name does not exist!")
            else:
                user = user[0]
                if user.password != bcrypt.hashpw(postData["password"].encode(), user.password.encode()):
                    messages.append("Password incorrect!")

        if len(result["messages"]) > 0:
            result["valid"] = False
        else:
            result["user"] = user

        return result

class User(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
