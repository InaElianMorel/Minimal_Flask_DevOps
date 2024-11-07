from app.models.models import TodoList
from flask import jsonify, request
import json
from app import db
from app.views import views_bp as bp


def todo_serializer(todo):
    # convert data from TodoList to JSON
    return {"id": todo.id, "todo": todo.todo}


@bp.route("/", methods=["GET"])
def home():
    return jsonify([*map(todo_serializer, TodoList.query.all())])


@bp.route("/todo-create", methods=["POST"])
def todo_create():
    # add todo to database
    request_data = json.loads(request.data)
    todo = TodoList(todo=request_data["todo"])

    db.session.add(todo)
    db.session.commit()

    return {"201": "todo created successfully"}


@bp.route("/update/<int:id>", methods=["PUT"])
def update_todo(id):
    item = TodoList.query.get(id)
    request.get_json(force=True)
    todo = request.json["todo"]
    item.todo = todo
    db.session.commit()

    return {"200": "Updated successfully"}


@bp.route("/<int:id>", methods=["POST"])
def delete_todo(id):

    request.get_json(force=True)
    request_data = json.loads(request.data)

    TodoList.query.filter_by(id=request_data["id"]).delete()
    db.session.commit()
    return {"204": "Delete successfully"}
