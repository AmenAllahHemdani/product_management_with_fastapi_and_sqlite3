
# Product management with Fastapi and Sqlite3

This project is a simple FastAPI application demonstrating how to build a RESTful API for managing items, featuring structured routing, SQLite database integration, and robust error handling.

## 🚀 Features

  * **FastAPI Framework:** Leverage the speed and simplicity of FastAPI for API development.
  * **SQLite Database:** Uses a local `.db` file for data storage, perfect for development and small-scale applications.
  * **Structured Routing:** Organizes API endpoints into separate router files for better maintainability.
  * **Dependency Injection:** Manages database connections efficiently using FastAPI's dependency injection system.
  * **CRUD Operations (Create & Read/Filter):**
      * **Create Item:** Add new items to the database with validation and conflict handling.
      * **Get/Filter Items:** Retrieve all items or filter them based on various criteria (name, description, price, tax).
  * **Pydantic Models:** Ensures robust data validation and serialization for API requests and responses.
  * **Comprehensive Error Handling:** Provides clear HTTP error responses (e.g., 409 Conflict, 500 Internal Server Error) for common issues.
  * **Interactive API Docs:** Automatic generation of OpenAPI (Swagger UI) documentation at `/docs`.

## 📂 Project Structure

```
my_fastapi_app/
├── models               # Products type creation
├── src/router           # Defines API routes
├── database.py          # Handles SQLite database connection, table creation, and dependency
├── main.py              # Main FastAPI application entry point
├── products.db          # SQLite database file
```

## 🛠️ Setup and Installation

Follow these steps to get the project up and running on your local machine.

1.  **Clone the repository (if applicable):**

    ```bash
    git clone https://github.com/AmenAllahHemdani/product_management_with_fastapi_and_sqlite3.git
    ```

    (If you manually created the files, just navigate to your project directory.)

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install fastapi uvicorn "pydantic>=1.8,<2"
    ```

    *(Note: If you're using a newer version of Pydantic (v2+), you can simply use `pip install fastapi uvicorn pydantic`)*

## 🚀 Running the Application

Once you have installed the dependencies, you can run the FastAPI application:

```bash
python main.py
```

  * The `--reload` flag is useful during development as it automatically restarts the server when you make changes to the code.
  * The application will typically run on `http://127.0.0.1:8000`.

## 📖 API Documentation

After starting the server, you can access the interactive API documentation (Swagger UI) at:

[http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)

This interface allows you to test the API endpoints directly from your browser.

## ⚡ API Endpoints

### Items (`/items`)

All item-related endpoints are grouped under the `/items` prefix.

  * **`POST /items/` - Create a New Item**

      * **Description:** Adds a new product item to the database.
      * **Request Body (JSON):**
        ```json
        {
          "id": 1,
          "name": "Tuf Gaming",
          "description": "Laptop gaming",
          "price": 2000,
          "tax": 10
        }
        ```
      * **Responses:**
          * `201 Created`: Item successfully added.
          * `409 Conflict`: An item with the given ID already exists.
          * `422 Unprocessable Entity`: Invalid input data (Pydantic validation error).
          * `500 Internal Server Error`: An unexpected server-side or database error occurred.

-----
