
from application import utils, login, db
import os
from flask import Flask, render_template, request
#from app import app
from markupsafe import escape
import yagmail as yagmail
from application.utils import isPasswordValid, isUsernameValid, isEmailValid
from application.login import formLogin, CrearUsuario 
from application.db import consulta_accion, consulta_seleccion
#from app.forms import formLogin

app = Flask(__name__)
app.secret_key = os.urandom(24) ## random 24 bits
app.config['UPLOAD_FOLDER'] = './imagenes'

## error al ejecutar Flask object has no attribute 'error_handler'
##@app.error_handler(404)
##def page_not_found():
##    return "pagina no encontrada" ## render_template('404errorPage.html')

@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        flogin = formLogin()
        return render_template('loginFormPy.html',title='inicio', form=flogin, isLogin= 1 )
    elif request.method == 'POST':
        ## Aqui va el codigo correspondiente
        ema = escape(request.form['usuario'])
        pwd = escape(request.form['thePassword'])
        retornar = ''
        if ema == '' or pwd == '':
            retornar = 'Usuario y/o contraseña no validos'
        print(retornar, ema, pwd)
        if retornar == '':
            try:
                sql = f"SELECT estado, clave, user FROM usuarios WHERE email='{ema}'"
                res = consulta_seleccion(sql)
                print(res)
                if res==None or len(res)==0:
                    retornar = 'Usuario o contraseña invalidos'
                else:
                    # Se recupera la clave que proviene de la base de datos
                    clavebd = res[0][1]
                    estadobd = res[0][0]
                    userbd = res[0][2]
                    print('')
                    #if check_password_hash(clavebd,cla):
                    if pwd == clavebd:
                        # Esta modificación obedece a la implementación de borrado lógico
                        if estadobd == 'I':
                            retornar = 'El usuario se encuentra inhabilitado para iniciar sesión'
                        elif estadobd == 'P':
                            retornar = 'El usuario no activado su cuenta'
                        else:
                            session.clear()
                            session['usr_id'] = ema
                            if userbd == 'admi':
                                session['usr_rol']= userbd
                            retornar = 'Acceso concedido'
                            return render_template('inventario.html', title='galeria')                    
                    else:
                        retornar = 'Usuario o contraseña invalidos'
                print(retornar)   
            except:
                print('Error')
                return render_template('loginFormPy.html',title='inicio', form=formLogin(), isLogin= 1 )
        else:
            return render_template('loginFormPy.html',title='inicio', form=formLogin(), isLogin= 1 )  

@app.route('/logout/')
def logout():
    try:
        session.clear()
        return render_template('loginFormPy.html',title='inicio', form=formLogin(), isLogin= 1 )
    except:
        pass
    return print('Error')


@app.route('/galeria/')
def galeria():
    return render_template('inventario.html')

## ruta que: a) lleva al formulario para nuevo usuario (con GET) ; b) transporta desde el Cliente los datos de manera "oculta" hacia el servidor
@app.route('/crearUsuario/', methods=['GET','POST'])
def crearUsuario():
#        """  --     Lógica algoritmica     --
#   1. Atender los métodos del formulario
    #try:
        if request.method == 'GET':
            inst = CrearUsuario()
            return render_template('crearUsuario.html',form = inst, isLogin=0)
        elif request.method == 'POST':
#   2. Recuperar los datos del formulario
            name = escape(request.form['name'])
            lname = escape(request.form['lname'])
            ema = escape(request.form['ema'])
            repEma = escape(request.form['repEma'])

#   3. Validar del lado del servidor
            retornar = ''
            if not isUsernameValid(name):
                retornar += 'Nombre de usuario no valido\n'
            elif not isEmailValid(ema):
                retornar += 'E-mail no valido\n'
            elif ema != repEma:
                retornar = 'Los E-Mails no coinciden'
            else:               
#   4. Comprobar en base de datos
                query = f"SELECT estado FROM usuarios where email = '{ema}'"
                res = consulta_seleccion(query)
