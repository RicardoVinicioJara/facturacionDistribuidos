import pymysql
db = pymysql.connect("localhost", "root", "", "facturaciondistribuidos")

 

class Producto:
    def __init__(self, id, nombre, precio, stock, codigo, descuento, eliminado):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.codigo = codigo
        self.descuento = descuento
        self.eliminado = eliminado



    def Imprimir(self):
        mensaje = ('Producto: \n id = ' + str(self.id) + '\n nombre = ' + self.nombre + '\n precio = ' + self.precio
                   + '\n stock = ' + self.stock + '\n descuento = ' + self.descuento+'\n codigo = ' + self.codigo)
        return (mensaje)


class ControladorProducto:
    def __init__(self, db):
            self.db = db

    def ingresar(self, Producto):
        try:
            pro = Producto
            cur = self.db.cursor()
            cur.execute('INSERT INTO producto (nombre, precio, stock, codigo, descuento, eliminado) VALUES (%s, %s, %s, %s, %s, %s)',
                        (pro.nombre,  pro.precio, pro.stock, pro.codigo, pro.descuento, pro.eliminado))
            self.db.commit()
            cur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def actualizar(self, Producto):
        try:
            pro = Producto
            cur = self.db.cursor()
            cur.execute("""
                UPDATE producto
                SET nombre = %s,
                    precio = %s,
                    stock = %s,
                    codigo = %s,
                    descuento = %s,
                    eliminado = %s
                WHERE id = %s
            """, (pro.nombre, pro.precio, pro.stock, pro.codigo,pro.descuento, pro.eliminado, pro.id))
            self.db.commit()
            cur.close()
            return True
        except Exception as e:
            print(str(e) + " eroror ")
            return False

    def listar(self):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM producto where eliminado <> 1')
        data = cur.fetchall()
        cur.close()
        return data

    def listarBusca(self, cedula):
        cur = db.cursor()
        cur.execute("SELECT * FROM producto WHERE eliminado <> 1 and id =  %s  or eliminado <> 1 and nombre like %s  or eliminado <> 1 and codigo like %s", (cedula, '%'+cedula+'%', '%'+cedula+'%')  )
        data = cur.fetchall()
        
        return data

    def eliminar(self, id):
        try:
            cur = self.db.cursor()
            cur.execute(
                'UPDATE `producto` SET `eliminado` = 1 WHERE `producto`.`id` = ' + id)
            self.db.commit()
            cur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def buscarProducto(self, id):
        cur = self.db.cursor()
        cur.execute(
            'SELECT * FROM producto WHERE eliminado <> 1 and id = %s', (id))
        data = cur.fetchall()
        cur.close()
        return data[0]

    def buscarProductoCodigo(self, id):
        cur = self.db.cursor()
        cur.execute(
            'SELECT * FROM producto WHERE eliminado <> 1 and codigo = %s', (id))
        data = cur.fetchall()
        cur.close()
        return data[0]


if __name__ == "__main__":
    pro = Producto(0, "nombre", "precio", 'stock', "codigo", "descuento", False)
    print(pro.Imprimir())

    con = ControladorProducto()
    