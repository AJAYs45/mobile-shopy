from fastapi import APIRouter
from models import Accessory, AccessoryUpdate
from database import db

acess= APIRouter()
collection = db["accessories"]  

@acess.post("/add_accessory/")
def add_accessory(accessory: Accessory):
    try:
        data = accessory.dict()
        result = collection.insert_one(data)
        return {"message": "Accessory added successfully", "id": str(result.inserted_id)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

@acess.get("/get_all_accessories")
def get_all_accessories():
    try:
        result = list(collection.find({}, {"_id": 0}))
        return {"data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    
    
@acess.get("/get_accessory/{name}")
def get_accessory(name: str):
    try:
        result = collection.find_one({"name": name}, {"_id": 0})
        if result:
            return {"data": result}
        else:
            return {"status": "error", "message": "Accessory not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    

@acess.put("/update_mobile/{brand}")
def update_mobile(brand: str, acesse: AccessoryUpdate):
    try:
        query = {"brand": brand.lower()}
        existing = collection.find_one(query)

        if not existing:
            return {"message": "Mobile not found"}

        set_fields = {}

        if acesse.model and acesse.model.strip().lower() != "string":
            set_fields["model"] = acesse.model.strip()

        if acesse.price is not None and acesse.price != 0:
            set_fields["price"] = acesse.price

        if acesse.specs and acesse.specs != ["string"]:
            set_fields["specs"] = acesse.specs

        if acesse.img_url and acesse.img_url.strip().lower() != "string":
            set_fields["img_url"] = acesse.img_url.strip()

        if acesse.brand and acesse.brand.strip().lower() != "string":
            set_fields["brand"] = acesse.brand.strip().lower()

        if not set_fields:
            return {"message": "No valid data to update"}

        result = collection.update_one(query, {"$set": set_fields})

        if result.modified_count == 1:
            return {"message": "Mobile updated successfully"}
        else:
            return {"message": "Data already same, no changes made"}

    except Exception as e:
        return {"message": "Error", "error": str(e)}

    
    

@acess.delete("/delete_accessory/{name}")
def delete_accessory(name: str):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            return {"message": "Accessory deleted successfully"}
        else:
            return {"status": "error", "message": "Accessory not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
