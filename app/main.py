import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from utils.openapi_documentation import CustomServerAPI
from database.tables import connect_database, disconnect_database
from rest_api import files_router, register_routers, profile_routers, auth_routers, users_routers, server_routers,channel_routers
from rest_api.exceptions import *
import config



app = FastAPI()
app.openapi = CustomServerAPI(app).get_openapi()



app.include_router(auth_routers)
app.include_router(register_routers)
app.include_router(profile_routers)
app.include_router(users_routers)
app.include_router(server_routers)
app.include_router(files_router)
app.include_router(channel_routers)



# exception handler for jwtauth
app.add_exception_handler(AuthJWTException, authjwt_exception_handler)
app.add_exception_handler(HTTPNotFoundError, http_not_found_exception_handler)
app.add_exception_handler(HTTPUnprocessableEntity, http_unprocessable_entity_exception_handler)



@app.on_event("startup")
async def start():
    await connect_database()



@app.on_event("shutdown")
async def stop():
    await disconnect_database()



@app.get("/domain", tags=["domain"])
async def mainpage():
    return {"name": config.SERVER_NAME, "status": "working"}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host=config.HOST, port=config.PORT)
