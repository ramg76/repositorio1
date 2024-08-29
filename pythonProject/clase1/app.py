from flask  import Flask,render_template

app = Flask(__name__)

#ruta : ejecuta las funciones en la ruta especificada "/" es la raiz o rutra principal
@app.route("/")
def hola_mundo():
    return "Hola Mundo!!"
#Para ejecutar en la terminal flask run

#en lugar mas adecuada o elegante
@app.route("/elegante")
def hola_mundo_elegante():
    return """
    <html>
        <body>
            <h1>Saludos!!</h1>
            <p>Hola Mundo!!</p>
        <body>
    </html>
             """
#primera_pagina.html
@app.route("/primera")
def template_primera():
    return render_template("primera_pagina.html")

#seguna pagina y segunda_pagina.html es el template que corresponde
@app.route("/segunda")
def template_segunda():
    return render_template("segunda_pagina.html")

@app.route("/variables")
def hola_nombre():
    return render_template("variables.html", nombre = "Rodrigo",curso = "Python")

@app.route("/carolina")
def hola_carolina():
    return render_template("variables.html", nombre = "carolina",curso = "Excel")

@app.route("/expresiones2")
def expresiones2():
    kwargs = {
    "nombre" :"Rodrigo",
    "apellido" : "Marin",
    "color" : "Naranjo",
    "base" : 5,
    "altura" :10
    }
    return render_template("expresiones.html", **kwargs)



#para ejecutar no desde terminal
if __name__ =="__main__":
    app.run()
