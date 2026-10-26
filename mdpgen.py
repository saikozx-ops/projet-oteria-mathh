import tkinter as tk
import random
import string
import time
import math


def genmdp(nb_caractere, maj, chiffre, special):
    lettres_minuscules = list(string.ascii_lowercase)
    lettres_majuscules = list(string.ascii_uppercase)
    chiffres = list(string.digits)
    caracteres_speciaux = list(string.punctuation)
 
    listefinal = []
    listefinal += lettres_minuscules
 
    if maj == "O":
        listefinal += lettres_majuscules
    if chiffre == "O":
        listefinal += chiffres
    if special == "O":
        listefinal += caracteres_speciaux
 
 
    mot_de_passe = []
    for i in range(nb_caractere):
       mot_de_passe.append(random.choice(listefinal))
 
    mot_de_passe_finale = "".join(mot_de_passe)
    return mot_de_passe_finale
 
 
def fenetre():
 
    fenetre = tk.Tk()
    fenetre.title("Générateur de mots de passe")
 
    maj = tk.StringVar(value="N")
    chiffre = tk.StringVar(value="N")
    special = tk.StringVar(value="N")
    resultat = tk.StringVar()
 
    tk.Label(fenetre, text="Longueur :").pack()
    longueur = tk.Scale(fenetre, from_=8, to=24, orient="horizontal")
    longueur.pack()
    fenetre.geometry("600x300")
    tk.Checkbutton(fenetre, text="Majuscules", variable=maj, onvalue="O", offvalue="N").pack()
    tk.Checkbutton(fenetre, text="Chiffres", variable=chiffre, onvalue="O", offvalue="N").pack()
    tk.Checkbutton(fenetre, text="Symboles", variable=special, onvalue="O", offvalue="N").pack()
 
    def generer():
        mot_de_passe_finale = genmdp(longueur.get(), maj.get(), chiffre.get(), special.get())
        resultat.set(mot_de_passe_finale)
 
    tk.Button(fenetre, text="Générer", command=generer).pack()
    tk.Entry(fenetre, textvariable=resultat, width=80).pack()
 
    fenetre.mainloop()
 
#teste
fenetre()
 