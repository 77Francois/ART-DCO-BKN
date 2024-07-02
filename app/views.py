from flask import jsonify, request
from app.models import Producto  #este es para importar lo que tiene models por conectarse con la base de datos



# mis funciones de art/dec

# funcion que busca todos los productos listados
def get_todos_productos():   # de la clase Producto ejecutame get_todo_prod() de models.py que se conecta a la base de datos y me busca todos los productos que estan en ella
    producto_obtenido = Producto.get_todo_prod()  # usa la funcion de models: get_todo_prod() para traer todos los productos de la base
    lista_product = [producto.serialize() for producto in producto_obtenido]   # recorro el resultado que obtuve en products y convierto el objeto a un diccionario
    return jsonify(lista_product)  


# funcion que busca un producto
def get_producto(id_product):
    prod = Producto.get_by_id(id_product)
    if not prod:
        return jsonify({'message': 'Producto no encontrado'}), 404
    return jsonify(prod.serialize())   



# funcion para crear los productos
# def create_producto():
#     data = request.json # request recibio los datos del cliente en formato json y los guardo en la variable 
#     # necesitamos agregar validaciones
#     new_producto = Producto(None,data['category'],data['name'],data['price'],data['image'])  # llamo al constructor de la clase Producto y completo  los parametros con los valores que estoy recibiendo de la solicitud request.json
#     new_producto.guardar_base() # llamo a ejecutar el metodo guardar_base() de models.py
#     return jsonify({'message':'Producto generado exitosamente'}), 201




# funcion para crear los productos
def create_producto():
    data = request.json # request (esta en el from arriba) recibio los datos del cliente en formato json y los guardo en la variable 
    # necesitamos agregar validaciones
    new_producto = Producto(None,data['category'],data['name'],data['price'],data['image'])  # llamo al constructor de la clase Producto y completo  los parametros con los valores que estoy recibiendo de la solicitud request.json
    new_producto.guardar_base() # llamo a ejecutar el metodo guardar_base() de models.py
    return jsonify({'message':'Producto generado exitosamente'}), 201

# función para crear los productos
# def create_producto():
#     try:
#         data = request.json  # request (está en el from arriba) recibió los datos del cliente en formato json y los guardo en la variable 

#         # Validaciones básicas
#         if not all(key in data for key in ('category', 'name', 'price', 'image')):
#             return jsonify({'message': 'Faltan datos necesarios'}), 400

#         if not isinstance(data['price'], (int, float)):
#             return jsonify({'message': 'El precio debe ser un número'}), 400

#         new_producto = Producto(None, data['category'], data['name'], data['price'], data['image'])  # llamo al constructor de la clase Producto y completo los parámetros con los valores que estoy recibiendo de la solicitud request.json
#         new_producto.guardar_base()  # llamo a ejecutar el método guardar_base() de models.py

#         return jsonify({'message': 'Producto generado exitosamente', 'product': new_producto.serialize()}), 201

#     except Exception as e:
#         return jsonify({'message': 'Error al crear el producto', 'error': str(e)}), 500







# funcion para actualizar productos
def update_producto(id_product):
    prod = Producto.get_by_id(id_product)
    if not prod:
        return jsonify({'message': 'Producto inexistente'}), 404
    data = request.json
    prod.category = data['category']
    prod.name = data['name']
    prod.price = data['price']
    prod.image = data['image']
    prod.guardar_base()
    return jsonify({'message': 'Producto actualizado'})


# funcion para borrar un producto
# def delete_producto(id_product):
#     prod = Producto.get_by_id(id_product)
#     if not prod:
#         return jsonify({'message': 'Producto inexistente'}), 404
#     prod.delete_producto()
#     return jsonify({'message': 'Producto eliminado'})  se cambio por nuestro codigo

def delete_producto(id_product):
    try:
        prod = Producto.get_by_id(id_product)
        if not prod:
            return jsonify({'message': 'Producto inexistente'}), 404
        prod.delete_producto()
        return jsonify({'message': 'Producto eliminado exitosamente', 'id_product': id_product})
    except Exception as e:
        return jsonify({'message': 'Error al eliminar el producto', 'error': str(e)}), 500


