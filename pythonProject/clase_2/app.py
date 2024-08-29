from flask  import Flask, render_template

app = Flask(__name__)

class Pelicula:
    def __init__(self,nombre,año,protagonista):
        self.nombre = nombre
        self.año = año
        self.protagonista = protagonista




@app.route("/estructura")
def estructura_datos():
    peliculas = ["EL lobo de wall street",
                "harry Potter",
                "Volver al futuro"
    ]



    lobo= {
        "Nombre" : "Lobo de wall Street",
        "Año" : 2013,
        "Protagonista" : "Leonardo Dicrapio",
    }

    volver = Pelicula("volver al futuro",1985,"Michael j. Fox")

    return render_template("estructuras.html", movies = peliculas,destacada = lobo, favorita = volver)



if __name__ =="__main__":
    app.run()

