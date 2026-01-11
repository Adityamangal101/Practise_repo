from fastapi import Depends, HTTPException, APIRouter
from ..models import User
from ..database import SessionLocal
from ..schemas import Register, Login
import bcrypt
from sqlalchemy.orm import Session

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

router=APIRouter()

@router.post("/register")
def user_register(user:Register,db: Session=Depends(get_db)):
     
     existing_user=db.query(User).filter(User.username==user.username).first()

     if existing_user:
         return {"message":"User already exist"}
     
     hashed=bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())

     new_user=User(username=user.username,password=hashed)
     db.add(new_user)
     db.commit()
     db.refresh(new_user)

     return {"message":"user registered successfully"}

@router.post("/login")
def user_login(user:Login,db: Session=Depends(get_db)):
    db_user= db.query(User).filter(User.username==user.username).first()

    if not db_user or not bcrypt.checkpw(user.password.encode(),db_user.password):
        return{"message":"invalid credentials"}
    
    return {"message":"User loggedin successfully"}
