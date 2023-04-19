import datetime


class Cuenta(object):

    def __init__(self, monto_inicio=0, numero_de_cuenta=0):  # contructor, siempre de la misma forma
        self.cantidad = monto_inicio
        self.numero_de_cuenta = numero_de_cuenta
        self.movimientos = []
        self.activa = True

    
    def crear_movimiento(self, descripcion, monto):
        movimiento = MovimientoCuenta(descripcion, monto)
        self.movimientos.append(movimiento)

    def __str__(self):
        # TODO: Completar para que quede mejor con nro de cuenta
        print(f"CUENTA comun {self.cantidad}")

class MovimientoCuenta(object):

    def __init__(self, descripcion, monto_del_movimiento):
        self.fecha_y_hora = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento

    def __str__(self):
        # Completar como pide el ejercicio 3)
        return f"{self.fecha_y_hora} {self.descripcion} {self.monto}"