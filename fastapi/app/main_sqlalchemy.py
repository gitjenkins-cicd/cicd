from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    state: str
    city: str

try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='postgres', cursor_factory=RealDictCursor)
    cursor= conn.cursor()
    print("Database connection is successful")
except Exception as error:
    print("Connecting to database is failed")
    print("Error", error)

@app.get("/posts")
def get_posts():
    cursor.execute("""select * from posts""")
    posts=cursor.fetchall()
    # print(posts)
    return {"data": posts}

@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return("Data:", posts)
    
@app.post("/sqlalchemy", status_code=status.HTTP_201_CREATED)
def create_post(post: Post, db: Session = Depends(get_db) ):
    new_post = models.Post(state=post.state, city=post.city)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"Data:": new_post }