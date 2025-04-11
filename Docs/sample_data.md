# Sample Input Data

This document provides sample input data for testing the API endpoints.

---

## Sample User Logins

Use the following credentials for testing user authentication:

| Username       | Password       |
|----------------|----------------|
| agent.coulson  | password123    |
| agent.pepper   | securepass456  |
| agent.may      | topsecret789   |

---

## Sample Create Mission Requests

Below are sample JSON payloads for creating missions.

### Mission Request 1

```json
{
  "agent_id": "agent.coulson",
  "mission": "Deploy Drone Surveillance Unit",
  "details": {
    "drone_id": "drn-007",
    "operation_area": "Sector 12",
    "payload": "Night Vision Camera"
  }
}
```
### Mission Request 2

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
### Mission Request 3

```json
{
  "agent_id": "agent.may",
  "mission": "Sync Classified Intelligence Database",
  "details": {
    "database_name": "classified_intel",
    "sync_frequency": "daily",
    "transmission_channel": "Secure Fiber Link"
  }
}
```
