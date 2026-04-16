from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Base, User, Post, Comment, Like  # Import your models
from database import engine, get_db  # Import your database connection settings
from schemas import UserCreate, UserLogin, PostCreate, CommentCreate  # Import your schemas

app = FastAPI()

# Create all database tables on startup
@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

@app.post("/auth/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Registration logic
    raise HTTPException(status_code=201, detail="User registered")

@app.post("/auth/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Login logic
    raise HTTPException(status_code=200, detail="Login successful")

@app.post("/posts/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    # Create post logic
    raise HTTPException(status_code=201, detail="Post created")

@app.get("/posts/")
def read_posts(db: Session = Depends(get_db)):
    # Read all posts logic
    raise HTTPException(status_code=200, detail="Posts retrieved")

@app.get("/posts/{id}")
def read_post(id: int, db: Session = Depends(get_db)):
    # Read single post logic
    raise HTTPException(status_code=200, detail="Post retrieved")

@app.put("/posts/{id}")
def update_post(id: int, post: PostCreate, db: Session = Depends(get_db)):
    # Update post logic
    raise HTTPException(status_code=200, detail="Post updated")

@app.delete("/posts/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    # Delete post logic
    raise HTTPException(status_code=204, detail="Post deleted")

@app.post("/posts/{id}/comments/")
def create_comment(id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    # Create comment logic
    raise HTTPException(status_code=201, detail="Comment created")

@app.get("/posts/{id}/comments/")
def read_comments(id: int, db: Session = Depends(get_db)):
    # Read comments logic
    raise HTTPException(status_code=200, detail="Comments retrieved")

@app.post("/posts/{id}/like/")
def like_post(id: int, db: Session = Depends(get_db)):
    # Like post logic
    raise HTTPException(status_code=200, detail="Post liked")

@app.get("/posts/{id}/likes/")
def get_likes(id: int, db: Session = Depends(get_db)):
    # Get likes logic
    raise HTTPException(status_code=200, detail="Likes retrieved")
