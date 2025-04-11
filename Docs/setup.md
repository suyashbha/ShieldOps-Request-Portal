# Setup Instructions

This document explains how to set up and test the project locally.

## Prerequisites

- A FastAPI backend server that is already online.
- An Appsmith account (you can use the cloud version at [app.appsmith.com](https://app.appsmith.com/) or a locally hosted instance).
- Git installed.

## 1. FASTAPI Backend
I have already deployed my backend online at https://shieldops-puce.vercel.app/, and it can be used for api calls from anywhere.

##### In case of Local Hosting:
I have included all the backend files along with requirements.txt file, so that the server can be started locally as well. In case of local hosting, you will need to creat a .env file
in which you will need to specify the MONGO_URI, referring to the database cluster you will need to create. In this case, you will also need to run the add_users.py script to add the sample users to
mongo db, before logging in.

## 2. Frontend (using appsmith)
I have included a SHIELDOpsRequestPortal.json file in my frontend folder, to import the application, go to appsmith, in your workspace, click on Create New -> import -> SHIELDOpsRequestPortal.json,
it will create the frontend application in edit view, just click on deploy to see the final version of the application. you will be redirected to the login page, and you can login using some of the
sample users I have created :

#### Sample User 1:
  Username: agent.coulson
  
  Password: password123
#### Sample User 2:
  Username: agent.pepper
  
  Password: securepass456
#### Sample User 3:
  Username: agent.may
  
  Password: topsecret789


  After logging in, you will be redirected to fetch missions page where you can view the available missions. From there, you can also create a new missions with the details accordingly.

## 3. Testing the application
#### Front-End: Use the Appsmith UI to create missions, log in, and view data. The actions will send requests to your online backend.
#### Backend Logs: Monitor your online backend logs to verify that API calls from Appsmith are processed successfully.


