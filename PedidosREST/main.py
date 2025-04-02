# This is a sample Python script.
import uvicorn
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Import la clase FastAPI del framework
from fastapi import FastAPI

from dao.database import Conexion
from routers import pedidosRouter,productosRouter,usuariosRouter
# crear una instancia de la clase FastAPI
app=FastAPI()
app.include_router(pedidosRouter.router)
app.include_router(productosRouter.router)
app.include_router(usuariosRouter.router)
@app.get("/")
async def home():
    salida = {"mensaje": "Bienvenido a PEDIDOSREST"}
    return salida
@app.on_event("startup")
async def startup():
    print("Conectando con MongoDB")
    conexion=Conexion()
    app.conexion=conexion
    app.db=conexion.getDB()
@app.on_event("shutdown")
async def shutdown():
    print("Cerrando la conexion con MongoDB")
    app.conexion.cerrar()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app",host='127.0.0.1',reload=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