#   5. Inserción en DB, estado 'P'
                if res == None or len(res)==0:
                    query = "INSERT INTO usuarios (nombres, apellidos, email, estado) VALUES (?,?,?,?)"
                    res = consulta_accion(query,(name, lname, ema, 'P'))
                    if res != None:
                        ### Buscar la forma de hacer el efecto "pop up" en los diseños
                        #retornar = 'Datos registrados con éxito, se envió un correo de verificación'
#   6. Enviar correo de verificación
#   7. Al recibir confirmación, cambiar estado a 'A'
                    #IsVerificado = true
                        retornar = 'Usuario Confirmado'
                        query = "UPDATE usuarios SET estado = 'A' WHERE email=(?)"
                        res = consulta_accion(query, ema)
                else:
                    retornar = 'No se pueden registrar usuarios con el mismo E-Mail'
#   8. Enviar respuesta al cliente de éxito al crear un usuario
                        
        else: 
            inst = CrearUsuario()
            return render_template('crearUsuario.html',form = inst, isLogin=0)
    #except:
        #retornar = 'Error'

        return retornar


#        """  --     Lógica algoritmica     --
#        1. validar los datos que vienen desde el formulario del Cliente <--- realizar las funciones en el archivo 'utils.py' de validaciones
#        3. Validar existencia del registro en la DB
#        4. Insercion en DB, estado 'P'
#        5. Enviar correo de confirmacion al usuario.
                    #yag = yagmail.SMPT('', '') # ajustar datos
                    #yag.send(to=email, subject='Confirmar cuenta TusAccApp', contents='Active su cuenta generando su contraseña mediante el siguiente enlace:: <a href=#>...enlace..... </a>')
                    #retornar = render_template('crearUsuario.html', isLogin = 0)
                    #retornar = f"usuario {nom} email {email}"
#        6. al recibir la  confirmacion (/confirmarCorreo)-->Cambiar estado a 'A'.
#        7. Enviar respuesta al Cliente de exito al crear usuario 
#        """


#################################
## Preguntar si maneja algun metodo o si se maneja un token el enlace que llegara al correo??? 
## pregunta: se pasa algun token mediante la url o como se hace ese proceso?
@app.route('/confirmarCorreo/', methods=['GET','POST'])
def confCorreoUsuario():
    if request.method == 'GET':
        return render_template('confirmarYGenerarPwd.html')
    elif request.method == 'POST':
        username = escape(request.form['usuario'])
        pwd= escape(request.form['thePassword'])
	##   --- logica Algoritmica ---
	#1. Validar los requisitos de los campos. 
	#2. Conexion a la base de datos Temporal.
	#3. Trasladar los datos de la base de datos temporal a la definitiva.
	#4. Asignar la contraseña en la DB de usuarios (definitiva)
	#5. Enviar mensaje de confirmacion al usuario.
	#6. Redirigir a la pagina de login
        return render_template('/login')

@app.route('/recuperarContrasena', methods=['GET', 'POST'])
def recupPwd():
    if request.method == 'GET':
        flogin = formLogin()
        return render_template('recuperarPwd.html',title='inicio', form=flogin)
    elif request.method == 'POST':
        usuario = escape(request.form['usuario'])
        retornar = ''
        if usuario.trim == "":
            retornar = 'campo de contraseña no diligenciado !'
        ## --- logica algoritmica ---
        # 1. validar campo usuario
        # 2. conectar base de datos
        # 3. comprobar que exista en la base de datos
        # 4. enviar enlace de generar nueva contraseña al email registrado en DB 

