import subprocess
from tkinter import simpledialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import json

root = tk.Tk()
root.withdraw()

class Menu:
    def __init__(self):
        self.menu = tk.Toplevel(root)
        self.menu.title("Menu de Pedro")
        self.menu.geometry("300x500")
        self.menu.attributes('-topmost', True)

        self.pedro = False

        tk.Label(self.menu, text="Bienvenue dans le menu de Pedro !", font=("Arial", 12)).pack(pady=10)

        img_open = Image.open(r"Pedro.png")
        self.img = ImageTk.PhotoImage(img_open.resize((150, 180)))
        self.label = tk.Label(self.menu, image=self.img, bd=0)
        self.label.pack()

        tk.Button(self.menu, text="Lancer Pedro", command=self.lancer_pedro).pack(pady=10)
        tk.Button(self.menu, text="Ajouter une phrase", command=self.ajouter_phrase).pack(pady=10)
        tk.Button(self.menu, text="Fermer le menu", command=exit).pack(pady=10)
        tk.Button(self.menu, text="Fermer Pedro", command=self.fermer_pedro).pack(pady=10)
    
    def ajouter_phrase(self):
        phrase = tk.simpledialog.askstring("Ajouter une phrase", "Entrez la nouvelle phrase :")
        fenetre = tk.simpledialog.askstring("Type", "Pour quelle fenêtre ?").lower()

        if phrase and fenetre:
            path_json = r".json"
            
            with open(path_json, "r") as f:
                data = json.load(f)

            data["phrases"][phrase] = fenetre 

            with open(path_json, "w") as f:
                json.dump(data, f, indent=4)
                
            tk.messagebox.showinfo("Succès", "Phrase ajoutée au dictionnaire de Pedro !")
        
        else:
            tk.messagebox.showerror("Erreur", "Veuillez entrer une phrase et une fenêtre valides.")
    
    def lancer_pedro(self):
        if not hasattr(self, 'pedro_process') or self.pedro_process.poll() is not None:
            path = r"ppi.py"
            self.pedro_process = subprocess.Popen(["python", path])
            self.pedro = True
            print("Pedro est lancé !")
        else:
            tk.messagebox.showinfo("Info", "Pedro est déjà réveillé !")

    def fermer_pedro(self):
        if hasattr(self, 'pedro_process') and self.pedro_process.poll() is None:
            self.pedro_process.terminate() 
            self.pedro = False
            tk.messagebox.showinfo("Succès", "Pedro est reparti dans son rêve.")
        else:
            self.pedro = False
            tk.messagebox.showinfo("Info", "Pedro n'est pas en cours d'exécution.")

menu = Menu()
root.mainloop()