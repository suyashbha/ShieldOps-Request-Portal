# Front-End Project Overview

This document provides an overview of the front-end implementation using Appsmith, along with instructions for setting it up and testing it locally.

---

## 1. Project Structure

- **frontend/appsmith_export.json**  
  - **Purpose:**  
    - This is the exported Appsmith application file containing the complete front-end configuration.  
    - It includes all widgets, data sources, and queries configured for the mission management and user authentication interfaces.
    
- **Documentation Files:**  
  - This document (frontend.md) explains how to import and configure the front-end application.

---

## 2. Setting Up the Front-End

### a. Requirements

- An Appsmith account (you can use the cloud version at [app.appsmith.com](https://app.appsmith.com/) or host Appsmith locally via Docker).
- Access to the exported JSON file (`appsmith_export.json`) provided in the `frontend/` folder of this repository.
- The FastAPI backend must be running (online or locally) and accessible via its API endpoints.

### b. Importing the Application

1. **Log in to Appsmith:**  
   Open your Appsmith instance (cloud or local).

2. **Import the Application:**  
   - In the Appsmith dashboard, click on **"Create New"** → **"Import Application"**.
   - Upload the `frontend/appsmith_export.json` file from the repository.
   - The application will be imported, and you can open it in edit mode.

3. **Configure API Endpoints:**  
   - Open the imported application in the Appsmith editor.
   - Locate the data sources and queries that connect to the backend (though, I have already connected my backend api, so it can be used directly also, and you can move to step 3 directly).
   - Update the API endpoint URLs to point to your FastAPI backend URL. For example, if your backend is running locally, change the endpoints to:  
     `http://localhost:8000/api/...`  
     Otherwise, use the appropriate online URL.
   - Save your changes.

---

## 3. Using and Testing the Front-End

- **Deploy the Application:**  
  After importing and configuring the API endpoints, deploy (publish) the application from Appsmith.

- **Interact with the UI:**  
  - Test functionalities such as mission creation, user login, and mission retrieval.
  - The application should send REST API calls to the FastAPI backend.
  - Verify that data is correctly saved and retrieved, and that error handling (e.g., form validation) works as expected.

- **Monitoring:**  
  Check the FastAPI backend logs to confirm that API calls from the front-end are processed as expected.

---

This document should provide you with all the necessary details to set up, import, and test the front-end component of the project. Enjoy testing the application!
