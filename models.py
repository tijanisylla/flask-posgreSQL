from connection import db, client
import psycopg2


# Get all todos
def get_todos():
    try:
        db.execute("SELECT * FROM todos ORDER BY id ASC")
        print("Got all todos successfully")
        return db.fetchall()  # [] or [{}, {}, {}]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

# Create a todo


def create_todo(title, description):
    try:
        db.execute(
            "INSERT INTO todos (title, description) VALUES (%s, %s)", (title, description))
        client.commit()
        print("Created todo successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  get a todo by id
def get_todo_by_id(id):
    try:
        db.execute("SELECT * FROM todos WHERE id = %s", (id,))
        print("Got todo by id successfully")
        return db.fetchone()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  update a todo
def update_todo_by_id(id, title, description):
    try:
        db.execute(
            "UPDATE todos SET title = %s, description = %s WHERE id = %s", (title, description, id))
        client.commit()
        print("Updated todo by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  delete a todo
def delete_todo_by_id(id):
    try:
        db.execute("DELETE FROM todos WHERE id = %s", (id,))
        client.commit()
        print("Deleted todo by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  Search for a todo
def search_todos(search):
    try:
        db.execute(
            "SELECT * FROM todos WHERE title LIKE %s OR description LIKE %s", (search, search))
        print("Searched for a todo successfully")
        return db.fetchall()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False
