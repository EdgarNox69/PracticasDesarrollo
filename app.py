from flask import *
from funciones import get_peliculas, get_usuario, comprobar_usuario, get_password, save_user, actualizar_password, get_datos_usuario, get_pelicula, get_quejas, save_quejas, get_post, save_post
from login import *
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "Moltr3s_3l_Gu4jolot3_M4cías"
user_in_sesion = "invitado"
@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
def index():
    pelis = get_peliculas()
    if user_in_sesion != "invitado":
        return render_template("index.html", peliculas = pelis)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
    else:
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
                    user_in_sesion = user
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

@app.route('/restart_password', methods=['GET','POST'])
@app.route('/restart_password/', methods=['GET','POST'])
def restart_password():
    if request.method == 'GET':
        msg = ''
        return render_template('restart_password.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            password = request.form['password']
            c_us = comprobar_usuario()
            if usuario not in c_us:
                return redirect("/new_user")
            else:
                actualizar_password(usuario, password)
                return redirect("/")
            
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
                save_pelicula(nombre, clasificaion, duracion, img, sinopsis)
                return redirect('/')
            
@app.route('/pelicula', methods=['GET','POST'])
@app.route('/pelicula/<nombre>', methods=['GET','POST'])
def pelicula():
    if request.method == 'GET':
        msg = ''
        return render_template('save_Peliculas.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            nombre = request.form['nombre']
            peli = get_pelicula()
            return render_template('/pelicula.html', pelicula = peli)

@app.route('/perfil', methods=['GET','POST'])
@app.route('/perfil/<usuario>', methods=['GET','POST'])
def usuario():
    if request.method == 'GET':
        msg = ''
        usuario = get_datos_usuario(user_in_sesion)
        return render_template('perfil.html', datos = usuario)
        
@app.route('/foro', methods=['GET','POST'])
@app.route('/foro/', methods=['GET','POST'])
def foro():
    if request.method == 'GET':
        msg = ''
        pos = get_post()
        return render_template('foro.html', post = pos)
        
@app.route('/quejas', methods=['GET','POST'])
@app.route('/quejas/', methods=['GET','POST'])
def quejas():
    if request.method == 'GET':
        quejaa = get_quejas()
        return render_template('quejas.html', quejas = quejaa)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            queja = request.form['queja']
            save_quejas(usuario, queja)
            quejaa = get_quejas()
            return render_template('quejas.html', quejas = quejaa)

#Cerrar sesion
@app.route('/logout', methods=['GET'])
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)