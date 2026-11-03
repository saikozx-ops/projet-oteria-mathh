import tkinter as tk
import random
import string
import time
import math


def genmdp(nb_caractere, maj, chiffre, special):
    lettres_minuscules = list(string.ascii_lowercase)
    lettres_majuscules = list(string.ascii_uppercase)
    chiffres = list(string.digits)
    caracteres_speciaux = list(string.punctuation)    # tout les cara/ lettres etc
 
    listefinal = []       # vas permettre de stocker tout pour crée le mdp final
    listefinal += lettres_minuscules   # de base ça pour le mdp
 
    if maj == "O":
        listefinal += lettres_majuscules
    if chiffre == "O":
        listefinal += chiffres
    if special == "O":
        listefinal += caracteres_speciaux     # utilsier le caractère O pour oui mais tt marche
 
   
                                                     
    mot_de_passe = []                             # liste pour prendre aleatoierment dans les caractere choisis

    for i in range(nb_caractere):
        mot_de_passe.append(random.choice(listefinal))    # prend aleatoiremet 

    mot_de_passe_finale = "".join(mot_de_passe)     # on passe d'une liste a une variable

    valide = True    

    for i in range(len(mot_de_passe_finale) - 1):
        if mot_de_passe_finale[i] == mot_de_passe_finale[i+1]:
            valide = False
            break                           # permet de check si il y a un doublon de caractère  

    if valide:
        return mot_de_passe_finale
    else:
        return genmdp(nb_caractere, maj, chiffre, special)     #on recomence car mdp a doublon

def entropie(nb_caractere, maj, chiffre, special, E):
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
        y = 0
        for i in range(nb_caractere):
            y+=1

        E = (math.log2(len(listefinal)))*y
        return E                                            # oui c'est degeu prsk ca reprend ce que le code prend deja en haut mais ratio ,  ça calcul l'entropie final correctement donc on touche pas svp
 
def fenetre():
 
    fenetre = tk.Tk()  #crée la fenetre
    fenetre.title("Générateur de mots de passe")      # titre fenetre
 
    maj = tk.StringVar(value="N")        # value des case sur non de base
    chiffre = tk.StringVar(value="N")
    special = tk.StringVar(value="N")
    E = tk.StringVar(value="N")         # same
    resultat = tk.StringVar()               # CRÉE UNE VARI A   ABLE POUR COTENIR DU TEXTE
 
    tk.Label(fenetre, text="Longueur :").pack()   #txt
    longueur = tk.Scale(fenetre, from_=8, to=24, orient="horizontal") # taille de la barre pour le nb de caract
    longueur.pack()       # permet d'afficher le widjet avec la barre qui deroule, bugé sur linux mais sur windows marche donc pas touche
    fenetre.geometry("600x300")   # taille fenetre
    tk.Checkbutton(fenetre, text="Majuscules", variable=maj, onvalue="O", offvalue="N").pack()  # permetde chosir si oui ou non
    tk.Checkbutton(fenetre, text="Chiffres", variable=chiffre, onvalue="O", offvalue="N").pack()
    tk.Checkbutton(fenetre, text="Symboles", variable=special, onvalue="O", offvalue="N").pack()
    tk.Checkbutton(fenetre, text="entropie", variable=E, onvalue="O", offvalue="N").pack()
    tk.Label(fenetre, text="<moins de 36 bits, Pas sécurisé>").pack() # txt
    tk.Label(fenetre, text="<36 à 59 bits, bof>").pack()
    tk.Label(fenetre, text="<60 bits et +, sécurisé>").pack()    #txt
 
    def generer():
        mot_de_passe_finale = genmdp(longueur.get(), maj.get(), chiffre.get(), special.get())   #  envoie les info pour gen le mdp
        entropie_finale = entropie(longueur.get(), maj.get(), chiffre.get(), special.get(), E.get()) # same pour entrpoie
        if E.get() == "O":                            # e cest lentropie 
            resultat.set(f"{mot_de_passe_finale}   |   Entropie : {entropie_finale:.1f} bits") # set l'entropie si activé  et :.1f arrondie au dixieme
        else:
            resultat.set(mot_de_passe_finale)            # set que mdp si entropie pas activé
 
    tk.Button(fenetre, text="Générer", command=generer).pack()    #bouton
    tk.Entry(fenetre, textvariable=resultat, width=80).pack()    # endroit ou le texte apparait
 
    fenetre.mainloop()
 
fenetre()
 
