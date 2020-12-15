import sqlite3
import var_ent

def consulta_seleccion(sql):
    try:
        with sqlite3.connect( var_ent.DB_TusAccApp ) as conexion:
            cur = conexion.cursor()
            sal = cur.execute()
            if sal !=None:
                sal = sal.fetchall()
    except:
        sal = None
    return sal



def consulta_accion():
    pass


def desconectar(conexion):
    try:
        conexion.close()
    finally:
        con=None
    return conexion

#######################

def ejecutar_consulta(con, sql):
    try:
        cur= con.execute(sql).fetchall()
    except ex:
        sal = None
    return sal
