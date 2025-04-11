# Shield Ops Request Portal

## Overview
The Shield Ops Request Portal is a web-based application designed for S.H.I.E.L.D. agents to submit mission requests efficiently. This project was built as part of a technical exercise to create a full-stack solution with a secure login, dynamic mission request forms, and data persistence, following the assignment requirements.

## Features
- **Secure Login Page:** Provides a basic authentication system for agents using sample credentials (e.g., `agent.coulson`).
- **Dynamic Mission Request List:** Displays a list of available mission requests fetched from the backend API.
- **Custom Mission Request Forms:** Presents tailored forms based on selected mission requests:
  - **Deploy Drone Surveillance Unit:** Collects Drone ID, Operation Area, and Payload.
  - **Set Up Secure Communications Relay:** Collects Relay ID, Communication Channel, and Encryption Protocol.
  - **Sync Classified Intelligence Database:** Collects Database Name, Sync Frequency, and Transmission Channel.
- **Data Persistence:** Utilizes MongoDB to store mission request details persistently.
- **Automated Submission:** Upon form submission, mission details are sent as a payload to the FastAPI backend for processing and storage.
- **Note:** Although JWT was suggested for authentication in the assignment, this implementation uses basic username/password validation.

## Tech Stack
- **Frontend:** AppSmith (low-code tool for UI development)
- **Backend:** Python's FastAPI
- **Database:** MongoDB
- **Deployment:** Backend API deployed on Vercel
- **Version Control:** Managed using GitHub

## Project Structure
- **Backend Code:** Contains FastAPI endpoints for user authentication, fetching mission requests, and saving submitted mission details.
- **Frontend Implementation:** Configured on AppSmith to connect with the backend API and dynamically render mission forms.
- **Documentation:** Includes setup instructions, architectural diagrams, and assumptions (refer to `setup.md`, `architecture.md`, and `assumptions.md`).

## Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/suyashbha/ShieldOps-Request-Portal.git
