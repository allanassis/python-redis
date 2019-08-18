from flask import Blueprint, request

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/")
def todo_list():
    """
        Get list
    """
    return "todo-list"


@bp.route("/", methods=["POST"])
def todo_post():
    """
        Add a new item
    """
    data = request.json
    return data


@bp.route("/<key>", methods=["PUT"])
def todo_put(key):
    """
        Update an item
    """
    data = request.json
    data["key"] = key
    return data


@bp.route("/<key>", methods=["DELETE"])
def todo_delete(key):
    """
        Update an item
    """

    data = request.json
    data["key"] = key
    return data
