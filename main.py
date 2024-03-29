from flask import Flask,render_template,request, flash, g
from flask_wtf.csrf import CSRFProtect
import forms

app=Flask(__name__)
app.secret_key='esta es mi clave secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre = 'Mario'
    print("before 1")
    
@app.after_request
def after_request(response):
    print("after 3")
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    print("alumno {}".format(g.nombre))
    nom = ''
    apa = ''
    ama = ''
    alumno_clase = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clase.validate():
        nom = alumno_clase.nombre.data
        apa = alumno_clase.aPaterno.data
        ama = alumno_clase.aMaterno.data
        edad = alumno_clase.edad.data
        print('Nombre: {}'.format(nom))
        print('aPaterno: {}'.format(apa))
        print('aMaterno: {}'.format(ama))
    
        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    
    return render_template("alumnos.html", form = alumno_clase, nom = nom, apa = apa, ama = ama)
        
@app.route("/maestros")
def maestros():
    return render_template("maestros.html")


@app.route("/hola")
def hola():
    return "<h1>Saludos desde Hola </h1>"


@app.route("/saludo")
def saludo():
    return "<h1>Saludos desde Saludo</h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "Hola: "+nom 
    

@app.route("/numero/<int:n1>")
def numero(n1):
    return "Numero: {} ".format(n1) 

@app.route("/user/<int:id>/<string:nom>")
def func(id,nom):
    return "ID: {} Nombre: {}".format(id,nom)


@app.route("/suma/<float:n1>/<float:n2>")
def func2(n1,n2):
    return "La suma {} + {} ={}".format(n1,n2,n1+n2)

@app.route("/default")
@app.route("/default/<string:d>")
def func3(d="Dario"):
    return "El nombre de User es: "+d

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method=="POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        
        return "La multiplicacion de {} X {} = {}".format(num1, num2, str(int(num1)*int(num2)))
        
    return'''
          <form action="/calcular" method="POST">
            <label>N1:</label>
            <input type="text" name="n1"><br>
            <label>N2:</label>
            <input type="text" name="n2"><br>
            <input type="submit"/>
          </form>  
          '''
          
@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resul():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        
        return "La multiplicacion de {} X {} = {}".format(num1, num2, str(int(num1)*int(num2)))

if __name__=="__main__":
    app.run(debug=True)