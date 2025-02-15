from flask import Flask, render_template
import random as r

app = Flask(__name__)

factos=["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
        "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
        "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
        "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
        "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
        "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
        "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
        "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]

p="<p>Hello, World!</p>"
h1="<h1>Hello, World!</h1>"
a="<a href='/Factos'>Descubre un dato</a>"
a2="<a href='/Index'>Mi pagina</a>"
br="<br>"

@app.route("/")
def hello_world():
    return h1 + p + a + br + a2

@app.route("/Factos")
def facts():
    li=f"<li>Dato del día:{r.choice(factos)}</li>"
    return li 

@app.route("/Index")
def web():

    return render_template("index.html")



app.run(debug=True, port=5200)
 