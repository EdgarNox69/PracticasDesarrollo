from flask import Flask, redirect, render_template,request, session, jsonify, url_for
from funciones import *
from login import *
from passlib.hash import sha256_crypt
import os

app = Flask(__name__)
app.secret_key = "Moltr3s_3l_Gu4jolot3_M4cías"
user_in_sesion = "invitado"
@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
def index():
    if user_in_sesion != "invitado":
        return render_template("index.html")
    else:
        return render_template("index.html")
    

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
                        return render_template('index.html',mensaje=msg)
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
            correo = request.form['direccion']
            date = request.form['Birthday']
            password = request.form['password']
            password_cryp = sha256_crypt.hash(password)
            c_usuario = comprobar_usuario()
            if usuario not in c_usuario:
                save_user(p_Nombre, s_nombre, p_Apellido, correo, usuario, password_cryp, date)
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
            

@app.route('/personajes', methods=['GET','POST'])
@app.route('/personajes/', methods=['GET','POST'])
def personajes():
    if request.method =='GET':
        msg = ''

        return render_template('Personajes.html',mensaje=msg)

@app.route('/foros', methods=['GET','POST'])
@app.route('/foros/', methods=['GET','POST'])
def foros():
    if request.method =='GET':
        msg = ''

        return render_template('foros.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            return redirect("/")

@app.route('/menu', methods=['GET','POST'])
@app.route('/menu/', methods=['GET','POST'])
def menu():
    if request.method =='GET':
        msg = ''

        return render_template('menu.html',mensaje=msg)

#Cerrar sesion
@app.route('/logout', methods=['GET'])
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)