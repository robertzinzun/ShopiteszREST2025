# This is a sample Python script.
import uvicorn
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Import la clase FastAPI del framework
from fastapi import FastAPI

# crear una instancia de la clase FastAPI
app=FastAPI()

@app.get("/")
async def home():
    salida = {"mensaje": "Bienvenido a PEDIDOSREST"}
    return salida

@app.post("/pedidos")
async def crearPedido():
    return {"mensaje":"Creando un pedido"}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app",host='127.0.0.1',reload=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
