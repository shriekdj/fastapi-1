
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException

# from fastapi.params import Body

from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
	# postgres://vjporhzz:WnSqbHD04RDABBYqSICcX1Gs4d-lUw9R@satao.db.elephantsql.com/vjporhzz
	# postgres://vjporhzz:WnSqbHD04RDABBYqSICcX1Gs4d-lUw9R@satao.db.elephantsql.com/vjporhzz
	try:
		conn = psycopg2.connect(database="vjporhzz",
		user="vjporhzz",
		password="WnSqbHD04RDABBYqSICcX1Gs4d-lUw9R",
		host="satao.db.elephantsql.com",
	#	port='5432',
		cursor_factory=RealDictCursor
		)

		cursor = conn.cursor()
		print("Database connection was successfull!")
		break
	except Exception as error:
		print("Connecting to database failed")
		print("Error: ", error)
		time.sleep(2)

my_posts = [
	{"title": "title of post 1", "content": "content of post 1", "id": 1},
	{"title": "favorite foods", "content": "I like pizza", "id": 2},
]

def find_post(id):
	for p in my_posts:
		if p["id"] == id:
			return p

def find_index_post(id):
	for i, p in enumerate(my_posts):
		if p["id"] == id:
			return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get('/')
def root():
	return {"message": "Hello World"}

