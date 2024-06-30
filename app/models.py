

from app.database import get_db

# en el modelo, se representa a travez de una clase, la entidad en la que queremos trabajar
# Esta capa se encarga de tener las instrucciones que nos permiten conectarnos a la base de datos
class Producto:

    # atributo de clase, para limitar la carga de productos a 8 maximo
    #contador_productos=0   lo utilizamos cuando apliquemos la carga en el front ademas de la vista previa/general


    # metodo que construye la clase producto
    def __init__(self,id_product=None,category=None,name=None,price=None,image=None):
        self.id_product = id_product
        self.category = category
        self.name = name 
        self.price = price
        self.image = image



    @staticmethod
    def get_by_id(id_product):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE id_product = %s", (id_product,))
        row = cursor.fetchone()
        cursor.close()
        if row:   # si encuentra algo, realiza el proceso de convercion a un formato que me  sirva para luego enviarlo como json en views.py: get_todos_productos()
            return Producto(id_product=row[0], category=row[1], name=row[2], price=row[3], image=row[4])
        return None

    # metodo que se conecta con la base de datos y nos trae todo los productos
    @staticmethod
    def get_todo_prod():
        # logica para traer todos los productos SELECT * FROM en la base
        db = get_db() # hace la coneccion a la base de datos
        cursor = db.cursor()  # permite ejecutar instrucciones de sql y obtener los resultados en un formato especifico dentro de flask
        cursor.execute("SELECT * FROM productos")  # en su caso era movies, es el productos del nombre de mi tabla de la base
        rows = cursor.fetchall()  # la consulta devuelve una lista, pero en formato tupla de todos los resultados. Por tanto hay que pasarlo a diccionario/ o sea permite recuperar los valores que se obtienen de la consulta sql
        lista_producto_obtenido = [Producto(id_product=row[0], category=row[1], name=row[2], price=row[3], image=row[4]) for row in rows]
        cursor.close()
        return lista_producto_obtenido   # para probar solamente



    def guardar_base(self):
        # logica para guardar/modificar INSERT/UPDATE en base de datos
        db = get_db()   # optiene la coneccion a la base de datos
        cursor = db.cursor()  # objeto que me permite ejecutar querys
        if self.id_product:   # si existe un id con un valor asignado
            query = """
                UPDATE productos SET category = %s, name = %s, price = %s, image = %s
                WHERE id_product = %s
            """, (self.category, self.name, self.price, self.image, self.id_product)
            cursor.execute(query)
        else:
            cursor.execute("""
                INSERT INTO productos (category, name, price, image) VALUES (%s, %s, %s, %s)
            """, (self.category, self.name, self.price, self.image))
            self.id_product = cursor.lastrowid   # cursor me permite traer la ultima PK que fue insertada
        db.commit()   # confirma para que se guarde
        cursor.close()

    
    def delete_producto(self):
        # logica para borrar DELETE de la base de datos
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id_product = %s", (self.id_product,))
        db.commit()
        cursor.close()
    


    def serialize(self):      # este metodo lo que hace : convertir una instacia o un objeto de la clase Producto a un diccionario de esta forma
        return{
            'id_product':self.id_product,
            'category':self.category,
            'name':self.name,
            'price':self.price,
            'image':self.image,
        }
        

    
