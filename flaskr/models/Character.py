import json

from jsonschema import validate

from .. import redis_client
from ..config import schema


class Character:
    def __init__(self, name, last_name, age):

        self.name = name
        self.last_name = last_name
        self.age = age

    def save(self):
        doc = self.__dict__

        try:
            validate(instance=doc, schema=schema)
        except Exception as e:
            return {"code": 422, "msg": e.message}

        if redis_client.get(self.name):
            return {"code": 409, "msg": "conflict"}

        redis_client.set(self.name, json.dumps(doc))
        redis_client.bgsave()

        return doc
