# Backend Project Structure

This document describes the purpose of the key files in the backend project.

## Files and Their Purposes

- **main.py**  
  - **Purpose:**  
    - Acts as the entry point for the FastAPI application.
    - Configures and initializes the application.
    - Sets up middleware (e.g., CORS) and includes the API routes from `routes.py`.
  - **Key Functions:**  
    - Starts the FastAPI server.
    - Provides a root endpoint (e.g., `/`) to confirm that the API is running.

- **routes.py**  
  - **Purpose:**  
    - Contains the API endpoints for the application.
    - Handles user authentication (e.g., `/auth/login`) and mission operations (creation via POST and retrieval via GET).
    - Uses dependency injection to obtain fresh database connections for each request.
  - **Key Endpoints:**  
    - `/auth/login` – Validates user credentials.
    - `/missions` (POST) – Inserts a new mission into the MongoDB collection.
    - `/missions` (GET) – Retrieves missions from the MongoDB collection.

- **database.py**  
  - **Purpose:**  
    - Manages the MongoDB connection for the application.
    - Provides the `get_db_client()` function that creates and returns a fresh MongoDB client and database instance.
  - **Key Functions:**  
    - `get_db_client()` – Establishes a connection to MongoDB using Motor and returns the database object.

- **models.py**  
  - **Purpose:**  
    - Defines the data models used in the application using Pydantic.
    - Provides validation for incoming request data, ensuring that required fields are provided and adhere to expected formats.
  - **Key Models:**  
    - `Mission` – Represents a mission with fields such as `agent_id`, `mission`, and `mission details`.
    - `User` – Represents a user with fields like `username` and `password`.

- **add_users.py**  
  - **Purpose:**  
    - A standalone script to seed the database with sample user data.
    - Inserts sample users (e.g., "agent.coulson", "agent.pepper", "agent.may") into the `users` collection if they do not already exist.
  - **Usage:**  
    - Run the script manually (e.g., using `python add_users.py`) to populate the database with initial user accounts.

- **requirements.txt**  
  - **Purpose:**  
    - Lists all the Python dependencies required to run the backend project.
    - Ensures that anyone setting up the project can install the necessary packages (e.g., FastAPI, Uvicorn, Motor, Passlib, etc.) by running:
      ```bash
      pip install -r requirements.txt
      ```
