from flask import Flask, redirect, render_template, request, session
import mysql.connector

#connect to mysql database
mydb = mysql.connector.connect(
  host="localhost",
  user="gracia",
  password="graciaH.2608",
  database="pen"
)
db = mydb.cursor()

#flask application
app = Flask(__name__)
#accueil
@app.route("/")
def index():
    return render_template("index.html")

#chercher les propriétés d'un cristal
@app.route("/propriétés",  methods=["GET", "POST"])
def propriétés():
    if request.method == "POST":
        db.execute("SELECT * FROM cristaux WHERE nom = %s", request.form.getlist('nom'))
        prop=db.fetchall()
        if len(prop) == 0:
            return render_template("désolé.html")
        else:
            crist = []
            for i in range (len(prop)):
                add = {"nom": prop[i][1],
                        "couleur": prop[i][2],
                        "maille": prop[i][3],
                        "densité": prop[i][4]
                }
                crist.append(add)
            
            return render_template("résultat.html", crist=crist)
    else:
        return render_template("propriétés.html")
    
#chercher le nom d'un cristal
@app.route("/nom",  methods=["GET", "POST"])    
def nom():
    if request.method == "POST":
        couleur = request.form.get("couleur")
        maille = request.form.get("maille")
        densité = request.form.get("densité")

        db.execute("SELECT * FROM cristaux WHERE couleur = %s and maille = %s and densité = %s",(couleur, maille, densité))
        prop= db.fetchall()
        if len(prop) == 0:
            db.execute("SELECT * FROM cristaux WHERE couleur = %s or maille = %s or densité = %s", (couleur, maille, densité ))
            sugg=db.fetchall()
            if len(sugg) == 0:
                return render_template("désolé.html")
            else:
                poss = []
                for i in range (len(sugg)):
                    add = {"nom": sugg[i][1],
                            "couleur": sugg[i][2],
                            "maille": sugg[i][3],
                            "densité": sugg[i][4]
                    }
                    poss.append(add)
                return render_template("suggestions.html", poss=poss)
        else:
            crist = []
            for i in range (len(prop)):
                add = {"nom": prop[i][1],
                        "couleur": prop[i][2],
                        "maille": prop[i][3],
                        "densité": prop[i][4]
                }
                crist.append(add)
            return render_template("résultat.html", crist=crist)
    else:
        return render_template("nom.html")

#ajouter un cristal
@app.route("/ajouter",  methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        nom = request.form.get("nom")
        couleur = request.form.get("couleur")
        maille = request.form.get("maille")
        densité = request.form.get("densité")
        db.execute("INSERT INTO cristaux (nom, couleur, maille, densité) VALUES (%s,%s,%s,%s)",(nom, couleur, maille, densité))
        db.execute("SELECT nom FROM cristaux")
        verif = db.fetchall()
        mydb.commit()
        return redirect("/")
    else:
        return render_template("ajouter.html")