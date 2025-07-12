from fastapi import APIRouter
from models import Headphone, HeadphoneUpdate
from database import db

ro = APIRouter()
collection = db["headphones"]


@ro.post("/add_headphone/")
def add_headphone(headphone:Headphone):
    try:
        data=headphone.dict()
        result=collection.insert_one(data)
        return {"message":"Headphone added successfully", "id": str(result.inserted_id)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

    
@ro.get("/get_all_headphones")
def get_all_headphones():
    try:
        result = list(collection.find({}, {"_id": 0}))
        return {"data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    
    
@ro.get("/get_headphone/{brand}")
def get_headphone(brand: str):
    try:
        result = collection.find_one({"brand": brand}, {"_id": 0})
        if result:
            return {"data": result}
        else:
            return {"status": "error", "message": "Headphone not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    
    
@ro.put("/update_headphone/{brand}")
def update_mobile(brand: str, headphone: HeadphoneUpdate):
    try:
        query = {"brand": brand.lower()}
        existing = collection.find_one(query)

        if not existing:
            return {"message": "Mobile not found"}

        set_fields = {}

        if headphone.model and headphone.model.strip().lower() != "string":
            set_fields["model"] = headphone.model.strip()

        if headphone.price is not None and headphone.price != 0:
            set_fields["price"] = headphone.price

        if headphone.specs and headphone.specs != ["string"]:
            set_fields["specs"] = headphone.specs

        if headphone.img_url and headphone.img_url.strip().lower() != "string":
            set_fields["img_url"] = headphone.img_url.strip()

        if headphone.brand and headphone.brand.strip().lower() != "string":
            set_fields["brand"] = headphone.brand.strip().lower()

        if not set_fields:
            return {"message": "No valid data to update"}

        result = collection.update_one(query, {"$set": set_fields})

        if result.modified_count == 1:
            return {"message": "Mobile updated successfully"}
        else:
            return {"message": "Data already same, no changes made"}

    except Exception as e:
        return {"message": "Error", "error": str(e)}

    
    

@ro.delete("/delete_headphone/{brand}")
def delete_headphone(brand: str):
    try:
        result = collection.delete_one({"brand": brand})
        if result.deleted_count > 0:
            return {"message": "Headphone deleted successfully"}    
        else:
            return {"status": "error", "message": "Headphone not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
