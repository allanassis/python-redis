from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/')
def todo():
    return 'todo-list'

