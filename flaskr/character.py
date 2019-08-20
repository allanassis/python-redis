from flask import Blueprint, request

from .models.character import Character

bp = Blueprint("character", __name__, url_prefix="/character")


@bp.route("/")
def character_list():
    """
        Get list
    """
   # keys = [item.decode() for item in Character.get_all()]
    return { "data": Character.get_all()}
    #return "character-list"


@bp.route("/", methods=["POST"])
def character_post():
    """
        Add a new item
    """
    data = request.json
    c = Character(
            name=data.get("name", None),
            last_name=data.get("last_name", ""),
            age=data.get("age", 0)
            )
    return c.save()


@bp.route("/<key>", methods=["PUT"])
def character_put(key):
    """
        Update an item
    """
    data = request.json
    char = Character.get(key)
    if type(char) != str:
        char.name = data.get("name", None)
        char.last_name = data.get("last_name","")
        char.age = data.get("age",0)
        return  char.save(update=True)

    return char


@bp.route("/<key>", methods=["DELETE"])
def character_delete(key):
    """
        Update an item
    """

    data = request.json
    data["key"] = key
    return data
