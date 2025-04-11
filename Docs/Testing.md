# Testing the API with Postman

This document explains how to test the FastAPI endpoints using Postman (or a similar tool like Insomnia).

---

## 1. Prerequisites

- **FastAPI Backend Running:**  
  Ensure your FastAPI application is up and running.  
  - If running locally, it might be at `http://localhost:8000`.  
  - If deployed, use the appropriate URL (e.g., `https://yourdomain.com`).

- **Postman Installed:**  
  Download and install [Postman](https://www.postman.com/downloads/) or use a similar API testing tool.

---

## 2. Endpoints

### 2.1. Login Endpoint

- **Method:** `POST`
- **URL:** `http://localhost:8000/api/auth/login`  
  *(Adjust the URL if running on a different host.)*

- **Request Body (JSON):**
  ```json
  {
    "username": "agent.coulson",
    "password": "password123"
  }
  ```
#### Expected Success Response:
```json
  {
    "message": "Login successful"
  }

```
#### Response on failure:
```json
  {
    "detail": "Invalid credentials"
  }
```
### 2.2. Create Mission Endpoint

- **Method:** `POST`
- **URL:** `http://localhost:8000/api/missions`  
  *(Adjust the URL if running on a different host.)*
- **Request Body (JSON):**
  ```json
  {
  "agent_id": "agent.pepper",
  "mission": "Set Up Secure Communications Relay",
  "details": {
    "relay_id": "relay-42",
    "channel": "Encrypted Channel Alpha",
    "encryption_protocol": "AES-256"
    }
  }

  ```
  
#### Expected Success Response:
```json
  {
  "message": "Mission created",
  "id": "<new_mission_id>"
}

```
#### If an error occurs (e.g., a database issue), expect a 500 Internal Server Error with an error message.
### 2.3. Get Missions Endpoint

- **Method:** `GET`
- **URL:** `http://localhost:8000/api/missions`  
  *(Adjust the URL if running on a different host.)*
#### Expected Success Response:
```json
  {
  "missions": [
    {
      "_id": "6457ab3d...etc",
      "agent_id": "agent.may",
      "mission": "Sync Classified Intelligence Database",
      "details": {
        "database_name": "classified_intel",
        "sync_frequency": "daily",
        "transmission_channel": "Secure Fiber Link"
      }
    },
    ...
  ]
}
```

#### If an error occurs (e.g., a retrieval issue), expect a 500 Internal Server Error.
