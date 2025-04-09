import datetime

from fastapi import APIRouter

from dao.pedidosDAO import PedidoDAO
from models.PedidoModel import Item, PedidoInsert, PedidoPay, Salida, PedidosSalida,Comprador,Vendedor,PedidoSelect
from fastapi import Request
router=APIRouter(prefix="/pedidos",tags=["Pedidos"])

@router.post("/",response_model=Salida,summary="Creación de un Pedido")
async def crearPedido(pedido:PedidoInsert,request:Request)->Salida:
    pedidoDAO=PedidoDAO(request.app.db)
    return pedidoDAO.agregar(pedido)
@router.put("/",summary="Modificación de un Pedido")
async def modificarPedido():
    return {"mensaje":"Modificando pedido"}

@router.delete("/",summary="Eliminación de un pedido")
async def eliminarPedido():
    return {"mensaje":"Eliminado pedido"}

@router.get("/",response_model=PedidosSalida,response_description="Consulta de Pedidos",description="Consulta General de Pedidos",summary="Consulta de Pedidos")
async def consultaPedidos(request:Request)->PedidosSalida:
    pedidoDAO=PedidoDAO(request.app.db)
    return pedidoDAO.consultaGeneral()
@router.get("/{idPedido}",summary="Consulta de un pedido")
async def consultarPedido(idPedido:str):
    return {"mensaje":"Consultando el pedido:"+idPedido}
@router.put("/{idPedido}/agregarProducto",summary="Agregar producto al pedido")
async def agregarProductoPedido(idPedido:str,item:Item):
    salida={"mensaje":"Agregando un producto al pedido:"+idPedido,
            "item":item.dict()}
    return salida
@router.put("/pagar/{idPedido}",summary="Pagar pedido")
def pagarPedido(idPeddido:str,pedidoPay:PedidoPay):
    return {"mensaje":"Pagando el pedido con id:"+idPeddido,
            "pago":pedidoPay}