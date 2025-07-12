from fastapi import FastAPI
from mobile import router  
from charger import rou
from headphone import ro
from acceseries import acess
import uvicorn


app = FastAPI()
app.include_router(router, prefix="/Mobile", tags=["Mobile"]) 
app.include_router(rou, prefix="/Charger", tags=["Charger"])
app.include_router(ro, prefix="/Headphone", tags=["Headphone"]) 
app.include_router(acess, prefix="/Accessory", tags=["Accessory"]) 



@app.get("/")
def home():
    return {"message": "Welcome to the Mobile API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    

