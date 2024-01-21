from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

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

my_posts= [{"state": "Telangana", "city": "hyderabad", "id": 1}, {"state": "karnataka", "city": "Bangalore", "id": 2} ]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        print("i value is:", i ,"p value is:", p)
        if p['id'] == id:
            return i




@app.get("/")
async def root():
    return {"message": "Welcome to API"}

@app.get("/posts")
def get_posts():
    cursor.execute("""select * from posts""")
    posts=cursor.fetchall()
    # print(posts)
    return {"data": posts}

# @app.post("/createpost")
# def post_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"data": f"State is {payload['state']} city is: {payload['city']}  successfully"}
###pydanti restricting only state( str) and city (str)
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def post_posts(new_post: Post):
    print(Post)
    # print(new_post)
    # post_dict= new_post.dict()
    # post_dict['id']= randrange(1,10000)
    cursor.execute("""insert into posts (state, city) values (%s, %s) returning *""", (new_post.state, new_post.city))

    # my_posts.append(post_dict)
    new_post=cursor.fetchone()
    conn.commit()

    return {"data": new_post}

#Getting a single post
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    # post = find_post(int(id))
    cursor.execute("""select * from posts where id = %s""", (str(id), ))
    post=cursor.fetchone()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND   // basic methos of raising exception//
        # return {'message': f"post with id {id} was not found"}
    return {"post details": post}

##Delete post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # index = find_index_post(id)
    cursor.execute("""delete from posts where id = %s returning *""", (str(id), ))
    deleted_post=cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post details not found {id}")
    # my_posts.pop(index)
    # return {'message': f'post was removed {id}'}
    return Response(status_code=status.HTTP_204_NO_CONTENT)

##Update post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    # index=find_index_post(id)
    cursor.execute("""update posts set state= %s, city= %s where id= %s returning *""", (post.state, post.city, str(id)))
    updated_post= cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id {id} not found")
    
    # post_dict=post.dict()
    # post_dict['id']=id
    # my_posts[index]= post_dict
    return {"data": updated_post}