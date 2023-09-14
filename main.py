from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description : str | None = None
    price : float
    tax: float | None = None
    
@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/{q}")
async def read_item(q: int = Path(gt=2, title="hahaha")):
    results = {"items": [{"item_name": "Foo"}, {"item_name": "Bar"}]}
    if q:
        results.update({"q": q})
    return results