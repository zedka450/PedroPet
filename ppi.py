import tkinter as tk
import pygetwindow as gw
from PIL import Image, ImageTk
import random
import datetime
import json

class PedroApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-topmost', True, '-transparentcolor', '#abcdef')
        self.root.overrideredirect(True)
        self.root.config(bg='#abcdef')

        self.bulle = tk.Toplevel(self.root)
        self.bulle.overrideredirect(True)
        self.bulle.attributes('-topmost', True)
        self.bulle.config(bg='white', bd=2, relief='solid')
        self.texte_bulle = tk.Label(self.bulle, text="", font=("Arial", 10), bg='white', wraplength=150)
        self.texte_bulle.pack(padx=5, pady=5)
        self.bulle.withdraw() 

        self.faim = 0
        self.mange = False
        with open(".json", "r") as f:
            self.data = json.load(f)

        try:
            img_open = Image.open(r"Pedro.png")
            self.img = ImageTk.PhotoImage(img_open.resize((150, 180)))
            self.label = tk.Label(self.root, image=self.img, bg='#abcdef', bd=0)
            self.label.pack()
        except:
            self.label = tk.Label(self.root, text="⛄️", font=("Arial", 30))
            self.label.pack()

        self.label.bind("<B1-Motion>", self.deplacer)
        self.label.bind("<Button-3>", lambda e: self.root.destroy())
        
        self.last_app = ""
        self.surveiller()

    def deplacer(self, event):
        x = self.root.winfo_pointerx() - 75
        y = self.root.winfo_pointery() - 90
        self.root.geometry(f"+{x}+{y}")
        self.maj_bulle()

    def dire(self, texte):
        self.texte_bulle.config(text=texte)
        self.bulle.deiconify() 
        self.maj_bulle()
        self.root.after(5000, self.bulle.withdraw)

    def maj_bulle(self):
        px = self.root.winfo_x()
        py = self.root.winfo_y() - 50
        self.bulle.geometry(f"+{px}+{py}")

    def surveiller(self):
        if datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 14 and self.mange == False or datetime.datetime.now().hour >= 19 and datetime.datetime.now().hour < 21 and self.mange == False or datetime.datetime.now().hour >= 8 and datetime.datetime.now().hour < 10 and self.mange == False:
            self.dire(random.choice(["J'ai faim ! Va sur un site de nourriture !", "C'est l'heure de manger ! Va sur un site de nourriture !", "Donne-moi à manger ! Va sur un site de nourriture !"]))
            self.faim += 1
            
        try:
            win = gw.getActiveWindow()
            if win:
                title = win.title.lower()
                if title != self.last_app and self.faim == 0:
                    if "paint" in title or "krita" in title or "photoshop" in title or "gimp" in title or "illustrator" in title or "draw" in title:
                        self.dire(random.choice(["Hé ! Tu dessines quoi ?", "C'est un chef-d'œuvre en cours ?", "Tu es un artiste en herbe ?"]))
                    elif "code" in title or "py" in title or "notepad" in title or "sublime" in title or "vscode" in title or "html" in title or "css" in title or "js" in title:
                        self.dire(random.choice(["C'est du python ce code ?", "Tu fais du développement web ?", "Tu codes quoi ?"]))
                    elif "food" in title:
                        self.dire(random.choice(["C'est pas Halal !", "Tu manges quoi ?", "Miam, ça sent bon !"]))
                    elif "youtube" in title or "netflix" in title or "twitch" in title:
                        self.dire(random.choice(["Tu regardes des vidéos au lieu de bosser ?", "Tu passes ton temps à regarder des vidéos ?", "Ouais, faut se détendre un peu, mais pas trop !"]))
                    elif "spotify" in title:
                        self.dire(random.choice(["Tu écoutes de la musique ?", "Tu aimes quel genre de musique ?"]))
                    elif "discord" in title:
                        self.dire(random.choice(["Tu parles à qui ?", "Tu discutes avec tes amis ?", "C'est pour le boulot ?"]))
                    elif "wikipédia" in title or "search" in title or "wikitionaire" in title or "ent" in title:
                        self.dire(random.choice(["Tu bosses sur quoi ?", "Tu cherches des infos ?", "Ha, cool, tu fait tes devoirs."]))
                    for phrase, fenetre in self.data["phrases"].items():
                        if fenetre in title:
                            self.dire(phrase)
                    self.last_app = title
                elif title != self.last_app and self.faim >= 1:
                    if "food" in title:
                        self.dire(random.choice(["Merci, j'avais super faim !", "Miam, ça a l'air délicieux !", "Tu m'as sauvé la vie !", "On va manger des nuggets ! Gedagedigedagdao"]))
                        self.faim = 0
                        self.mange = True
                    self.last_app = title
                if self.faim == 3:
                    self.dire(random.choice(["J'ai trop faim, je vais manger tout seul !", "Je suis affamé, je vais me faire un sandwich !", "Je meurs de faim, je vais manger une pomme !"]))
                    self.faim = 0
                    self.mange = True
        except: pass
        self.root.after(2000, self.surveiller)
app = PedroApp()
app.root.mainloop()