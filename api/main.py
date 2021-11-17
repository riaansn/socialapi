from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, post, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine) # only needed if not using alembic

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "This is our api root path welcome..."}
