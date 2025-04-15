from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(title="Просте API")

class Item(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

db = {}

def get_item_or_404(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Товар не знайдений")
    return db[item_id]

@app.get("/")
def read_root():
    return {"message": "Ласкаво просимо в простий додаток!"}

@app.get("/items/", response_model=List[Item])
def read_items():
    return list(db.values())

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str):
    item = get_item_or_404(item_id)
    return item

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    if not item.id:
        item.id = str(uuid.uuid4())
    db[item.id] = item
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, item: Item):
    get_item_or_404(item_id) 
    db[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: str):
    get_item_or_404(item_id)  
    del db[item_id]
    return None