##   by Admin
@app.route('/actualizarUsuario/<string:accion>', methods=['GET','POST'])
def actualizarUsuario(accion):
    if request.method == 'GET':
        print(f"accion es ::  {accion}")
        isEliminar = False
        if accion == "eliminar":
            isEliminar = True
        print(f"accion es ::  {accion}")
        return render_template('actualizarUsuario.html', ACCION = isEliminar, isLogin = 0)
    elif request.method == 'POST':
        # usuario = escape(request.form['nickname'])
        ##   ---- logica algotitmica   ---- 
        ## buscar en la base de datos el nombre de las personas
        ## retornar la plantilla con los datos del empleado
        
        return render_template('actualizarUsuario.html', datos= Null, ACCION = isEliminar)  # datos para rellenar el formulario
        #                                                                                     # accion = "acctualizar" mas no "eliminar"
@app.route('/actualizandoUsuario/', methods=['POST'])
def actndoUsu():
    if request.method == 'POST':
        print("estoy aqui procesando POST")
        nom     = escape(request.form['nombres'])
        apell   = escape(request.form['apellidos'])
        email   = escape(request.form['email'])
        repEm  = escape(request.form['repEmail'])
        #activo  = escape(request.form['activo'])
        retornar = ''
        if not isUsernameValid(nom): ## falta validad existencia en DB
            retornar += 'Nombre de usuario no valido\n'
        elif not isEmailValid(email):
            retornar += 'Email no valido\n'
        else:
            retornar = 'Usuario actualizado con exito\n'
            #yag = yagmail.SMPT('', '') # ajustar datos
            #yag.send(to=email, subject='Confirmar cuenta TusAccApp', contents='Active su cuenta generando su contraseña mediante el siguiente enlace:: <a href=#>...enlace..... </a>')
            retornar = render_template('crearUsuario.html', isLogin = 0)
            #retornar = f"usuario {nom} email {email}"
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

@app.route('/eliminandoUsuario')
def eliminandoUsuario():
   pass

@app.route('/nuevoAccesorio', methods=['GET', 'POST'])
def crearAccesorio():
    if request.method == 'GET':
        
        return render_template('crearProducto.html')
    elif request.method == 'POST':
        nombre      = escape(request.form['nombre'])
        precio      = escape(request.form['precio'])
        codigo      = escape(request.form['referencia'])
        cantidad    = escape(request.form['cantidad'])
        uploaded_file = request.files['archivo']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
            imagen_string =  base64.b64encode(uploaded_file.read())
                
        flash("Productoagregado con Exito")
        sql = f"INSERT INTO accesorios (nombre, referencia, existencias, precio, imagen) VALUES('{nombre}','{codigo}','{cantidad}','{precio}','{uploaded_file.filename}')"
        consulta_seleccion(sql)
        print(nombre)
        return render_template('crearProducto.html')
        

@app.route('/actualizarAccesorio/<string:accion>', methods=['GET', 'POST'])
def ActualizarProducto(accion):
    if request.method == 'GET':
        isEliminar= False
        if accion == 'eliminar':
            isEliminar = True
        return render_template('actualizarProducto.html', isLogin=0, ACCION= isEliminar)
    elif request.method == 'POST':
        # Este post viene despues de darle click en la imagen de inventarios. R
        
        nombre = escape(request.form['nombre'])
        codigo = escape(request.form['referencia'])
        # validar datos (caracteres html)
        # Realizar una busqueda en base de datos

@app.route('/actualizandoAccesorio', methods=['POST'])
def actzndoAcc():
    if request.method == 'POST':
        nombre     = escape(request.form['nombre'])
        codigo     = escape(request.form['referencia'])
        cantidad   = escape(request.form['cantidad'])
        #imagen     = escape(request.form['imagen'])
        print(nombre)
        
        retornar = ''
        nombre.string
        #if nombre.string == "":
        #    retornar += 'no se permite nombre vacio'
        # -- logica algoritmica -- 
        # 1. validar cada campo. 			<< cantidades no negativas¿?
        # 2. conexion a la base de datos de accesorios
        # 3. ejecutar la actualizacion de la base de datos.
        # 4. notificar al usuario la respuesta de exito de la actualizacion

        return render_template('actualizarProducto.html')



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
        pass
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
    pass

