import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Générateur de mots de passe")

tk.Label(fenetre, text="Longueur :").pack()
longueur = tk.Scale(fenetre, from_=32, to=256, orient="horizontal")
longueur.pack()

tk.Checkbutton(fenetre, text="Majuscules").pack()
tk.Checkbutton(fenetre, text="Chiffres").pack()
tk.Checkbutton(fenetre, text="Symboles").pack()

tk.Button(fenetre, text="Générer").pack()

fenetre.mainloop()