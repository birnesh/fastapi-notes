from fastapi import FastAPI
from app.db.database import engine, database, metadata
from app.api.api import api_rounter

metadata.create_all(engine)
app = FastAPI(
    title="practice"
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(api_rounter)



# from typing import Optional
# from pydantic import BaseModel
# from fastapi.responses import HTMLResponse
# # fake DB
# car_db = [
#     {"name":"alto", "year":1980, "description": None },
#     {"name":"swift", "year":1980, "description": None},
#     {"name":"desire", "year":1980, "description": None},
#     {"name":"baleno", "year":1980, "description": None},
# ]

# # car pydantic model
# class Car(BaseModel):
#     name: str
#     year: int
#     description: Optional[str] = None

# @app.get('/')
# async def root():
#     return {"message":"hello world"}


# @app.get('/api/v1/item/{item_id}')
# async def get_item(item_id: int):
#     return {"item":f"you asked for item {item_id} which is of type {type(item_id)}"}


# @app.get('/api/v1/cars/')
# async def car_list(skip: int=0, limit: int=2, format: Optional[str]=None):
#     return car_db[skip:skip+limit]


# @app.post('/api/v1/cars/', status_code=201)
# async def register_car(car_obj: Car):
#     car_db.append(car_obj)
#     return {"message":"Car successfully added"}


# @app.get("/api/v1/files/")
# async def upload_file():
#     content = """
#     <body>
#     <form action="/files/" enctype="multitype/form-data" method="post">
#     <input name="files" type="file" multiple>
#     <input type="submit">
#     </form>
#     </body
#     """
#     return HTMLResponse(content=content)