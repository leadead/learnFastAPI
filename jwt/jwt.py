from fastapi import Depends
from jose import JWTError, jwt
from models import User

# 身份验证函数
def get_current_user(token: str = Depends(get_token)):
    ...

# 装饰器函数来验证用户权限
def check_permission(current_user: User = Depends(get_current_user)):
    ...

# 保护需要权限的API端点
@app.get("/protected/")
def protected_route(current_user: User = Depends(check_permission)):
    ...