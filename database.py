import sqlite3
import os

DATABASE_FILE = 'products.db' 

def connect_db(db_file=DATABASE_FILE):
    """Establishes a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        print(f"Connected to database: {db_file}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn, query:str):
    """Creates a table if it doesn't already exist."""
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit() 
        print("Table 'product' created or already exists.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def cleanup_database():
    if os.path.exists(DATABASE_FILE):
        os.remove(DATABASE_FILE)
        print(f"Removed existing database file: {DATABASE_FILE}")

if not os.path.exists(DATABASE_FILE):
    print(f"Creating new database file: {DATABASE_FILE}")
    _conn_init = get_db_connection()
    if _conn_init:
        create_product_table(_conn_init)
        _conn_init.close()
        _conn_init = None
    else:
        print("Could not create initial database file.")

conn = connect_db()


# if __name__ == "__main__":
#     if os.path.exists(DATABASE_FILE):
#         os.remove(DATABASE_FILE)
#         print(f"Removed existing database file: {DATABASE_FILE}")
#     conn = connect_db()
#     if conn:
#         try:
#             # 2. Create table
#             query = '''
#             CREATE TABLE IF NOT EXISTS product (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 description TEXT NOT NULL,
#                 price INTEGER,
#                 tax INTEGER
#             )
#             '''
#             create_table(conn, query)
#         finally:
#             # Close the connection when done
#             conn.close()
#             print("\nDatabase connection closed.")
