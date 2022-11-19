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
                                db='bd_practica')

def save_user(pNombre:str, sNombre:str, pApellido:str, sApelldio:str, correo:str, usuario:str, password:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(primerNombre, segundoNombre, apellidoPaterno, apellidoMaterno, correo, usuario, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (pNombre, sNombre, pApellido, sApelldio, correo, usuario, password))
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

def get_datos_usuario(user_name:str)->dict:
    datosU = [],[]
    conexion = conectarse()
    with conexion.cursor() as cursor:
        primerNombre = cursor.execute("SELECT primerNombre FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        primerNombre = cursor.fetchone()
        segundoNombre = cursor.execute("SELECT segundoNombre FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        segundoNombre = cursor.fetchone()
        apellidoPaterno = cursor.execute("SELECT apellidoPaterno FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        apellidoPaterno = cursor.fetchone()
        apellidoMaterno = cursor.execute("SELECT apellidoMaterno FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        apellidoMaterno = cursor.fetchone()
        correo = cursor.execute("SELECT correo FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        correo = cursor.fetchone()
        usuario = cursor.execute("SELECT usuario FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        usuario = cursor.fetchone()
        contraseña = cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        contraseña = cursor.fetchone()
    conexion.close()
    pn = primerNombre.__getitem__(0)
    sn = segundoNombre.__getitem__(0)
    ap = apellidoPaterno.__getitem__(0)
    am = apellidoMaterno.__getitem__(0)
    c = correo.__getitem__(0)
    us = usuario.__getitem__(0)
    con = contraseña.__getitem__(0)
    datosU[0][0] = pn
    datosU[0][1] = sn
    datosU[0][2] = ap
    datosU[0][3] = am
    datosU[0][4] = c
    datosU[0][5] = us
    datosU[0][6] = con
    return datosU

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
        password = cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = " + "'" + user_name + "'")
        password = cursor.fetchone()
    conexion.close() 
    for i in range(len(password)):
        pas = password.__getitem__(i)
    print(pas)
    return pas 
get_password("Prueba")
def actualizar_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor = cursor.execute("UPDATE usuarios SET contraseña =" + "'" + password_cryp + "'" + " WHERE usuario = " + "'" + user_name + "'")
    conexion.commit()
    conexion.close()

def save_peliculas(nombre:str, clasificacion:str, duracion:float, imagen:str, sinopsis:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO peliculas(nombre, clasificacion, duracion, imagen, sonopsis) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, clasificacion, duracion, imagen, sinopsis))
    conexion.commit()
    conexion.close()

def get_pelicula(nPelicula:str)->list:
    peliculas = [],[]
    conexion = conectarse()
    with conexion.cursor() as cursor:
        nombre = cursor.execute("SELECT nombre FROM peliculas WHERE nombre = '" + nPelicula + "'")
        nombre = cursor.fetchone()
        clasificaion = cursor.execute("SELECT clasificacion FROM peliculas WHERE nombre = '" + nPelicula + "'")
        clasificaion = cursor.fetchone()
        duracion = cursor.execute("SELECT duracion FROM peliculas WHERE nombre = '" + nPelicula + "'")
        duracion = cursor.fetchone()
        imagen = cursor.execute("SELECT imagen FROM peliculas WHERE nombre = '" + nPelicula + "'")
        imagen = cursor.fetchone()
    conexion.close() 
    for i in range(len(nombre)):
        nom = nombre.__getitem__(i)
        clas = clasificaion.__getitem__(i)
        dura = duracion.__getitem__(i)
        img = imagen.__getitem__(i)
    peliculas[0][0] = nom
    peliculas[0][1] = clas
    peliculas[0][2] = dura
    peliculas[0][3] = img
    return peliculas 

def get_peliculas()->list:
    peliculas = [],[]
    conexion = conectarse()
    with conexion.cursor() as cursor:
        nombre = cursor.execute("SELECT nombre FROM peliculas")
        nombre = cursor.fetchall()
        clasificaion = cursor.execute("SELECT clasificacion FROM peliculas")
        clasificaion = cursor.fetchall()
        duracion = cursor.execute("SELECT duracion FROM peliculas")
        duracion = cursor.fetchall()
        imagen = cursor.execute("SELECT imagen FROM peliculas")
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

def save_post(usuario:str, titulo:str, descripcion:float, fecha:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO post(usuario, titulo, comentario, fecha) VALUES (%s, %s, %s, %s)",
                       (usuario, titulo, descripcion, fecha))
    conexion.commit()
    conexion.close()

def get_post()->list:
    comentarios = [],[]
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT usuario FROM comentarios " )
        usuario = cursor.fetchall()
        comentario = cursor.execute("SELECT comentario FROM comentarios ")
        comentario = cursor.fetchall()
        post = cursor.execute("SELECT post FROM comentarios ")
        post = cursor.fetchall()
        replica = cursor.execute("SELECT replica FROM comentarios ")
        replica = cursor.fetchall()
        fecha = cursor.execute("SELECT fecha FROM comentarios ")
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
    
def get_quejas()->list:
    quejas = [],[]
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT usuario FROM quejas" )
        usuario = cursor.fetchall()
        queja = cursor.execute("SELECT queja FROM quejas")
        queja = cursor.fetchall()
        fecha = cursor.execute("SELECT fecha FROM quejas")
        fecha = cursor.fetchall()
    conexion.close() 
    for i in range(len(usuario)):
        us = usuario.__getitem__(i)
        quej = queja.__getitem__(i)
        fech = fecha.__getitem__(i)
        quejas[i][0] = us
        quejas[i][1] = quej
        quejas[i][2] = fech
    return quejas 

#Referencia de los get: https://parzibyte.me/blog/2021/03/29/flask-mysql-ejemplo-conexion-crud/
