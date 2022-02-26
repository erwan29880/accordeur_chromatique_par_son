from tkinter import *
from tkinter import filedialog
from typing import List
import pygame
import os


class Lecteur:


    def __init__(self, import_liste_test=2):
        
        # importer une playlist
        self.import_liste_texte = import_liste_test

        # initialisation de la fenêtre
        self.__root=Tk()
        self.__root.geometry('750x300')
        self.__root.title('accordeur chromatique par son')
        self.song_box = None

        # la frame qui va contenir les fichiers
        self.listbox_frame = Frame(self.__root)
        self.listbox_frame.pack(ipadx=20, pady=10)

        # la liste avec les tunes
        self.song_box = Listbox(self.listbox_frame, bg = 'black', fg = 'green', width=80)
        self.song_box.pack(ipady=20)

        # la barre de défilement
        self.__scrollbar = Scrollbar(self.listbox_frame)
        self.__scrollbar.pack(side = 'right', fill = 'both')
        self.song_box.config(yscrollcommand = self.__scrollbar.set)
        self.__scrollbar.config(command = self.song_box.yview)

        # les images des boutons
        self.__play_btn_img = PhotoImage(file='media/play1.png')
        self.__stop_btn_img = PhotoImage(file='media/stop1.png')
        self.__clear_btn_img = PhotoImage(file='media/clear.png')

        # conteneur pour les boutons : 
        self.__controls_frame = Frame(self.__root)
        self.__controls_frame.pack()

        # les boutons
        self.__play_btn = Button(self.__controls_frame, image=self.__play_btn_img, command=self.play)
        self.__stop_btn = Button(self.__controls_frame, image=self.__stop_btn_img, command = self.stop)
        # self.__clear_btn = Button(self.__controls_frame, image=self.__clear_btn_img, command=self.clear_playlist)

        self.__play_btn.grid(column=0, row=0, padx=10)
        self.__stop_btn.grid(column=1, row=0, padx=10)
        # clear_btn.grid(column=2, row=0, padx=10)

        # menus
        self.__my_menu = Menu(self.__root)
        self.__root.config(menu = self.__my_menu)

        # sous-menu
        self.__sous_menu = Menu(self.__my_menu)
        self.__my_menu.add_cascade(label = 'fichier', menu=self.__sous_menu)
        self.__sous_menu.add_command(label='ouvrir un fichier', command=self.add_file)
        self.__sous_menu.add_command(label='supprimer la playlist', command=self.clear_playlist)
        self.__sous_menu.add_command(label='supprimer l\'élément', command=self.remove_item_playlist)
        self.__sous_menu.add_command(label='quitter', command=self.__root.quit)
  

        


        # initialisation du mixer pygame
        pygame.mixer.init()
    



    # fonctions callback

    def add_file(self):
        song = filedialog.askopenfilename(initialdir='./', title="choisissez un fichier", filetypes=[('mp3 Files','*.mp3'), ('wave Files', '*.wav')])
        self.song_box.insert(END, song)

    def play(self):
        song = self.song_box.get(ACTIVE)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=-1)

    def stop(self):
        pygame.mixer.music.stop()

    def clear_playlist(self):
        self.song_box.delete(0, END)

    def remove_item_playlist(self):
        song = self.song_box.get(ACTIVE)
        idx = self.song_box.get(0, END).index(song)
        self.song_box.delete(idx)
    
    def import_fichier_playlist1(self):
        """importe acdc !"""
        liste_mp3 = []
        
        for i in (os.listdir('/home/erwan/Musique/audio/')):
            if i.endswith('.mp3'):
                dossier = '/home/erwan/Musique/audio/'+i
                liste_mp3.append(dossier)

        liste_mp3 = sorted(liste_mp3)
        
        for i in liste_mp3:
                self.song_box.insert(END, i)
    

    def import_fichier_playlist2(self):
        "importe les fichiers midis"
        liste_mp3 = []
        
        for i in (os.listdir('/home/erwan/Musique/notes_3/')):
            if i.endswith('.wav'):
                dossier = '/home/erwan/Musique/notes_3/'+i
                liste_mp3.append(dossier)

        liste_mp3 = sorted(liste_mp3)
        
        for i in liste_mp3:
                self.song_box.insert(END, i)

       

    def demarrer_le_programme(self):
        if self.import_liste_texte == 1:
            self.import_fichier_playlist1()     
        if self.import_liste_texte == 2:
            self.import_fichier_playlist2()

        self.__root.mainloop()
    
    
    
    
    
if __name__ == "__main__":

    fen = Lecteur(import_liste_test=2)

    fen.demarrer_le_programme()
    
    
    
    






    