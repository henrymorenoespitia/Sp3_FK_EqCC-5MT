import sqlite3
#import var_ent 

def consulta_seleccion(sql):
    try:
        with sqlite3.connect( 'C:\\Users\\henda\\Downloads\\N U E  V  O\\proyectoCiclo03\\application\\tusAccesoriosApp.db') as conexion:
            cur = conexion.cursor()
            sal = cur.execute()
            if sal !=None:
                sal = sal.fetchall()
    except:
        sal = None
    return sal



def consulta_accion():
    pass


#######################

def conectar():
    try:
        sal = sqlite3.connect('C:\\Users\\henda\\Downloads\\N U E  V  O\\proyectoCiclo03\\application\\tusAccesoriosApp.db')
    except:
        sal = None
    return sal

######

def desconectar(conexion):
    try:
        conexion.close()
    finally:
        con=None
    return conexion

##############

def ejecutar_consulta_sele(con, sql):
    try:
        cur = con.cursor()
        sal= cur.execute(sql)
        if sal != None:
            sal = sal.fetchall()
    except:
        sal = None
    return sal
