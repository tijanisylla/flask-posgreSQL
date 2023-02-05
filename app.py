from flask import Flask, jsonify, request
from models import create_todo, get_todos, get_todo_by_id, update_todo_by_id, delete_todo_by_id, search_todos

app = Flask(__name__)


def format_todo(todos):
    return [{
        'id': todo['id'],
        'title': todo['title'],
        'description': todo['description'],
        'date': todo['date']
    } for todo in todos]


@app.route('/todos', methods=['GET'])
def get_todos_route():
    todos = get_todos()
    new_todo = format_todo(todos)
    return jsonify(new_todo), 200


@app.route('/todos', methods=['POST'])
def create_todo_route():
    data = request.get_json()
    title = data['title']
    description = data['description']
    create_todo(title, description)
    return jsonify({'message': 'Todo created successfully'}), 201


@app.route('/todos/<int:id>', methods=['GET'])
def get_todo_route(id):
    todo = get_todo_by_id(id)
    new_todo = format_todo([todo])
    return jsonify(new_todo), 200


@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo_route(id):
    data = request.get_json()
    title = data['title']
    description = data['description']
    update_todo_by_id(id, title, description)
    return jsonify({'message': 'Todo updated successfully'}), 200


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo_route(id):
    delete_todo_by_id(id)
    return jsonify({'message': 'Todo deleted successfully'}), 200


@app.route('/todos/search/<search>', methods=['GET'])
def search_todo_route(search):
    todos = search_todos(search)
    new_todo = format_todo(todos)
    return jsonify(new_todo), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
