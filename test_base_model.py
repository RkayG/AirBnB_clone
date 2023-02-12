#!/usr/bin/python3
from models.base_model import BaseModel

model_dict = {'id': '2e3b95f2-703d-4291-ae8f-d2d5f358f58c', 'created_at': '2023-02-10T14:56:39.652609',
              'updated_at': '2023-02-10T14:56:39.652609', '__class__': 'BaseModel'}
my_model = BaseModel(**model_dict)
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

