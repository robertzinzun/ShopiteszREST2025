from fastapi import APIRouter

router=APIRouter(prefix="/pedidos",tags=["Pedidos"])

@router.post("/")
async def crearPedido():
    return {"mensaje":"Creando un pedido"}

@router.put("/")
async def modificarPedido():
    return {"mensaje":"Modificando pedido"}

@router.delete("/")
async def eliminarPedido():
    return {"mensaje":"Eliminado pedido"}

@router.get("/")
async def consultaPedidos():
    return {"mensaje":"Consultando los pedidos"}

@router.get("/{idPedido}")
async def consultarPedido(idPedido:str):
    return {"mensaje":"Consultando el pedido:"+idPedido}
