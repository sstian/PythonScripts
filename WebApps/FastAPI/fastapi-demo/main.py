from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from routers import users

# FastAPI 是直接从 Starlette 继承的类。
app = FastAPI()

app.include_router(users.router, prefix="/api/users")


# 使用 Pydantic 模型声明请求体，创建数据模型
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


"""
路径操作装饰器：
@app.get()
@app.post()
@app.put()
@app.delete()
@app.options()
@app.head()
@app.patch()
@app.trace()
"""
@app.get("/")
def read_root():
    return {"msg": "Hello World"}

# GET 请求
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

"""
函数参数按如下规则进行识别：
- 路径中声明了相同参数的参数，是路径参数
- 类型是（int、float、str、bool 等）单类型的参数，是查询参数
- 类型是 Pydantic 模型的参数，是请求体
"""
# PUT 请求
# 路径参数 - item_id
# 查询参数 - short 必选，q 可选
# 请求体 - item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, short: bool, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

