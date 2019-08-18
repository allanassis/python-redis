from .. import redis_client
import json


class Character:
    def __init__(self, name, last_name, age):

        self.name = name
        self.last_name = last_name
        self.age = age

    def save(self):
        doc = self.__dict__

        if redis_client.get(self.name):
            return {"code": 409, "msg": "conflict"}

        redis_client.set(self.name, json.dumps(doc))
        return doc
