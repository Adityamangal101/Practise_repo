from pydantic import BaseModel

class Register(BaseModel):
    username: str
    password:str

class Login(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    id:int
    username:str

    class config:
        orm_mode=True