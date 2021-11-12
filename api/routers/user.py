from sqlalchemy.sql.functions import mode
from .. import models, schemas, utils
from ..database import get_db
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["User Endpoints"]
)


@router.post("/", response_model=schemas.UserResponse)
async def get_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        user.password = utils.hashing(user.password)
        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        return {"ERROR": "The email has already been registered."}


@router.get("/{id}", response_model=schemas.UserResponse)
async def get_user(id: int, db: Session = Depends(get_db)):
    user_info = db.query(models.User).filter(models.User.id == id).first()

    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User with id: {}, could not be found.".format(id))
    return user_info
