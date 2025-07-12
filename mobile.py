from fastapi import APIRouter
from models import Mobile, MobileUpdate
from database import db


router=APIRouter()
collection=db["mobiles"]


@router.post("/add_mobile/")
def Add_mobiles(mobile:Mobile):
    try:
        data=mobile.dict()
        result=collection.insert_one(data)
        return {"message":"Add mobile"}
    except Exception as e:
        return {"stetus ": "error" ,"message":str(e)}
    


    
@router.get("/get_all_mobiles")
def get_all():
    try:
        result=list(collection.find({},{"_id":0}))
        return {"data":result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    


@router.get("/get_mobile/{model}")
def get_mobile(model: str):
    try:
        result=collection.find_one({"model":model.strip().lower()},{"_id":0})
        if result:
            return {"data":result}
        else:  
            return {"status": "error", "message": "Mobile not found"}
    except Exception as e:  
        return {"status": "error", "message": str(e)}
    
    

@router.put("/update_mobile/{brand}")
def update_mobile(brand: str, mobile: MobileUpdate):
    try:
        query = {"brand": brand.lower()}
        existing = collection.find_one(query)

        if not existing:
            return {"message": "Mobile not found"}

        set_fields = {}

        if mobile.model and mobile.model.strip().lower() != "string":
            set_fields["model"] = mobile.model.strip()

        if mobile.price is not None and mobile.price != 0:
            set_fields["price"] = mobile.price

        if mobile.specs and mobile.specs != ["string"]:
            set_fields["specs"] = mobile.specs

        if mobile.img_url and mobile.img_url.strip().lower() != "string":
            set_fields["img_url"] = mobile.img_url.strip()

        if mobile.brand and mobile.brand.strip().lower() != "string":
            set_fields["brand"] = mobile.brand.strip().lower()

        if not set_fields:
            return {"message": "No valid data to update"}

        result = collection.update_one(query, {"$set": set_fields})

        if result.modified_count == 1:
            return {"message": "Mobile updated successfully"}
        else:
            return {"message": "Data already same, no changes made"}

    except Exception as e:
        return {"message": "Error", "error": str(e)}

    
    

@router.delete("/delete_mobile/{model}")
def delete_mobile(model: str):
    try:
        result=collection.delete_one({"model":model.strip().lower()})
        if result.deleted_count > 0:
            return {"message":"Mobile deleted successfully"}
        else:
            return {"status": "error", "message": "Mobile not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
     








