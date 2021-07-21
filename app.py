from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///nenis.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#Esquema de usuarios
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(50), unique=True, nullable=False)
    contrasenia = db.Column(db.String(80), nullable=False)

@app.route("/")
def index():
    return render_template("index.html")

#Ruta serach para buscar un usuario por id
@app.route("/search")
def search():
    id_usuario = request.args.get("id")
    #podemos realizar una consulta
    usuario = Usuarios.query.filter_by(id=id_usuario).first()
    if usuario:
        return usuario.nombre
    return "The user doesn't exist." # por query params /search?id=1 for example

#Ruta signup para registrar usuario
@app.route("/signUp.html", methods=["GET", "POST"])   
def signup():
    if request.method == "POST":
        hashed_pw = generate_password_hash(request.form["password"], method="sha256")
        nuevo_usuario = Usuarios(nombre=request.form["NickName"], telefono=request.form["phone"], correo=request.form["email"], contrasenia=hashed_pw)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("signUp.html")

#Ruta login para loguear usuario
@app.route("/login.html", methods=["GET", "POST"])   
def login():
    if request.method == "POST":
        usuario = Usuarios.query.filter_by(correo=request.form["email"]).first()
        if usuario and check_password_hash(usuario.contrasenia, request.form["password"]):
            return render_template("index.html")
        return "Your credentials are invalid, check and try again."
    return  render_template("login.html")

#Ruta Novedades
@app.route("/novedades.html")   
def novedades():
    return  render_template("novedades.html")

#Ruta accesorios
@app.route("/accesorios.html")   
def accesorios():
    return  render_template("accesorios.html")

#Ruta Hogar
@app.route("/hogar.html")   
def hogar():
    return  render_template("hogar.html")

#Ruta updateDelete
@app.route("/updateDelete.html")   
def updateDelete():
    return  render_template("updateDelete.html")

#Ruta vestidos
@app.route("/vestidos.html")   
def vestidos():
    return  render_template("vestidos.html")

#Ruta zapatos
@app.route("/zapatos.html")   
def zapatos():
    return  render_template("zapatos.html")

#Ruta eliminar para loguear usuario
@app.route('/delete/<id>')
def delete(id):
    Usuarios.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('usuarios'))

#Ruta editar usuario
@app.route('/update', methods = ['GET', 'POST'])
def update():
    #return request.form
    if request.method == 'POST':
        datos_nuevos = Usuarios.query.get(request.form.get('id'))
        datos_nuevos.nombre = request.form['nombre']
        datos_nuevos.telefono = request.form['telefono']
        datos_nuevos.correo = request.form['correo']
        db.session.commit()
        return redirect(url_for('usuarios'))
    return redirect(url_for('usuarios'))

#Ruta usuarios
@app.route('/usuarios.html')
def usuarios():
    usuario = Usuarios.query.all()
    return  render_template("usuarios.html", lista_usuarios=usuario)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)