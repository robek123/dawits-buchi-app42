
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client['pet_db']


# Model

class Pet(BaseModel):
    name: str
    pet_type: str
    status: str


# Endpoints

@app.post("/create_pet")
async def create_pet(pet: Pet):
    db['pet_collection'].insert_one(pet.dict())
    return {"detail": "Pet created successfully"}
