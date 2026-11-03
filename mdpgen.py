import tkinter as tk
import secrets
import os
import string
import math

global last_mdp

def save():
    if not os.path.exists("save"):
        os.mkdir("save")

    mdp = last_mdp

    with open("save/mots2passe.txt", "a", encoding="UTF-8") as save:
        save.write(mdp + "\n")

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

    nb_caracteres_disponibles = len(listefinal)

    if nb_caracteres_disponibles < 2 or nb_caractere <= 0:
        raise ValueError("Longueur ou alphabet invalide")

    mot_de_passe = []

    for i in range(nb_caractere):
        choix = listefinal.copy()

        if i > 0:
            choix.remove(mot_de_passe[i-1])

        mot_de_passe.append(secrets.choice(choix))

    mot_de_passe_finale = "".join(mot_de_passe)

    return mot_de_passe_finale

def calcul_entropie(mdp):
    alphabet = 0

    if any(c in string.ascii_lowercase for c in mdp):
        alphabet += 26

    if any(c in string.ascii_uppercase for c in mdp):
        alphabet += 26

    if any(c in string.digits for c in mdp):
        alphabet += 10

    if any(c in string.punctuation for c in mdp):
        alphabet += len(string.punctuation)

    if alphabet == 0:
        return 0

    E = len(mdp) * math.log2(alphabet)

    return E

def entropie(nb_caractere, maj, chiffre, special):
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

        E = (math.log2(len(listefinal)))*nb_caractere
        return E

def fenetre():
    global last_mdp

    fenetre = tk.Tk()
    fenetre.title("Generateur de mots de passe")
    fenetre.geometry("600x350")

    maj = tk.StringVar(value="N")
    chiffre = tk.StringVar(value="N")
    special = tk.StringVar(value="N")
    E = tk.StringVar(value="N")

    resultat = tk.StringVar()
    entropie_calcule = tk.StringVar()
    text2variable = tk.StringVar()

    tk.Label(fenetre, text="Longueur :").pack()

    longueur = tk.Scale(fenetre, from_=8, to=24, orient="horizontal")
    longueur.pack()

    tk.Checkbutton(fenetre, text="Majuscules", variable=maj, onvalue="O", offvalue="N").pack()
    tk.Checkbutton(fenetre, text="Chiffres", variable=chiffre, onvalue="O", offvalue="N").pack()
    tk.Checkbutton(fenetre, text="Symboles",variable=special, onvalue="O", offvalue="N").pack()
    tk.Checkbutton(fenetre, text="Entropie", variable=E, onvalue="O", offvalue="N").pack()

    tk.Label(fenetre, text="<moins de 36 bits, Pas securise>").pack()
    tk.Label(fenetre, text="<36 à 59 bits, bof>").pack()
    tk.Label(fenetre, text="<60 bits et +, securise>").pack()

    # GENERATION DU MOT DE PASSE
    def generer():
        global last_mdp

        nb = longueur.get()
        mot_de_passe_finale = genmdp(nb, maj.get(), chiffre.get(), special.get())

        last_mdp = mot_de_passe_finale
        entropie_finale = entropie(nb, maj.get(), chiffre.get(), special.get())

        if E.get() == "O":
            resultat.set(f"{mot_de_passe_finale} | Entropie : {entropie_finale:.1f} bits")
        else:
            resultat.set(mot_de_passe_finale)

    # CALCUL DE L'ENTROPIE
    def calcule():
        mdp = entropie_calcule.get()
        if not mdp:
            text2variable.set("Veuillez entrer un mot de passe.")
            return

        calculte2entropie = calcul_entropie(mdp)
        text2variable.set(f"Entropie théorique estimée : {calculte2entropie:.1f} bits")

    # BOUTONS ET AFFICHAGE

    tk.Button(fenetre, text="Generer", command=generer).pack()
    tk.Button(fenetre, text="Sauvegarder", command=save).pack()
    tk.Entry(fenetre, textvariable=resultat, width=80).pack()

    tk.Label(fenetre, text="Calculer l'entropie d'un mot de passe :").pack(pady=5)
    tk.Entry(fenetre, textvariable=entropie_calcule, width=80).pack()
    tk.Button(fenetre, text="Calculer Entropie", command=calcule).pack()
    tk.Label(fenetre, textvariable=text2variable).pack(pady=5)

    fenetre.mainloop()

if __name__ == "__main__":
    fenetre()
