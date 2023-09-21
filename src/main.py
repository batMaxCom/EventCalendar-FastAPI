from fastapi import FastAPI
from src.event_calendar.routers import router as event_routers

app = FastAPI(
    title="Event Calendar"
)

app.include_router(event_routers)
