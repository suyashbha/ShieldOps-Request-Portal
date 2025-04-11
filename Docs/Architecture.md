# Architecture Diagram and Ingestion Process

This document outlines the high-level system architecture and explains the data ingestion processes for the application.

---

## 1. System Architecture

The project consists of three primary components:

- **User Interface (Appsmith):**  
  A low-code front-end application that provides forms for user authentication and mission management.  
- **FastAPI Backend:**  
  A RESTful API server built with FastAPI that handles requests, performs validation, and communicates with the database.  
- **MongoDB Database:**  
  A NoSQL database used to store mission data and user information.

## 2. Ingestion Process

### Mission Creation Flow

#### User Action (Front-End)
- A user fills out the mission creation form on the Appsmith UI.  
- The form captures required fields such as **title**, **description**, and **location**.

#### API Request
- On submission, the Appsmith front-end sends a **POST** request to the FastAPI endpoint `/api/missions` with the mission details in JSON format.

#### Backend Processing
- FastAPI receives the request and validates the input using a **Pydantic model**.  
- If validation passes, the mission data is inserted into the **missions** collection in MongoDB.  
- A success response (including the new mission ID) is sent back to the client.  
- In case of errors (e.g., empty fields, database issues), an appropriate **HTTP error** response is returned.

#### Response and UI Update
- The Appsmith UI displays a success message and updates the mission list, or shows an error message if something went wrong.  
- The backend logs record the API call and the outcome.

### User Authentication Flow

#### User Action (Front-End)
- A user enters their login credentials on the Appsmith login form.

#### API Request
- The front-end sends a **POST** request to `/api/auth/login` with the username and password in JSON format.

#### Backend Processing
- FastAPI searches for the user in the **users** collection.  
- The provided password is verified against the stored **bcrypt** hash.  
- If the credentials are correct, a success message is returned; otherwise, an error message is sent back.

#### Session Management
- For this assignment, session handling is basic.  

---

## 3. Security and Performance Considerations

### Security
- Passwords are **hashed using bcrypt** to prevent plain-text storage.  
- Environment variables secure sensitive configurations (e.g., database connection strings).  
- **CORS policies** are applied in the FastAPI backend to control access.

### Performance
- FastAPI’s **asynchronous** nature allows handling multiple requests concurrently.  
- **MongoDB connection pooling** (via Motor) is used in production to optimize database access.  
- The architecture is designed for **scalability**, with the possibility to deploy components independently.
