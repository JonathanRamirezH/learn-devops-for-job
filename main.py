from enum import Enum

from fastapi import FastAPI

#Make fake Array Enum to use in API
class ModelName(str, Enum):
    Jonathan = "Jonathan"
    Jose = "Jose"
    Luis = "Luis"

app= FastAPI()

@app.get("/")
async def main():
    return str("Hello to new website using API")

#MAKE API WITH "PATH PARAMETERS"
@app.get("/user/{user_name}")
async def getUserName(user_name):
    return {"Nombred del usuario:":user_name}

# Path Parameters with data validation over API one
@app.get("/brand_car/search/{brandCar}")
async def showBrandCar(brandCar: str):
    return {"marca seleccionada": brandCar}

#Make GET request throught ENUM class to choice value
@app.get("/brand/selectPartner/{model_name}")
async def selectPartner(model_name:ModelName):
    if model_name is ModelName.Jonathan:
        return {"Partner name":model_name, "ranking":1}
    if model_name.value == "Jose":
        return{"Partner name": model_name, "ranking":2}
    return {"Default Partner":model_name}