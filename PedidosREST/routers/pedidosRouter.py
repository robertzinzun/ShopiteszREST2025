import datetime

from fastapi import APIRouter

from models.PedidoModel import Item, PedidoInsert, PedidoPay, Salida, PedidosSalida,Comprador,Vendedor,PedidoSelect

router=APIRouter(prefix="/pedidos",tags=["Pedidos"])

@router.post("/",response_model=Salida,summary="Creación de un Pedido")
async def crearPedido(pedido:PedidoInsert)->Salida:
    salida=Salida(estatus="OK",mensaje="Pedido creado con exito")
    #return {"mensaje":"Creando un pedido","pedido":pedido}
    return salida
@router.put("/",summary="Modificación de un Pedido")
async def modificarPedido():
    return {"mensaje":"Modificando pedido"}

@router.delete("/",summary="Eliminación de un pedido")
async def eliminarPedido():
    return {"mensaje":"Eliminado pedido"}

@router.get("/",response_model=PedidosSalida,response_description="Consulta de Pedidos",description="Consulta General de Pedidos",summary="Consulta de Pedidos")
async def consultaPedidos()->PedidosSalida:
    comprador=Comprador(idComprador=1,nombre="Juan")
    vendedor=Vendedor(idVendedor=1,nombre="WALMART")
    pedido=PedidoSelect(idPedido="500",fechaRegistro=datetime.date.today(),
                        fechaConfirmacion=datetime.date.today(),fechaCierre=datetime.date.today(),
                        costosEnvio=100,subtotal=200,totalPagar=3000,estatus="Pagado",
                        comprador=comprador,vendedor=vendedor)
    lista=[]
    lista.append(pedido)
    salida=PedidosSalida(estatus="OK",mensaje="Consulta de Pedidos",pedidos=lista)
    #return {"mensaje":"Consultando los pedidos"}
    return salida
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