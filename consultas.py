from db import conectar, ejecutar_consulta_sele, desconectar

con = conectar()
if con != None:
    sentencia = "SELECT nombres, apellidos, nickname, clave, estado FROM usuarios"    
    res = ejecutar_consulta_sele(con, sentencia)
    if res != None:
        for fila in res:
            print(fila)
        #print("hola estoy aqui recuperando registros")
    else:
        print("No se selecciono ningun registro")
    desconectar(con)
else:
    print("error al conectarse a la base de datos")