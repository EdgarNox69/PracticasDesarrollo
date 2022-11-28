from flask import*
from funciones import *
from login import *
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "Moltr3s_3l_Gu4jolot3_M4cías"
user_in_sesion = 'Prueba'
@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
@app.route("/")
def index():
    pelis = get_peliculas()
    
    if request.method == 'GET':
        return render_template("index.html", peliculas = pelis)
    

@app.route('/login', methods=['GET','POST'])
@app.route('/login/', methods=['GET','POST'])
def login():
#"""
    if request.method == 'GET':
        msg = ''
        return render_template('login.html',mensaje=msg)
    else:
        if request.method == 'POST':
            usuario = request.form['usuario']
            user = get_usuario(usuario)
            c_usuario = comprobar_usuario()
            
            if usuario not in c_usuario:
                return redirect('/new_user')
            else:
                if usuario == user:
                    password_db = get_password(usuario) # password guardado
                    password_forma = request.form['password'] #password presentado
                    verificado = sha256_crypt.verify(password_forma,password_db)
                    user_in_sesion = usuario
                    if (verificado == True):
                        session['usuario'] = usuario
                        session['logged_in'] = True
                        incio(user_in_sesion)
                        if 'ruta' in session:
                            ruta = session['ruta']
                            session['ruta'] = None
                            return redirect(ruta)
                        else:
                            return redirect("/")
                    else:
                        msg = f'El password de {usuario} no corresponde'
                        return render_template('/login.html',mensaje=msg)
#"""

@app.route('/new_user', methods=['GET','POST'])
@app.route('/new_user/', methods=['GET','POST'])
def new_user():
    if request.method == 'GET':
        msg = ''
        return render_template('new_user.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            p_Nombre  = request.form['pnombre']
            s_nombre  = request.form['snombre']
            p_Apellido  = request.form['papellido']
            s_Apellido  = request.form['sapellido']
            correo = request.form['correo']
            password = request.form['contraseña']
            password_cryp = sha256_crypt.hash(password)
            c_usuario = comprobar_usuario()
            if usuario not in c_usuario:
                save_user(p_Nombre, s_nombre, p_Apellido, s_Apellido, correo, usuario, password_cryp)
            return redirect('/login')
         
@app.route('/save_pelicula', methods=['GET','POST'])
@app.route('/save_pelicula/', methods=['GET','POST'])
def save_pelicula():
    if request.method == 'GET':
        msg = ''
        return render_template('/save_Peliculas.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['Enviar']
        if valor == 'Enviar':
            nombre = request.form['nombre']
            clasificaion = request.form['clasificacion']
            duracion = request.form['duracion']
            img = request.form['imagen']
            sinopsis  = request.form['sinopsis']
            c_pelicula = get_peliculas()
            if nombre not in c_pelicula:
                save_peliculas(nombre, clasificaion, duracion, img, sinopsis)
            return redirect('/')
            
@app.route('/perfil', methods=['GET','POST'])
@app.route('/perfil/', methods=['GET','POST'])
def usuario():
    if request.method == 'GET':
        us = get_datos_usuario(user_in_sesion)
        return render_template('perfil.html', datos = us)
        
@app.route('/quejas', methods=['GET','POST'])
@app.route('/quejas/', methods=['GET','POST'])
def quejas():
    if request.method == 'GET':
        quejaa = get_quejas()
        return render_template('quejas.html', quejas = quejaa)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            queja = request.form['queja']
            save_quejas(user_in_sesion, queja)
            quejaa = get_quejas()
            return render_template('quejas.html', quejas = quejaa)

@app.route('/foro', methods=['GET','POST'])
@app.route('/foro/', methods=['GET','POST'])
def foro():
    pos = get_post()
    if request.method == 'GET':
        return render_template('foro.html', posts = pos)
    if request.method == 'POST':
        valor = request.form['publicar']
        if valor == 'Publicar':
            titulo = request.form['titulo']
            queja = request.form['comentario']
            save_post(user_in_sesion, titulo, queja)
            return render_template('foro.html', posts = pos)

#Cerrar sesion
@app.route('/logout', methods=['GET'])
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)