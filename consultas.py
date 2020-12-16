from db import consulta_seleccion, consulta_accion

datos = ('henry', 'moreno', 'A', '2henrymoreno@gmail.com', '2henrymoreno', 'Aa1234567' ) ## tupla o lista
sentencia =  '''INSERT INTO usuarios (nombres, apellidos, estado, email, nickname, clave) VALUES(?,?,?,?,?,?) ;'''
consulta_accion(sentencia, datos)

print(consulta_seleccion("SELECT nombres, apellidos, nickname, email, clave, estado FROM usuarios"    ))