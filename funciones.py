from passlib.hash import sha256_crypt
import pymysql
    
#'''
class Usuarios():
    def __init__(self, pNombre, sNombre, pApellido, sApellido, correo, usuario, password, date):
        self.pNomnbre = pNombre
        self.sNombre = sNombre
        self.pApellido = pApellido
        self.sApellido = sApellido
        self.correo = correo
        self.usuario = usuario
        self.password = password
        self.date = date
#Cambiar los datos necesarios
def conectarse()->None:
    return pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='2117',
                                db='prueba_bd')

def save_user(pNombre:str, sNombre:str, pApellido:str, sApelldio:str, correo:str, usuario:str, password:str, date:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(primerApellido, segundoNombre, apellidoPaterno, apellidoMaterno, correo, usuario, password, fechaCumpleaños) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (pNombre, sNombre, pApellido, sApelldio, correo, usuario, password, date))
    conexion.commit()
    conexion.close()
    
def get_usuario(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT usuario FROM usuarios WHERE usuario = " + '"' + user_name + '"')
        usuario = cursor.fetchone()
    conexion.close()
    us = usuario.__getitem__(0)
    return us

def comprobar_usuario()->list:
    c_us = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT usuario FROM usuarios")
        c_usuario = cursor.fetchall()
    conexion.close()
    for i in range(len(c_usuario)):
        us = c_usuario.__getitem__(i)
        c_us.append(us.__getitem__(0))
    return c_us

def get_password(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        password = cursor.execute("SELECT password FROM usuarios WHERE usuarios = " + '"' + user_name + '"')
        password = cursor.fetchone()
    conexion.close() 
    for i in range(len(password)):
        pas = password.__getitem__(i)
    return pas 

def actualizar_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor = cursor.execute("UPDATE usuarios SET password =" + '"' + password_cryp + '"' + " WHERE usuario = " + '"' + user_name + '"')
    conexion.commit()
    conexion.close()

def save_peliculas(nombre:str, clasificacion:str, duracion:float, imagen:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO peliculas(nombre, clasificacion, duracion, imagen) VALUES (%s, %s, %s, %s)",
                       (nombre, clasificacion, duracion, imagen))
    conexion.commit()
    conexion.close()

def get_peliculas()->list:
    peliculas = [],[]
    conexion = conectarse()
    with conexion.cursor() as cursor:
        nombre = cursor.execute("SELECT nombre FROM peliculas")
        nombre = cursor.fetchall()
        clasificaion = cursor.execute("SELECT nombre FROM peliculas")
        clasificaion = cursor.fetchall()
        duracion = cursor.execute("SELECT nombre FROM peliculas")
        duracion = cursor.fetchall()
        imagen = cursor.execute("SELECT nombre FROM peliculas")
        imagen = cursor.fetchall()
    conexion.close() 
    for i in range(len(nombre)):
        nom = nombre.__getitem__(i)
        clas = clasificaion.__getitem__(i)
        dura = duracion.__getitem__(i)
        img = imagen.__getitem__(i)
        peliculas[i][0] = nom
        peliculas[i][1] = clas
        peliculas[i][2] = dura
        peliculas[i][3] = img
    return peliculas 

def save_comentarios(usuario:str, comentario:str, post:float, replica:str, fecha:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO comentarios(usuario, comentario, post, replica, fecha) VALUES (%s, %s, %s, %s, %s)",
                       (usuario, comentario, post, replica, fecha))
    conexion.commit()
    conexion.close()

def get_comentarios()->list:
    comentarios = [],[]
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT usuario FROM comentarios")
        usuario = cursor.fetchall()
        comentario = cursor.execute("SELECT comentario FROM comentarios")
        comentario = cursor.fetchall()
        post = cursor.execute("SELECT post FROM comentarios")
        post = cursor.fetchall()
        replica = cursor.execute("SELECT replica FROM comentarios")
        replica = cursor.fetchall()
        fecha = cursor.execute("SELECT fecha FROM comentarios")
        fecha = cursor.fetchall()
    conexion.close() 
    for i in range(len(usuario)):
        us = usuario.__getitem__(i)
        com = comentario.__getitem__(i)
        pos = post.__getitem__(i)
        repl = replica.__getitem__(i)
        fech = fecha.__getitem__(i)
        comentarios[i][0] = us
        comentarios[i][1] = com
        comentarios[i][2] = pos
        comentarios[i][3] = repl
        comentarios[i][4] = fech
    return comentarios 


def save_post(usuario:str, titulo:str, descripcion:float, imagen:str, fecha:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO post(usuario, titulo, descripcion, imagen, fecha) VALUES (%s, %s, %s, %s, %s)",
                       (usuario, titulo, descripcion, imagen, fecha))
    conexion.commit()
    conexion.close()

def get_post(usuario:str, titulo:str)->list:
    comentarios = [],[]
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT usuario FROM comentarios WHERE usuario = " + "'" + usuario + "'" + "and titulo = " + "'" + titulo + "'" )
        usuario = cursor.fetchall()
        comentario = cursor.execute("SELECT comentario FROM comentarios WHERE usuario = " + "'" + usuario + "'" + "and titulo = " + "'" + titulo + "'")
        comentario = cursor.fetchall()
        post = cursor.execute("SELECT post FROM comentarios WHERE usuario = " + "'" + usuario + "'" + "and titulo = " + "'" + titulo + "'")
        post = cursor.fetchall()
        replica = cursor.execute("SELECT replica FROM comentarios WHERE usuario = " + "'" + usuario + "'" + "and titulo = " + "'" + titulo + "'")
        replica = cursor.fetchall()
        fecha = cursor.execute("SELECT fecha FROM comentarios WHERE usuario = " + "'" + usuario + "'" + "and titulo = " + "'" + titulo + "'")
        fecha = cursor.fetchall()
    conexion.close() 
    for i in range(len(usuario)):
        us = usuario.__getitem__(i)
        com = comentario.__getitem__(i)
        pos = post.__getitem__(i)
        repl = replica.__getitem__(i)
        fech = fecha.__getitem__(i)
        comentarios[i][0] = us
        comentarios[i][1] = com
        comentarios[i][2] = pos
        comentarios[i][3] = repl
        comentarios[i][4] = fech
    return comentarios 

def save_quejas(usuario:str, queja:str, fecha:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO queja(usuario, queja, fecha) VALUES (%s, %s, %s)",
                       (usuario, queja, fecha))
    conexion.commit()
    conexion.close()

#Referencia de los get: https://parzibyte.me/blog/2021/03/29/flask-mysql-ejemplo-conexion-crud/
