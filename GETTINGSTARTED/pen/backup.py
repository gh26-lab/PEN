import mysql.connector

#connect to mysql database
mydb = mysql.connector.connect(
  host="localhost",
  user="gracia",
  password="graciaH.2608",
  database="pen"
)
db = mydb.cursor()
#main
def main():
    #demander à l'utilisateur ce qu'il veut faire
    print("\nBonjour, merci de suivre les consignes suivantes:\n\n Pour chercher les propriétés d'un crisltal tappez 1\n "
    "Pour chercher le nom d'un cristal à partir de ses propriétés tappez 2\n Pour enregistrer un nouveau cristal dans la base de données tappez 3\n")
    while True:
        try:
            choix = int(input("Que voulez vous faire:"))
            if choix == 1 or choix == 2 or choix == 3:
                break
            else:
                print("l'information attendue est un chiffre (1, 2 ou 3)")
        except ValueError:
            print("l'information attendue est un chiffre (1, 2 ou 3)")

    #exécuter la demande de l'utilisateur
    if choix == 1:
        propriétés()
    elif choix == 2:
        nom()
    elif choix == 3:
        ajouter()

#donner les propriétés d'un cristal à partir de son nom
def propriétés():
    nom = ['az','22','']
    nom.append(input("nom du cristal (ex: )"))
    print(db.execute("SELECT * FROM cristaux WHERE nom = %s",nom))

#donner le nom d'un cristal à partir de ses propriétés
def nom():
    print("à faire")

#ajouter un cristal (nom + propriétés) à la base de données
def ajouter():
    print("à faire")

#main
if __name__ == "__main__":
    main()
