from .. import models, schemas
from ..database import get_db
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/posts",
    tags=["Post Endpoints"]
)


@router.get("/", response_model=List[schemas.PostResponse])
async def get_posts(db: Session = Depends(get_db), current_user: int = Depends(get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    return db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
async def create_posts(post: schemas.Post, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.PostResponse)
async def get_user_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    user_post = db.query(models.Post).filter(models.Post.id == id).first()
    if not user_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post with id: {} was not found".format(id))
    return user_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    post_to_delete = db.query(models.Post).filter(models.Post.id == id)
    RequestException(post_to_delete.first(), current_user, "delete", id)
    # if post_to_delete.first() == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail="Post with id: {} could not be found".format(id))
    # post = post_to_delete.first()

    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail="Unautherized to delete this post.")
    post_to_delete.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.PostResponse)
async def update_post(id: int, post: schemas.Post, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    RequestException(post_query.first(), current_user, "update", id)
    # post_update = post_query.first()
    # if post_update == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
    #                         "message": "Post with id: {} could not be found".format(id)})
    # if post_update.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail="Unautherized to update this post.")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()


def RequestException(obj1, obj2, type, id=0):
    if obj1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "message": "Post with id: {} could not be found".format(id)})
    if obj1.owner_id != obj2.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Unautherized to {} this post.".format(type))
