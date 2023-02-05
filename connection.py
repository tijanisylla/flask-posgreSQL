import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os


#  ========== DATABASE CONNECTION ==========
load_dotenv()
database_url = os.getenv("DATABASE_URL")

client = psycopg2.connect(database_url)
db = client.cursor(cursor_factory=psycopg2.extras.DictCursor)


#  ========== CREATE TABLE ==========
table_name = "todos"


def create_table():
    create_todo_query = """ 
    CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    db.execute(create_todo_query)
    client.commit()
    print("Table created successfully in PostgreSQL ")


#  ========== CHECK IF TABLE EXISTS ==========

def check_if_exists(table_name):
    try:
        db.execute("""
                    SELECT EXISTS (
                    SELECT 1 FROM information_schema.tables
                    WHERE table_catalog = 'flask-todo'
                    AND table_schema = 'public'
                    AND table_name = %s
                    );
                """, (table_name,))
        return db.fetchone()[0]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


print(f"Table {table_name} exists: {check_if_exists(table_name)}")

if check_if_exists(table_name) == False:
    create_table()
else:
    print("Table already exists")

print(f"Table {table_name} exists: {check_if_exists(table_name)}")
