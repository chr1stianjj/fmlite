from fastapi import FastAPI
from backend.api.players_router import router as players_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Backend Sandbox")

# CORS for frontend running on a different port
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the players router
app.include_router(players_router, prefix="/players")
