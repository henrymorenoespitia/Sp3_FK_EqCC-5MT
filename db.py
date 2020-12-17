import sqlite3
#import var_ent 

def consulta_seleccion(sql):
    try:
        with sqlite3.connect( 'D:\\Escritorio\\application\\application\\tusAccesoriosApp.db') as conexion:
            cur = conexion.cursor()
            sal = cur.execute(sql)
            conexion.commit()
            if sal !=None:
                sal = sal.fetchall()
    except:
        sal = None
    return sal

##################

def consulta_accion(sql, datos):
    try:
        with sqlite3.connect( 'D:\\Escritorio\\application\\application\\tusAccesoriosApp.db') as conexion:
            cur = conexion.cursor()
            sal = cur.execute(sql, datos)
            conexion.commit()
    except:
        sal = None
    return sal