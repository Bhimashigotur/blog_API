from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Login(BaseModel):
    email: EmailStr
    password: str

class PostCreate(BaseModel):
    title: str
    content: str

class CommentCreate(BaseModel):
    post_id: int
    content: str
