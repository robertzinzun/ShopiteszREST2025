from fastapi import APIRouter

router=APIRouter(prefix="/productos",tags=["Productos"])

@router.get("/")
async def consultaGeneral():
    return {"mensaje":"Consultando productos"}

@router.get("/{idProducto}")
async def consultaIndividual(idProducto:int):
    return {"mensaje":"Consultado el producto con id:"+str(idProducto)}

@router.get("/vendedor/{idVendedor}")
async def consultaPorVendedor(idVendedor:str):
    return {"mensaje":"Consultado productos del vendedor:"+idVendedor}

@router.get("/categoria/{idCategoria}")
async def consultaPorCategoria(idCategoria:int):
    return {"mensaje":"Consultando productos de la categoria:"+str(idCategoria)}
