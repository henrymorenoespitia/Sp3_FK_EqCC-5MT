
from flask import Flask, render_template, request
from markupsafe import escape
import yagmail as yagmail
from utils import isPasswordValid, isUsernameValid, isEmailValid


app = Flask(__name__)

## error al ejecutar Flask object has no attribute 'error_handler'
##@app.error_handler(404)
##def page_not_found():
##    return "pagina no encontrada" ## render_template('404errorPage.html')


@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        ## Aqui va el codigo correspondiente
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
        #repEm  = escape(request.form['repEmail'])
        retornar = ''
        if not isUsernameValid(nom): ## falta validad existencia en DB
            retornar += 'Nombre de usuario no valido\n'
        elif not isEmailValid(email):
            retornar += 'Email no valido\n'
        else:
            #retornar = 'Se ha enviado un correo al usuario para confirmar. #Todos los datos estan correctos al validarse\n'
            #yag = yagmail.SMPT('', '') # ajustar datos
            #yag.send(to=ema, subject='Confirmar cuenta TusAccApp', contents='Active su cuenta generando su contraseña mediante el siguiente enlace:: <a href=#>...enlace..... </a>')
            retornar = render_template('crearUsuario.html')
        return retornar

        """ 
        --     Lógica algoritmica     --
        1. validar los datos que vienen desde el formulario del Cliente
        2. Conexion a la base de datos 
        3. Validar existencia del registro en la DB
        4. Insercion en DB Tabla TEMPORAL !!
        5. Enviar correo de confirmacion al usuario.
        6. Insercion en DB tabla Usuarios PERMANENTE !!.
        7. Enviar respuesta al Cliente de exito al crear usuario 
        """
    else: 
        return render_template('crearUsuario.html')


@app.route('/nuevoAccesorio/', methods=['GET', 'POST'])
def crearAccesorio():
    if request.method == 'GET':
        return render_template('crearAccesorio.html')
    elif request.method == 'POST':
        ## Aqui va el codigo correspondiente
        pass

## como se usa el escame del marupsafe aqui para evitar inyeccion en la url por GET ???
@app.route('/buscarAccesorio/<string:palabraClaveAccesorio>', methods=['GET'])
def buscarAccesorio(palabraClaveAccesorio):
   if escape(palabraClaveAccesorio) != None or escape(palabraClaveAccesorio).trim(" ")!= "" :
       return render_template('crearUsuario.html', escape(palabraClaveAccesorio))
   return "no pasa na"
   pass 

## como convertir el tipo de paso de parametro any dentro de la funcion ??
@app.route('/actualizarImagen/<string:imagen>', methods=['GET','POST'])
def actImagen(imagen):
    return "actualizando imagen"


