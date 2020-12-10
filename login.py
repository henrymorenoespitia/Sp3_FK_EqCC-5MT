from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class formLogin(FlaskForm):  # crear una clase que extiende de FlaskForm
    usuario = StringField('Usuario*', validators=[DataRequired(message='El campo es requerido')])
    clave = PasswordField('Contraseña*', validators=[DataRequired(message='El campo es requerido')])
    #recordar = BooleanField('Manteerse conectado*')
    enviar  = SubmitField('Ingresar*')
    ## meter esto dentro de un try except
    

class CrearProducto():
    nombre = StringField('Nombre producto *', validators=[DataRequired(message='Campo requerido')])
    codigo = StringField('Codigo *', validators=[DataRequired(message='Campo requerido')])
    cantidad = StringField('Cantidad *', validators=[DataRequired(message='Campo requerido')])
    imagen = FileField('Imagen *', validators=[DataRequired(message='Campo requerido')])
    enviar = SubmitField('Crear Procuto')  
  
class ActualizarProducto():
    nombre = StringField('Nombre producto *', validators=[DataRequired(message='Campo requerido')])
    codigo = StringField('Codigo *', validators=[DataRequired(message='Campo requerido')])
    cantidad = StringField('Cantidad *', validators=[DataRequired(message='Campo requerido')])
    imagen = FileField('Imagen *', validators=[DataRequired(message='Campo requerido')])
    enviar = SubmitField('Actualizar Procuto')  





