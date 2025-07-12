from fastapi import APIRouter
from models import Charger, ChargerUpdate
from database import db


collection = db["chargers"] 
rou = APIRouter()

@rou.post("/add_charger/")
def add_charger(charger: Charger):
    try:
        data = charger.dict()
        result = collection.insert_one(data)
        return {"message": "Charger added successfully", "id": str(result.inserted_id)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

    
@rou.get("/get_all_chargers")
def get_all_chargers():
    try:
        result = list(collection.find({}, {"_id": 0}))
        return {"data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}  
     
    
    

@rou.get("/get_charger/{brand}")
def get_charger(brand: str): 
    try:
        result=collection.find_one({"brand":brand}, {"_id": 0})
        if result:
            return {"data":result}
        else:
            return {"status": "error", "message": "Charger not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)} 
      

@rou.put("/update_mobile/{brand}")
def update_mobile(brand: str, charger: ChargerUpdate):
    try:
        query = {"brand": brand.lower()}
        existing = collection.find_one(query)

        if not existing:
            return {"message": "Mobile not found"}

        set_fields = {}

        if charger.model and charger.model.strip().lower() != "string":
            set_fields["model"] = charger.model.strip()

        if charger.price is not None and charger.price != 0:
            set_fields["price"] = charger.price

        if charger.specs and charger.specs != ["string"]:
            set_fields["specs"] = charger.specs

        if charger.img_url and charger.img_url.strip().lower() != "string":
            set_fields["img_url"] = charger.img_url.strip()

        if charger.brand and charger.brand.strip().lower() != "string":
            set_fields["brand"] = charger.brand.strip().lower()

        if not set_fields:
            return {"message": "No valid data to update"}

        result = collection.update_one(query, {"$set": set_fields})

        if result.modified_count == 1:
            return {"message": "Mobile updated successfully"}
        else:
            return {"message": "Data already same, no changes made"}

    except Exception as e:
        return {"message": "Error", "error": str(e)}

    

    

@rou.delete("/delete_charger/{brand}")
def delete_charger(brand: str):
    try:
        result = collection.delete_one({"brand": brand})
        if result.deleted_count > 0:
            return {"message": "Charger deleted successfully"}      
        else:
            return {"status": "error", "message": "Charger not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

