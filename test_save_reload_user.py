#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.amenity import Amenity

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = Place()
my_user.city_id = "Bogota"
my_user.user_id = "id_bogota"
my_user.name = "name_bogota"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = Amenity ()
my_user2.name = "amenity_name"
my_user2.save()
print(my_user2)
