
from flask import Flask, render_template, request
from markupsafe import escape

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
        return f"datos recibidos"


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

