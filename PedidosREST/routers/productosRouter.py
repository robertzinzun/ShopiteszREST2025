from fastapi import APIRouter,Request
from typing import Any
from dao.productosDAO import ProductoDAO
from models.productosModel import ProductosSalida

router=APIRouter(prefix="/productos",tags=["Productos"])

@router.get("/",response_model=ProductosSalida,summary="Consulta de productos")
async def consultaGeneral(request:Request)->Any:
    #return {"mensaje":"Consultando productos"}
    productoDAO=ProductoDAO(request.app.db)
    return productoDAO.consultaGeneral()


@router.get("/{idProducto}")
async def consultaIndividual(idProducto:int):
    return {"mensaje":"Consultado el producto con id:"+str(idProducto)}

@router.get("/vendedor/{idVendedor}")
async def consultaPorVendedor(idVendedor:str):
    return {"mensaje":"Consultado productos del vendedor:"+idVendedor}

@router.get("/categoria/{idCategoria}")
async def consultaPorCategoria(idCategoria:int):
    return {"mensaje":"Consultando productos de la categoria:"+str(idCategoria)}
