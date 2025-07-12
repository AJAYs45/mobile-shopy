from pydantic import BaseModel
from typing import Optional

class Mobile(BaseModel):
    brand:str
    model:str
    price:float
    specs:list[str]
    img_url:str


class MobileUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    price: Optional[float] = None
    specs: Optional[list[str]] = None
    img_url: Optional[str] = None


class Charger(BaseModel):
    brand:str
    type:str
    price:float
    specs:list[str]
    img_url:str


class ChargerUpdate(BaseModel):
    brand: Optional[str] = None
    type: Optional[str] = None
    price: Optional[float] = None
    specs: Optional[list[str]] = None
    img_url: Optional[str] = None


class Headphone(BaseModel):
    brand:str
    wirless:bool
    price:float
    specs:list[str]
    img_url:str
    

class HeadphoneUpdate(BaseModel):
    brand: Optional[str] = None
    wirless: Optional[bool] = None
    price: Optional[float] = None
    specs: Optional[list[str]] = None
    img_url: Optional[str] = None


class Accessory(BaseModel):
    name:str
    category:str
    price:float
    specs:list[str]
    img_url:str



class AccessoryUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    specs: Optional[list[str]] = None
    img_url: Optional[str] = None