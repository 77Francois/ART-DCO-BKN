# aca pongo la ruta que quiero que atienda que archivo

from flask import Flask
from app.database import init_app
from app.views import *    #index, saludar   importo la funcion index desde el archivo views y la funcion saludar
from flask_cors import CORS



# voy a crear una instancia de Flask, que es la clase que importe primero

app = Flask(__name__)  # __name__ es una variable especial de python 

init_app(app)  # para que se ejecute la funcion que inicializa el uso de la aplicacion de la base de datos

# habilitamos que acepte solicitudes de cualquier origen, jamas hacer en ambito de produccion
CORS(app)


# hago la asociacion de rutas con las vistas usando .route 

# app.route('/helloworld',methods=['GET'])(index)  si te llega la ruta '/helloworld', le defino el tipo de metodo http quiero que use 'GET' y entre parentesis (index) que vista quiero que se asocie a la ruta
# se lee: si a mi servidor le llega la solicitud por medio de la ruta helloworld y que se la solicitud sea del tipo GET, que el backend ejecute el metodo index

# app.route('/',methods=['GET'])(index)

app.route('/api/productos/', methods=['GET'])(get_todos_productos)    # get_todos_productos es la funcion definida en views.py
app.route('api/productos/<int:id_product>', methods=['GET'])(get_producto)   # ruta hasta funciones en views.py
app.route('/api/productos/', methods=['POST'])(create_producto)
app.route('api/productos/<int:id_product>', methods=['PUT'])(update_producto)   # ruta hasta funciones en views.py
app.route('api/productos/<int:id_product>', methods=['DELETE'])(delete_producto)  # ruta hasta funciones en views.py



# ACA VAN LOS METODOS PARA BORRAR, EDITAR, CONSULTAR, ETC

# servidor de desarrollo



# permite separar el codigo que se ejecuta cuando se corre el archivo
if __name__=='__main__':  # me permite definir que es lo quiero que se ejecute dentro de mi archivo python cuando yo ejecute este archivo
    app.run(debug=True)
