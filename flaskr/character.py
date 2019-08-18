from flask import Blueprint, request
from .models.character import Character
from .config import REDIS_URL

bp = Blueprint("character", __name__, url_prefix="/character")


@bp.route("/")
def character_list():
    """
        Get list
    """
    return "character-list"


@bp.route("/", methods=["POST"])
def character_post():
    """
        Add a new item
    """
    c = Character(name="allan", last_name="assis", age=23)
    # data = request.json
    return c.save()


@bp.route("/<key>", methods=["PUT"])
def character_put(key):
    """
        Update an item
    """
    data = request.json
    data["key"] = key
    return data


@bp.route("/<key>", methods=["DELETE"])
def character_delete(key):
    """
        Update an item
    """

    data = request.json
    data["key"] = key
    return data
