from models.PedidoModel import PedidoInsert,Salida,PedidosSalida
from datetime import date
from dao.usuariosDAO import UsuarioDAO
from fastapi.encoders import jsonable_encoder
class PedidoDAO:
    def __init__(self,db):
        self.db=db
    def agregar(self,pedido:PedidoInsert):
        salida=Salida(estatus="",mensaje="")
        try:
            pedido.fechaRegistro=date.today()
            if pedido.idVendedor!=pedido.idComprador:
                usuarioDAO=UsuarioDAO(self.db)
                if usuarioDAO.comprobarUsuario(pedido.idComprador) and usuarioDAO.comprobarUsuario(pedido.idVendedor):
                    result=self.db.pedidos.insert_one(jsonable_encoder(pedido))
                    salida.estatus="OK"
                    salida.mensaje="Pedido agregado con exito con id:"+str(result.inserted_id)
                else:
                    salida.estatus="ERROR"
                    salida.mensaje="El usuario comprador o el vendedor no existen o no se encuentran activos."
            else:
                salida.estatus="ERROR"
                salida.mensaje="No se puede agregar el pedido, porque los ids de los usuarios son iguales."
        except Exception as ex:
            print(ex)
            salida.estatus="ERROR"
            salida.mensaje="Erro al agregar el pedido, consulta al administrador."
        return salida
    def consultaGeneral(self):
        salida=PedidosSalida(estatus="",mensaje="",pedidos=[])
        try:
            lista=list(self.db.pedidosView.find())
            salida.estatus="OK"
            salida.mensaje="Listado de pedidos"
            salida.pedidos=lista
        except Exception as ex:
            print(ex)
            salida.estatus="ERROR"
            salida.mensaje="Error al consultar los pedidos, consulta al administrador."
        return salida

