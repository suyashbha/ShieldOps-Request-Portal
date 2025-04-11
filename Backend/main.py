from fastapi import FastAPI
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="S.H.I.E.L.D Ops Request Portal",
    description="API for mission requests",
    version="1.0.0",
)

# Enable CORS middleware (adjust allow_origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# including the router with a prefix for clarity
app.include_router(router, prefix="/api")

# home route just to check if backend is running  or not
@app.get("/")
def read_root():
    return {"message": "S.H.I.E.L.D Ops API is running!"}

# To run the app, use:
# uvicorn main:app --host 0.0.0.0 --port 8000
