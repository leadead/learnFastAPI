from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import Base, get_db

# 创建用户模型
class User(Base):
    ...

# 创建用户注册路由
@app.post("/register/", response_model=User)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    ...

# 创建用户登录路由
@app.post("/login/")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    ...

# 创建用户注销路由
@app.post("/logout/")
def logout_user(current_user: User = Depends(get_current_user)):
    ...
