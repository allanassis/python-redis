import json

from jsonschema import validate

from .. import redis_client
from ..config import schema


class Character:
    def __init__(self, name, last_name, age):

        self.name = name
        self.last_name = last_name
        self.age = age

    def save(self, update=False):
        doc = self.__dict__

        try:
            validate(instance=doc, schema=schema)
        except Exception as e:
            return {"code": 422, "msg": e.message}

        if redis_client.get(self.name) and not update:
            return {"code": 409, "msg": "conflict"}

        redis_client.set(self.name, json.dumps(doc))
        redis_client.bgsave()

        return doc

    def delete(self):
        return redis_client.delete(self.name)

    @staticmethod
    def get(name):
        doc = json.loads(redis_client.get(name))
        if doc:
            char = Character(
                name=doc["name"], last_name=doc["last_name"], age=doc["age"]
            )
            return char
        return "not found"

    @staticmethod
    def get_all():
        keys = [key.decode() for key in redis_client.keys("*")]
        char_list = []
        for key in keys:
            char_list.append(json.loads(redis_client.get(key)))
        return char_list
