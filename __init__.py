
from application import utils, login

import os
from flask import Flask, render_template, request

#from app import app

from markupsafe import escape
import yagmail as yagmail
from utils import isPasswordValid, isUsernameValid, isEmailValid

from login import formLogin 

#from app.forms import formLogin

app = Flask(__name__)
app.secret_key = os.urandom(24) ## random 24 bits

## error al ejecutar Flask object has no attribute 'error_handler'
##@app.error_handler(404)
##def page_not_found():
##    return "pagina no encontrada" ## render_template('404errorPage.html')

@app.route('/')
@app.route('/index')
def index():
    return "Pagina principal del sitio"


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        flogin = formLogin()
        return render_template('loginFormPy.html',title='inicio', form=flogin)
    elif request.method == 'POST':
        ## Aqui va el codigo correspondiente
        nickname = escape(request.form['usuario'])
        pdw      = escape(request.form['thePassword'])
        retornar = ''
        if not isUsernameValid(nickname):
            retornar = 'Datos erroneos'
        elif not isPasswordValid(pwd):
            retornar = 'Datos erroneos'
         
        ## ---  logica algoritmica --- ##
        # 1. Validar datos que se reciben
        # 2. comprobar existencia de nickname en base de datos
        # 3. comprobar que la contraseña sea la correcta
        # 4. Permitir acceso a la aplicacion a ese usuario (asignar autorizaciones, tokens, session?)
	# 5. Retornar a la pagina de galerias de inventarios.
	return render_template(/inventarios)
        pass

## ruta que: a) lleva al formulario para nuevo usuario (con GET) ; b) transporta desde el Cliente los datos de manera "oculta" hacia el servidor
@app.route('/crearUsuario/', methods=['GET','POST'])
def registro():
    if request.method == 'GET':
        return render_template('crearUsuario.html')
    elif request.method == 'POST':
        nom     = escape(request.form['nombres'])
        apell   = escape(request.form['apellidos'])
        email   = escape(request.form['email'])
        repEm  = escape(request.form['repEmail'])
        activo  = escape(request.form['activo'])
        retornar = ''
        if not isUsernameValid(nom): ## falta validad existencia en DB
            retornar += 'Nombre de usuario no valido\n'
        elif not isEmailValid(email):
            retornar += 'Email no valido\n'
        else:
            retornar = 'Se ha enviado un correo al usuario para confirmar. #Todos los datos estan correctos al validarse\n'
            #yag = yagmail.SMPT('', '') # ajustar datos
            #yag.send(to=email, subject='Confirmar cuenta TusAccApp', contents='Active su cuenta generando su contraseña mediante el siguiente enlace:: <a href=#>...enlace..... </a>')
            retornar = render_template('crearUsuario.html')
       	return retornar
        """  --     Lógica algoritmica     --
        1. validar los datos que vienen desde el formulario del Cliente <--- realizar las funciones en el archivo 'utils.py' de validaciones
        2. Conexion a la base de datos 
        3. Validar existencia del registro en la DB
        4. Insercion en DB Tabla TEMPORAL !!
        5. Enviar correo de confirmacion al usuario.
        6. al recibir la  confirmacion (/confirmarCorreo)-->Insercion en DB tabla Usuarios PERMANENTE !!.
        7. Enviar respuesta al Cliente de exito al crear usuario 
        """
    else: 
        return render_template('crearUsuario.html')

#################################
## Preguntar si maneja algun metodo o si se maneja un token el enlace que llegara al correo??? 
## pregunta: se pasa algun token mediante la url o como se hace ese proceso?
@app.route('/confirmarCorreo/', methods=['GET','POST'])
def confCorreoUsuario():
    if request.method == 'GET':
	return render_template('confirmarYGenerarPwd.html')
    elif request.method == 'POST':
	username = escape(request.form['usuario'])
	pwd      = escape(request.form[''])
	##   --- logica Algoritmica ---
	1. Validar los requisitos de los campos. 
	2. Conexion a la base de datos Temporal.
	3. Trasladar los datos de la base de datos temporal a la definitiva.
	4. Asignar la contraseña en la DB de usuarios (definitiva)
	5. Enviar mensaje de confirmacion al usuario.
	6. Redirigir a la pagina de login
	
	return render_template('/login')

@app.route('/actualizarUsuario', methods=['GET','POST'])
def actUsuario():
    pass
    ## recibir los campos del formulario (ej. /crearUsuario)
    ##   --- logica Algoritmica ---

@app.route('/nuevoAccesorio/', methods=['GET', 'POST'])
def crearAccesorio():
    if request.method == 'GET':
        return render_template('crearAccesorio.html')
    elif request.method == 'POST':
        nombre     = escape(request.form['nombre'])
        codigo     = escape(request.form['codigo'])
        cantidad   = escape(request.form['cantidad'])
        imagen   = escape(request.form['imagen'])
        return render_template('crearAccesorio.html')
	##   --- logica algoritmica ----###

@app.route('/actualizarAccesorio', methods=['GET', 'POST'])
def ActualizarProducto():
    if request.method == 'GET':
        return render_template('actualizarAccesorio.html')
    else:
        nombre     = escape(request.form['nombre'])
        codigo     = escape(request.form['codigo'])
        cantidad   = escape(request.form['cantidad'])
        imagen     = escape(request.form['imagen'])
	# -- logica algoritmica -- 
	# 1. validar cada campo. 			<< cantidades no negativas¿?
	# 2. conexion a la base de datos de accesorios
	# 3. ejecutar la actualizacion de la base de datos.
	# 4. notificar al usuario la respuesta de exito de la actualizacion


        return render_template('actualizarAccesorio.html')
    ##   --- logica Algoritmica ---


## buscar como actualizar con AJAX --
@app.route('/actualizarCantidades', methods=['POST'])
def actCantidades():
    ## recibir los campos del formulario (ej. /crearUsuario)
    referencia  = escape(request.form['referencia'])
    cantidad    = escape(request.form['cantidad'])
    ##   --- logica Algoritmica ---
    # 1. validar los datos.
    # 2. conectar a base de datos.
    # 3. ejecutar las consulta
    # 4. confirmar al usuario el estado de la actualizacion
    pass




## como convertir el tipo de paso de parametro any dentro de la funcion ??
@app.route('/actualizarImagen/<string:imagen>', methods=['GET','POST', 'PUT'])#, 'PUT'
def actImagen(imagen):  ## no string sino 'path'
    return "actualizando imagen"



## como se usa el escape del marupsafe aqui para evitar inyeccion en la url por GET ???
# @app.route('/buscarAccesorio/<string:palabraClaveAccesorio>', methods=['GET'])
@app.route('/inventario/<string:palabraClaveAccesorio>', methods=['GET'])
def galeriaInventario(palabraClaveAccesorio):
    if escape(palabraClaveAccesorio) != None or escape(palabraClaveAccesorio).trim(" ")!= "" :
	## ---  Logica algoritmica  ---
        # consultar en la base de datos la palabra clave ???  cual es la palabra clave de este referencia??
        # recuperar respuesta de la base de datos para alistarla para el cliente.
	# retornar la respuesta al cliente (incluir en el formulario de respuesta ??)
    else:
	##  --- logica algoritmica ---
	# conexion a base de datos
	# Accesorios por defecto a mostrar: definir cuales se van a mostrar en galeria por defecto
	# ejecutar consulta
	# procesay y alistar los datos a enciar
	return render_template('inventario.html')
	return render_template('', escape(palabraClaveAccesorio))
	pass

