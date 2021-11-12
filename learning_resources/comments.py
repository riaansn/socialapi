"""This contains information of methods of doing tasks that is useful for learing api's...
# from typing import List, Optional
# from fastapi import FastAPI, status, HTTPException, Response, Depends
# from fastapi.params import Body
# from pydantic import BaseModel
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from sqlalchemy.sql.functions import mode, user
# from . import models, schemas, utils
# from .database import engine, get_db
# from sqlalchemy.orm import Session

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}


# my_posts = [{"Title": "Working with API's", "Content": "I like learning about API's", "id": 1}, {
#     "Title": "CRUD is important...", "Content": "To interact with an API we use the CRUD model to manipulate data...", "id": 2}]


# try:
#     conn = psycopg2.connect(host="localhost", database="fastapi",
#                             user="postgres", password='postgres', cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connected...")
# except Exception as e:
#     print("Connection to database failed")
#     print("Connection Error: {}".format(e))


# def find_post(id):
#     for post in my_posts:
#         if post["id"] == id:
#             return post


# def find_post_index(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i

# @app.get("/test/{pw}")
# async def test(pw: str):
#     my_hash = utils.hashing(pw)
#     print(my_hash)
#     return {"hash": my_hash}

############## Oauth changes
@router.post("/login")
async def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credentials.email).first()
    
########## Database connection"""
# cursor.execute(""" SELECT * FROM posts """)
# posts = cursor.fetchall()
# return {"data": posts}

# cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING *""",
#                (post.title, post.content, post.published))
# new_post = cursor.fetchone()
# conn.commit()

# new_post = models.Post(
#     title=post.title, content=post.content, published=post.published)

# cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
# user_post = cursor.fetchone()
# return {"post": user_post}

# cursor.execute(
#     """DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
# deleted_post = cursor.fetchone()

# cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING * """,
#                (post.title, post.content, post.published, str(id)))
# updated_post = cursor.fetchone()
# return {"data": post_update.first()}
"""

"""
