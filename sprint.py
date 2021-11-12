class Bodega:
    def __init__(self, id_bodega, nombre_bodega, total_producto, *proveedores):
        self.id_bodega = id_bodega
        self.nombre_bodega = nombre_bodega
        self.__total_producto = total_producto
        self.proveedores = proveedores
        self_stock_producto = {}

    def agregar_proveedor(self):
        lista_proveedores = []



    # def eliminar_proveedor(self):

    # def transferir_producto


class Proveedor:
    def __init__(self, id_proveedor, nombre_proveedor, tipo_producto):
        self.id_proveedor = id_proveedor
        self.nombre_proveedor = nombre_proveedor
        self.tipo_producto = tipo_producto

    def inscripcion_bodega(self, bodega:Bodega):
        lista_bodega = []
        lista_bodega.append(bodega.id_bodega)



    def modificar_producto(self):
        pass


