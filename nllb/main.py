from model import Translator
from typing import Optional
from fastapi import FastAPI, Response
from pydantic import BaseModel

import orjson

translator = Translator()
app = FastAPI()

class Item(BaseModel):
    text: str
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/translate/")
async def translate(item: Item):
    item_dict = item.model_dump()
    
    translated = await translator.translate(item_dict["text"])
    
    return Response(
            status_code=200,
            content=orjson.dumps({"translated": translated}, default=str),
            media_type="application/json")
        
    
