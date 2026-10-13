from flask import Flask

app = Flask(__name__)

import random

Facts = [
    "Me encanta programar",
    "Me gustan los animales",
    "Soy bueno en matemáticas",
    "Soy un buen estudiante",
    "Soy creativo"
]

@app.route("/Fact")
def Inicio():
    return f'<p>Hola! {random.choice(Facts)}</p>'

@app.route("/")
def Home():
    return '<h1>Bienvenido a la página sobre mi!</h1> <a href="/Fact">¡Ver un dato aleatorio!</a> <a1 href="/Password">Intenta adivinar la contraseña de la WEB!</a1>'

@app.route("/Password")
def Password():
    Valid = "abcdefghijklmnopqrstuvwxyz+-*.,_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Length = 30
    Pass = ""
    for i in range(Length-1):
        Pass += random.choice(Valid)

    return Pass

@app.route("/Operator/<string:Operation>/<int:num1>/<int:num2>")
def Operator(Operation,num1, num2):
    if Operation == "sum":
        resultado = num1 + num2
        return f"<h1> La suma es {resultado} </h1>"
    elif Operation == "sub":
        resultado = num1 - num2
        return f"<h1> La resta es {resultado} </h1>"
    elif Operation == "mul":
        resultado = num1 * num2
        return f"<h1> La multiplicación es {resultado} </h1>"
    elif Operation == "div":
        resultado = num1 / num2
        return f"<h1> La División es {resultado} </h1>"
    elif Operation == "pow":
        resultado = num1 ** num2
        return f"<h1> La Potencia es {resultado} </h1>"

app.run(debug=True)