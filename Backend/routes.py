from fastapi import APIRouter, HTTPException, Depends
from models import Mission, User
from database import get_db_client
import bcrypt

router = APIRouter()
#access the database
def get_collections():

    db = get_db_client()
    missions_collection = db["missions"]
    users_collection = db["users"]
    return {"missions_collection": missions_collection, "users_collection": users_collection}

# to check login credentials
@router.post("/auth/login")
async def login(user: User, collections=Depends(get_collections)):
    users_collection = collections["users_collection"]
    
    stored_user = await users_collection.find_one({"username": user.username})
    if not stored_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    #check hashed password
    if not bcrypt.checkpw(user.password.encode(), stored_user["password"].encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful"}

#to create a new mission
@router.post("/missions")
async def create_mission(mission: Mission, collections=Depends(get_collections)):
    missions_collection = collections["missions_collection"]

    try:
        result = await missions_collection.insert_one(mission.dict())
    except Exception as e:
        print("Error inserting mission:", e)
        raise HTTPException(status_code=500, detail="Database error during mission creation")
    
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to create mission")
    
    return {"message": "Mission created", "id": str(result.inserted_id)}

#to show already created missions
@router.get("/missions")
async def get_missions(collections=Depends(get_collections)):
    missions_collection = collections["missions_collection"]
    try:
        missions = await missions_collection.find().to_list(length=100)
    except Exception as e:
        print("Error retrieving missions:", e)
        raise HTTPException(status_code=500, detail="Database error during retrieving missions")
    
    for mission in missions:
        mission["_id"] = str(mission["_id"])
        print("Converted _id to string")
    
    return {"missions": missions}
