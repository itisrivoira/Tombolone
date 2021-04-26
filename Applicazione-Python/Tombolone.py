import tkinter as tk
from tkinter import messagebox
from os import path
import os, random
import pygame as pygame


class Giocatore():
    def __init__(self, nome, schedine):
        self._nome=nome
        self._schedine=schedine
        self._punteggioCorrente=0
        self._classifica=[]
        self._flagPronto=False

    def setFlagPronto(self, val):
        self._flagPronto=val

    def getFlagPronto(self):
        return self._flagPronto

    def setNome(self, nome):
        self._nome=nome
    
    def setSchedine(self, schedine):
        self._schedine=schedine

    def setPunteggioCorrente(self, punteggio):
        self._punteggioCorrente = punteggio

    def setClassifica(self, classifica):
        self._classifica=classifica

    def addRecordToClassifica(self, record):
        self._classifica.append(record)

    def getNome(self):
        return self._nome
    
    def getSchedine(self):
        return self._schedine

    def getPunteggioCorrente(self):
        return self._punteggioCorrente

    def getClassifica(self):
        return self._classifica


class Tombolone(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.currentDirectory = path.abspath(os.getcwd())
        self.master.title("Il Tombolone")
        self.larghezzaCellaSchedine=1
        self.larghezzaCellaTabellone=2
        self.larghezza = int(self.master.winfo_screenwidth()/1)
        self.altezza = int(self.master.winfo_screenheight()/1)
        print("Altezza: ", self.altezza, "\n Larghezza: ", self.larghezza)
        self.master.geometry("%dx%d+0+0" % (self.larghezza, self.altezza))
        self.update()
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.screen="window"
        self.master.bind("<f>", self.fullscreen)
        self.grid()
        print(self.currentDirectory)
        lblAltezza=tk.Label(self, text="", font=("Helvetica", 1), bg="black", height=int(self.altezza/2)).grid(row=0, column=1, sticky="ns")
        lblLarghezza=tk.Label(self, text="", font=("Helvetica", 1), bg="black", width=self.larghezza).grid(row=1, column=0, sticky="ew")
        self.globals()
        self.colors()
        pygame.mixer.init()
        pygame.mixer.music.pause()
        pygame.mixer.music.load(self.currentDirectory+"/Files/Musica/ColonneSonore/Shake.ogg")
        pygame.mixer.music.play(-1)
        self.clickSound=pygame.mixer.Sound(file=path.abspath(self.currentDirectory+"/Files/Musica/EffettiSonori/click.ogg"))
        self.CreateWidgets()
        self.Menu(event=None)


    def fullscreen(self, event):
        if self.screen=="full":
            self.master.attributes("-fullscreen", False)
            self.screen="window"
        else:
            self.master.attributes("-fullscreen", True)
            self.screen="full"

    def colors(self):
        # Setto le variabili globali dei colori 
        # per gli sfondi e per le scritte
        """"""
        """------------------   VARIABILI   -------------------"""
        self.punteggio_sfondo_bg_color = "black"
        self.punteggio_titolo_bg_color = "black"
        self.punteggio_titolo_fg_color = "black"
        self.punteggio_labels_bg_color = "black"
        self.punteggio_labels_fg_color = "black"

        self.menu_sfondo_bg_color = "black"
        self.menu_titolo_bg_color = "black"
        self.menu_titolo_fg_color = "black"
        self.menu_buttons_bg_color= "black"
        self.menu_buttons_fg_color= "black"

        self.gioco_sfondo_bg_color = "black"
        self.gioco_titolo_bg_color = "black"
        self.gioco_titolo_fg_color = "black"
        self.gioco_nestratto_bg_color = "black"
        self.gioco_nestratto_fg_color = "black"
        self.gioco_label_nestratto_bg_color = "black"
        self.gioco_label_nestratto_fg_color = "black"
        self.gioco_tabellone_unset_bg_color = "black"
        self.gioco_tabellone_unset_fg_color = "black"
        self.gioco_tabellone_set_bg_color = "black"
        self.gioco_tabellone_set_fg_color = "black"
        self.gioco_schedine_unset_bg_color = "black"
        self.gioco_schedine_unset_fg_color = "black"
        self.gioco_schedine_set_bg_color = "black"
        self.gioco_schedine_set_fg_color = "black"
        self.gioco_schedine_disabled_fg_color = "black"
        self.gioco_logs_bg_color = "black"
        self.gioco_logs_fg_color = "black"
        self.gioco_framedestro_bg_color = "black"
        self.gioco_classifica_bg_color = "black"
        self.gioco_classifica_titolo_fg_color = "black"
        self.gioco_classifica_tabella_fg_color = "black"
        self.gioco_premi_bg_color = "black"
        self.gioco_premi_titolo_fg_color = "black"
        self.gioco_premi_btns_bg_color = "black"
        self.gioco_premi_btns_fg_color = "black"
        
        self.pregioco_sfondo_bg_color = "black"
        self.pregioco_titolo_bg_color = "black"
        self.pregioco_titolo_fg_color = "black"
        self.pregioco_labels_bg_color = "black"
        self.pregioco_labels_fg_color = "black"
        self.pregioco_options_bg_color = "black"
        self.pregioco_options_fg_color = "black"
        self.pregioco_rbtn_circle_bg_color = "black"

        self.impostazioni_sfondo_bg_color = "black"
        self.impostazioni_titolo_bg_color = "black"
        self.impostazioni_titolo_fg_color = "black"
        self.impostazioni_labels_bg_color = "black"
        self.impostazioni_labels_fg_color = "black"
        self.impostazioni_options_bg_color = "black"
        self.impostazioni_options_fg_color = "black"
        self.impostazioni_rbtn_circle_bg_color = "black"
        
        
        
        """------------------   SCURO   -------------------"""
        self.punteggio_sfondo_dark_bg_color = "black"
        self.punteggio_titolo_dark_bg_color = "black"
        self.punteggio_titolo_dark_fg_color = "white"
        self.punteggio_labels_dark_bg_color = "black"
        self.punteggio_labels_dark_fg_color = "white"

        self.menu_sfondo_dark_bg_color = "black"
        self.menu_titolo_dark_bg_color = "black"
        self.menu_titolo_dark_fg_color = "white"
        self.menu_buttons_dark_bg_color = "gray"
        self.menu_buttons_dark_fg_color = "white"

        self.gioco_sfondo_dark_bg_color = "black"
        self.gioco_titolo_dark_bg_color = "black"
        self.gioco_titolo_dark_fg_color = "black"
        self.gioco_label_nestratto_dark_bg_color = "gray"
        self.gioco_label_nestratto_dark_fg_color = "white"
        self.gioco_nestratto_dark_bg_color = "black"
        self.gioco_nestratto_dark_fg_color = "white"
        self.gioco_tabellone_unset_dark_bg_color = "gray"
        self.gioco_tabellone_unset_dark_fg_color = "white"
        self.gioco_tabellone_set_dark_bg_color = "black"
        self.gioco_tabellone_set_dark_fg_color = "white"
        self.gioco_schedine_unset_dark_bg_color = "gray"
        self.gioco_schedine_unset_dark_fg_color = "white"
        self.gioco_schedine_set_dark_bg_color = "black"
        self.gioco_schedine_set_dark_fg_color = "white"
        self.gioco_schedine_disabled_dark_fg_color = "white"
        self.gioco_logs_dark_bg_color = "gray"
        self.gioco_logs_dark_fg_color = "black"
        self.gioco_framedestro_dark_bg_color = "gray"
        self.gioco_classifica_dark_bg_color = "black"
        self.gioco_classifica_titolo_dark_fg_color = "white"
        self.gioco_classifica_tabella_dark_fg_color = "white"
        self.gioco_premi_dark_bg_color = "black"
        self.gioco_premi_titolo_dark_fg_color = "white"
        self.gioco_premi_btns_dark_bg_color = "gray"
        self.gioco_premi_btns_dark_fg_color = "white"

        self.pregioco_sfondo_dark_bg_color = "black"
        self.pregioco_titolo_dark_bg_color = "black"
        self.pregioco_titolo_dark_fg_color = "white"
        self.pregioco_labels_dark_bg_color = "black"
        self.pregioco_labels_dark_fg_color = "white"
        self.pregioco_options_dark_bg_color = "gray"
        self.pregioco_options_dark_fg_color = "white"
        self.pregioco_rbtn_circle_dark_bg_color = "black"

        self.impostazioni_sfondo_dark_bg_color = "black"
        self.impostazioni_titolo_dark_bg_color = "black"
        self.impostazioni_titolo_dark_fg_color = "white"
        self.impostazioni_labels_dark_bg_color = "black"
        self.impostazioni_labels_dark_fg_color = "white"
        self.impostazioni_options_dark_bg_color = "gray"
        self.impostazioni_options_dark_fg_color = "white"
        self.impostazioni_rbtn_circle_dark_bg_color = "black"
        
        
        
        """------------------   CHIARO   -------------------"""
        self.punteggio_sfondo_ligth_bg_color = "#9400D3"
        self.punteggio_titolo_ligth_bg_color = "#9400D3"
        self.punteggio_titolo_ligth_fg_color = "blue"
        self.punteggio_labels_ligth_bg_color = "#9400D3"
        self.punteggio_labels_ligth_fg_color = "blue"

        self.menu_sfondo_ligth_bg_color = "orange"
        self.menu_titolo_ligth_bg_color = "orange"
        self.menu_titolo_ligth_fg_color = "black"
        self.menu_buttons_ligth_bg_color = "orange"
        self.menu_buttons_ligth_fg_color = "black"

        self.gioco_sfondo_ligth_bg_color = "green"
        self.gioco_titolo_ligth_bg_color = "green"
        self.gioco_titolo_ligth_fg_color = "black"
        self.gioco_label_nestratto_ligth_bg_color = "gray"
        self.gioco_label_nestratto_ligth_fg_color = "black"
        self.gioco_nestratto_ligth_bg_color = "green"
        self.gioco_nestratto_ligth_fg_color = "white"
        self.gioco_tabellone_unset_ligth_bg_color = "orange"
        self.gioco_tabellone_unset_ligth_fg_color = "black"
        self.gioco_tabellone_set_ligth_bg_color = "red"
        self.gioco_tabellone_set_ligth_fg_color = "black"
        self.gioco_schedine_unset_ligth_bg_color = "orange"
        self.gioco_schedine_unset_ligth_fg_color = "black"
        self.gioco_schedine_set_ligth_bg_color = "red"
        self.gioco_schedine_set_ligth_fg_color = "black"
        self.gioco_schedine_disabled_ligth_fg_color = "black"
        self.gioco_logs_ligth_bg_color = "#0FFFF0"
        self.gioco_logs_ligth_fg_color = "blue"
        self.gioco_framedestro_ligth_bg_color = "#A0522D"
        self.gioco_classifica_ligth_bg_color = "gray"
        self.gioco_classifica_titolo_ligth_fg_color = "black"
        self.gioco_classifica_tabella_ligth_fg_color = "black"
        self.gioco_premi_ligth_bg_color = "red"
        self.gioco_premi_titolo_ligth_fg_color = "yellow"
        self.gioco_premi_btns_ligth_bg_color = "orange"
        self.gioco_premi_btns_ligth_fg_color = "black"

        self.pregioco_sfondo_ligth_bg_color = "red"
        self.pregioco_titolo_ligth_bg_color = "red"
        self.pregioco_titolo_ligth_fg_color = "black"
        self.pregioco_labels_ligth_bg_color = "red"
        self.pregioco_labels_ligth_fg_color = "black"
        self.pregioco_options_ligth_bg_color = "orange"
        self.pregioco_options_ligth_fg_color = "black"
        self.pregioco_rbtn_circle_ligth_bg_color = "red"

        self.impostazioni_sfondo_ligth_bg_color = "#0040ff"
        self.impostazioni_titolo_ligth_bg_color = "#0040ff"
        self.impostazioni_titolo_ligth_fg_color = "black"
        self.impostazioni_labels_ligth_bg_color = "#0040ff"
        self.impostazioni_labels_ligth_fg_color = "black"
        self.impostazioni_options_ligth_bg_color = "#0080ff"
        self.impostazioni_options_ligth_fg_color = "black"
        self.impostazioni_rbtn_circle_ligth_bg_color = "#0080ff"
        
    def checkTema(self):
        # Verifica quale tema si ha selezionato
        self.frameGiocoCPU.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameMenu.grid_forget()
        self.framePreGiocoCPU.grid_forget()
        self.framePreGiocoGioc.grid_forget()

        #self.frameImpostazioni.pack_forget()
        #self.frameGioco.pack_forget()
        #self.frameMenu.pack_forget()

        if self.tema.get() == "Normale":
            self.punteggio_sfondo_bg_color = self.punteggio_sfondo_ligth_bg_color
            self.punteggio_titolo_bg_color = self.punteggio_titolo_ligth_bg_color
            self.punteggio_titolo_fg_color = self.punteggio_titolo_ligth_fg_color
            self.punteggio_labels_bg_color = self.punteggio_labels_ligth_bg_color
            self.punteggio_labels_fg_color = self.punteggio_labels_ligth_fg_color

            self.menu_sfondo_bg_color = self.menu_sfondo_ligth_bg_color               
            self.menu_titolo_bg_color = self.menu_titolo_ligth_bg_color               
            self.menu_titolo_fg_color = self.menu_titolo_ligth_fg_color               
            self.menu_buttons_bg_color = self.menu_buttons_ligth_bg_color              
            self.menu_buttons_fg_color = self.menu_buttons_ligth_fg_color              
                                          
            self.gioco_sfondo_bg_color = self.gioco_sfondo_ligth_bg_color              
            self.gioco_titolo_bg_color = self.gioco_titolo_ligth_bg_color              
            self.gioco_titolo_fg_color = self.gioco_titolo_ligth_fg_color              
            self.gioco_label_nestratto_bg_color = self.gioco_label_nestratto_ligth_bg_color     
            self.gioco_label_nestratto_fg_color = self.gioco_label_nestratto_ligth_fg_color     
            self.gioco_nestratto_bg_color = self.gioco_nestratto_ligth_bg_color           
            self.gioco_nestratto_fg_color = self.gioco_nestratto_ligth_fg_color           
            self.gioco_tabellone_unset_bg_color = self.gioco_tabellone_unset_ligth_bg_color     
            self.gioco_tabellone_unset_fg_color = self.gioco_tabellone_unset_ligth_fg_color     
            self.gioco_tabellone_set_bg_color = self.gioco_tabellone_set_ligth_bg_color       
            self.gioco_tabellone_set_fg_color = self.gioco_tabellone_set_ligth_fg_color       
            self.gioco_schedine_unset_bg_color = self.gioco_schedine_unset_ligth_bg_color      
            self.gioco_schedine_unset_fg_color = self.gioco_schedine_unset_ligth_fg_color      
            self.gioco_schedine_set_bg_color = self.gioco_schedine_set_ligth_bg_color        
            self.gioco_schedine_set_fg_color = self.gioco_schedine_set_ligth_fg_color
            self.gioco_schedine_disabled_fg_color = self.gioco_schedine_disabled_ligth_fg_color
            self.gioco_logs_bg_color = self.gioco_logs_ligth_bg_color
            self.gioco_logs_fg_color = self.gioco_logs_ligth_fg_color
            self.gioco_framedestro_bg_color = self.gioco_framedestro_ligth_bg_color
            self.gioco_classifica_bg_color = self.gioco_classifica_ligth_bg_color
            self.gioco_classifica_titolo_fg_color = self.gioco_classifica_titolo_ligth_fg_color
            self.gioco_classifica_tabella_fg_color = self.gioco_classifica_tabella_ligth_fg_color
            self.gioco_premi_bg_color = self.gioco_premi_ligth_bg_color
            self.gioco_premi_titolo_fg_color = self.gioco_premi_titolo_ligth_fg_color
            self.gioco_premi_btns_bg_color = self.gioco_premi_btns_ligth_bg_color
            self.gioco_premi_btns_fg_color = self.gioco_premi_btns_ligth_fg_color
            
            self.pregioco_sfondo_bg_color = self.pregioco_sfondo_ligth_bg_color 
            self.pregioco_titolo_bg_color = self.pregioco_titolo_ligth_bg_color 
            self.pregioco_titolo_fg_color = self.pregioco_titolo_ligth_fg_color 
            self.pregioco_labels_bg_color = self.pregioco_labels_ligth_bg_color 
            self.pregioco_labels_fg_color = self.pregioco_labels_ligth_fg_color 
            self.pregioco_options_bg_color =self.pregioco_options_ligth_bg_color
            self.pregioco_options_fg_color =self.pregioco_options_ligth_fg_color
            self.pregioco_rbtn_circle_bg_color = self.pregioco_rbtn_circle_ligth_bg_color

            self.impostazioni_sfondo_bg_color = self.impostazioni_sfondo_ligth_bg_color       
            self.impostazioni_titolo_bg_color = self.impostazioni_titolo_ligth_bg_color       
            self.impostazioni_titolo_fg_color = self.impostazioni_titolo_ligth_fg_color       
            self.impostazioni_labels_bg_color = self.impostazioni_labels_ligth_bg_color       
            self.impostazioni_labels_fg_color = self.impostazioni_labels_ligth_fg_color       
            self.impostazioni_options_bg_color = self.impostazioni_options_ligth_bg_color      
            self.impostazioni_options_fg_color = self.impostazioni_options_ligth_fg_color      
            self.impostazioni_rbtn_circle_bg_color = self.impostazioni_rbtn_circle_ligth_bg_color  

            self.CreateWidgets()
            self.frameGiocoCPU.grid_forget()
            self.frameGiocoGioc.grid_forget()
            self.frameImpostazioni.grid_forget()
            self.frameMenu.grid_forget()
            self.framePreGiocoCPU.grid_forget()
            self.framePreGiocoGioc.grid_forget()
            #self.frameImpostazioni.pack_forget()
            #self.frameGioco.pack_forget()
            #self.frameMenu.pack_forget()

        elif self.tema.get() == "Scuro":
            self.punteggio_sfondo_bg_color = self.punteggio_sfondo_dark_bg_color
            self.punteggio_titolo_bg_color = self.punteggio_titolo_dark_bg_color
            self.punteggio_titolo_fg_color = self.punteggio_titolo_dark_fg_color
            self.punteggio_labels_bg_color = self.punteggio_labels_dark_bg_color
            self.punteggio_labels_fg_color = self.punteggio_labels_dark_fg_color

            self.menu_sfondo_bg_color = self.menu_sfondo_dark_bg_color               
            self.menu_titolo_bg_color = self.menu_titolo_dark_bg_color               
            self.menu_titolo_fg_color = self.menu_titolo_dark_fg_color               
            self.menu_buttons_bg_color = self.menu_buttons_dark_bg_color              
            self.menu_buttons_fg_color = self.menu_buttons_dark_fg_color              
                                          
            self.gioco_sfondo_bg_color = self.gioco_sfondo_dark_bg_color              
            self.gioco_titolo_bg_color = self.gioco_titolo_dark_bg_color              
            self.gioco_titolo_fg_color = self.gioco_titolo_dark_fg_color              
            self.gioco_label_nestratto_bg_color = self.gioco_label_nestratto_dark_bg_color     
            self.gioco_label_nestratto_fg_color = self.gioco_label_nestratto_dark_fg_color     
            self.gioco_nestratto_bg_color = self.gioco_nestratto_dark_bg_color           
            self.gioco_nestratto_fg_color = self.gioco_nestratto_dark_fg_color           
            self.gioco_tabellone_unset_bg_color = self.gioco_tabellone_unset_dark_bg_color     
            self.gioco_tabellone_unset_fg_color = self.gioco_tabellone_unset_dark_fg_color     
            self.gioco_tabellone_set_bg_color = self.gioco_tabellone_set_dark_bg_color       
            self.gioco_tabellone_set_fg_color = self.gioco_tabellone_set_dark_fg_color       
            self.gioco_schedine_unset_bg_color = self.gioco_schedine_unset_dark_bg_color      
            self.gioco_schedine_unset_fg_color = self.gioco_schedine_unset_dark_fg_color      
            self.gioco_schedine_set_bg_color = self.gioco_schedine_set_dark_bg_color        
            self.gioco_schedine_set_fg_color = self.gioco_schedine_set_dark_fg_color
            self.gioco_schedine_disabled_fg_color = self.gioco_schedine_disabled_dark_fg_color
            self.gioco_logs_bg_color = self.gioco_logs_dark_bg_color
            self.gioco_logs_fg_color = self.gioco_logs_dark_fg_color
            self.gioco_framedestro_bg_color = self.gioco_framedestro_dark_bg_color
            self.gioco_classifica_bg_color = self.gioco_classifica_dark_bg_color
            self.gioco_classifica_titolo_fg_color = self.gioco_classifica_titolo_dark_fg_color
            self.gioco_classifica_tabella_fg_color = self.gioco_classifica_tabella_dark_fg_color
            self.gioco_premi_bg_color = self.gioco_premi_dark_bg_color
            self.gioco_premi_titolo_fg_color = self.gioco_premi_titolo_dark_fg_color
            self.gioco_premi_btns_bg_color = self.gioco_premi_btns_dark_bg_color
            self.gioco_premi_btns_fg_color = self.gioco_premi_btns_dark_fg_color

            self.pregioco_sfondo_bg_color = self.pregioco_sfondo_dark_bg_color
            self.pregioco_titolo_bg_color = self.pregioco_titolo_dark_bg_color
            self.pregioco_titolo_fg_color = self.pregioco_titolo_dark_fg_color
            self.pregioco_labels_bg_color = self.pregioco_labels_dark_bg_color
            self.pregioco_labels_fg_color = self.pregioco_labels_dark_fg_color
            self.pregioco_options_bg_color = self.pregioco_options_dark_bg_color
            self.pregioco_options_fg_color = self.pregioco_options_dark_fg_color
            self.pregioco_rbtn_circle_bg_color = self.pregioco_rbtn_circle_dark_bg_color

            self.impostazioni_sfondo_bg_color = self.impostazioni_sfondo_dark_bg_color       
            self.impostazioni_titolo_bg_color = self.impostazioni_titolo_dark_bg_color       
            self.impostazioni_titolo_fg_color = self.impostazioni_titolo_dark_fg_color       
            self.impostazioni_labels_bg_color = self.impostazioni_labels_dark_bg_color       
            self.impostazioni_labels_fg_color = self.impostazioni_labels_dark_fg_color       
            self.impostazioni_options_bg_color = self.impostazioni_options_dark_bg_color      
            self.impostazioni_options_fg_color = self.impostazioni_options_dark_fg_color      
            self.impostazioni_rbtn_circle_bg_color = self.impostazioni_rbtn_circle_dark_bg_color  

            self.CreateWidgets()
            self.frameGiocoCPU.grid_forget()
            self.frameGiocoGioc.grid_forget()
            self.frameImpostazioni.grid_forget()
            self.frameMenu.grid_forget()
            self.framePreGiocoCPU.grid_forget()
            self.framePreGiocoGioc.grid_forget()
            #self.frameImpostazioni.pack_forget()
            #self.frameGioco.pack_forget()
            #self.frameMenu.pack_forget()

    def CreateWidgets(self):
#TODO*****************************************************************************************************************\
# *******************************************  CLASSIFICA  ***********************************************************\
# *********************************************************************************************************************

        self.framePunteggio=tk.Frame(self, bg=self.punteggio_sfondo_bg_color)

        self.btnTornaAlMenuClassifica=tk.Button(self.framePunteggio, text="←", bg=self.punteggio_sfondo_bg_color, fg=self.punteggio_titolo_fg_color, highlightthickness=0, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bd=0, command=lambda:self.MenuSuono(), relief="solid")
        self.btnTornaAlMenuClassifica.grid(row=1, column=0)

        self.lblTitoloClassifica=tk.Label(self.framePunteggio, text="Classifica Personale", bg=self.punteggio_titolo_bg_color, fg=self.punteggio_titolo_fg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54))))
        self.lblTitoloClassifica.grid(row=1, column=1)

        #self.txtStoricoPartite=tk.Text()
        self.lblPunteggioTotale=tk.Label(self.framePunteggio, text=self.punteggio, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.punteggio_labels_bg_color, fg=self.punteggio_labels_fg_color)
        self.lblPunteggioTotale.grid(row=2, column=1)

        self.framePunteggio.rowconfigure(2, weight=1)
        self.framePunteggio.columnconfigure(1, weight=1)


#TODO*****************************************************************************************************************\
# *****************************************  MENU PRINCIPALE  ********************************************************\
# *********************************************************************************************************************

        self.frameMenu=tk.Frame(self, bg=self.menu_sfondo_bg_color)


        #margineAltoSx=tk.Label(self.frameMenu, bg="green", width=20).grid(row=0, column=0)
        #margineAltoDx=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, width=20).grid(row=0, column=2)

        spazioTraTitoloETop=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))).grid(row=0, column=1) #30

        self.btnClassificaPersonale=tk.Button(self.frameMenu, text="{}", command=lambda:self.PunteggioSuono(), bg=self.menu_sfondo_bg_color, fg=self.menu_titolo_fg_color, font=("Helvetica", 15, "bold"))
        self.btnClassificaPersonale.grid(row=0, column=0, sticky="s")

        self.lblTitoloMenu=tk.Label(self.frameMenu, text="Tombolone", bg=self.menu_titolo_bg_color, fg=self.menu_titolo_fg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54)))) #50
        self.lblTitoloMenu.grid(row=1, column=1, sticky="nesw")

        #spazioTraTitoloEScelte=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))).grid(row=2, column=1)


        frameBtns=tk.Frame(self.frameMenu, bg=self.menu_sfondo_bg_color)

        self.btnGioca=tk.Button(frameBtns, text="Gioca", width=14, command=lambda:self.TipoGiocoSuono(), bg=self.menu_buttons_bg_color, fg=self.menu_buttons_fg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))))
        #self.btnGioca.bind("<Return>", (lambda event: self.Gioca()))
        self.btnGioca.grid(row=0, column=1)

        spazioTraScelte=tk.Label(frameBtns, bg=self.menu_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=1, column=1) #20

        self.btnImpostazioni=tk.Button(frameBtns, text="Impostazioni", width=14, command=lambda:self.ImpostazioniSuono(), font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), fg=self.menu_buttons_fg_color, bg=self.menu_buttons_bg_color)
        self.btnImpostazioni.grid(row=2, column=1)

        spazioTraScelte1=tk.Label(frameBtns, bg=self.menu_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=3, column=1)

        self.btnEsci=tk.Button(frameBtns, text="Esci", command=lambda: self.EsciSuono(), fg=self.menu_buttons_fg_color, bg=self.menu_buttons_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))))
        self.btnEsci.grid(row=4, column=1)


        frameBtns.grid(row=2, column=1)

        spazioTraScelteEBottom=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))).grid(row=3, column=1)

        self.frameMenu.columnconfigure(1, weight=1)
        self.frameMenu.rowconfigure(2, weight=2)

#TODO*****************************************************************************************************************\
# **********************************************  GIOCO CPU  *********************************************************\
# *********************************************************************************************************************

        self.frameGiocoCPU = tk.Frame(self, bg=self.gioco_sfondo_bg_color)
        frameSchedine = tk.LabelFrame(self.frameGiocoCPU, text=" Schedine:", bg=self.gioco_sfondo_bg_color, fg=self.gioco_schedine_unset_fg_color)

        #margineAltoDx=tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color, width=14).grid(row=0, column=0)

        #tk.Label(self.frameGioco, text="", width=160, bg=self.gioco_sfondo_bg_color, font=("Helvetica", 11, "bold")).grid(row=0, column=0, columnspan=10, sticky="nesw")

        self.btnTornaAlMenuGioco=tk.Button(self.frameGiocoCPU, text="←", bg=self.gioco_sfondo_bg_color, fg=self.gioco_schedine_set_fg_color, highlightthickness=0, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bd=0, command=lambda:self.TornaAlMenuGiocaSuono(), relief="solid")
        self.btnTornaAlMenuGioco.grid(row=0, column=0, columnspan=2, sticky="w")
        #self.update()
        #print("Altezza",btnTornaAlMenu.winfo_height())
        #print("larghezza", btnTornaAlMenu.winfo_width())
        #fakebtnTornaAlMenu = tk.Button(self.frameGioco, bg=self.gioco_sfondo_bg_color, highlightthickness=0, state=tk.DISABLED, relief=tk.FLAT, height=4, width=17).grid(row=1, column=9)



        #spazioTraTitoloESchedine=tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=2, column=0)

        frameLogs=tk.LabelFrame(self.frameGiocoCPU, text=" Logs:", bg=self.gioco_logs_bg_color, fg=self.gioco_titolo_fg_color)

        self.txtLogs=tk.Text(frameLogs, width=45, height=6, font=("Helvetica", int((self.altezza/85) + (self.larghezza/151))), state=tk.DISABLED, bd=0, bg=self.gioco_logs_bg_color, fg=self.gioco_logs_fg_color)
        self.txtLogs.insert(1.0, "")
        self.txtLogs.grid()
        scrollTxtLogs=tk.Scrollbar(self.frameGiocoCPU, command=self.txtLogs.xview())
        self.txtLogs.configure(yscrollcommand=scrollTxtLogs.set)

        frameLogs.grid(row=2, column=2, sticky="n", pady=30)


        frameDestro=tk.Frame(self.frameGiocoCPU, bg=self.gioco_framedestro_bg_color)

        frameNomeGioc=tk.LabelFrame(frameDestro, text=" Nome:", bg=self.gioco_framedestro_bg_color, fg=self.gioco_titolo_fg_color)

        #frameNome=tk.LabelFrame(frameNomeGioc, text=" Nome:", bg=self.gioco_framedestro_bg_color, fg=self.gioco_titolo_fg_color)
        nick=str(self.nickname.get())
        self.lblTitoloGiocoCPU = tk.Label(frameNomeGioc, text=nick, justify=tk.CENTER, width=12, fg=self.gioco_titolo_fg_color, bg=self.gioco_framedestro_bg_color, font=('Helvetica', int((self.altezza/102) + (self.larghezza/182))))
        self.lblTitoloGiocoCPU.grid(row=1, column=1)
        #frameNome.grid(row=1, column=1)

        self.btnPrevPlayerCPU=tk.Button(frameNomeGioc, text="<", highlightthickness=0, disabledforeground=self.gioco_framedestro_bg_color, state=tk.DISABLED, bg=self.gioco_label_nestratto_bg_color, fg=self.gioco_label_nestratto_fg_color, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182)), "bold"), command=lambda:self.switchPlayerCPUSuono("<"))
        self.btnPrevPlayerCPU.grid(row=1, column=0, sticky="w")
        self.btnNextPlayerCPU=tk.Button(frameNomeGioc, text=">", highlightthickness=0, disabledforeground=self.gioco_framedestro_bg_color, bg=self.gioco_label_nestratto_bg_color, fg=self.gioco_label_nestratto_fg_color, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182)), "bold"), command=lambda:self.switchPlayerCPUSuono(">"))
        self.btnNextPlayerCPU.grid(row=1, column=2, sticky="e")

        frameNomeGioc.grid(row=0, column=0, pady=10)


        framePremiRimanenti=tk.LabelFrame(frameDestro, text=" Premi Disponibili:", bg=self.gioco_premi_bg_color, fg=self.gioco_premi_titolo_fg_color)

        blank=tk.Label(framePremiRimanenti, text="", width=2, bg=self.gioco_premi_bg_color).grid(row=0, column=0)

        self.btnAmbo=tk.Button(framePremiRimanenti, text="AMBO", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnAmbo.grid(row=1, column=1, pady=30, sticky="nesw")

        self.btnTerna=tk.Button(framePremiRimanenti, text="TERNA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnTerna.grid(row=1, column=3, pady=30, sticky="nesw")

        blank2=tk.Label(framePremiRimanenti, text="", width=2, bg=self.gioco_premi_bg_color).grid(row=2, column=2)

        self.btnQuaterna=tk.Button(framePremiRimanenti, text="QUATERNA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnQuaterna.grid(row=2, column=1, pady=30, sticky="nesw")

        self.btnCinquina=tk.Button(framePremiRimanenti, text="CINQUINA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/290))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnCinquina.grid(row=2, column=3, pady=30, sticky="nesw")

        blank1=tk.Label(framePremiRimanenti, text="", width=2, bg=self.gioco_premi_bg_color).grid(row=5, column=4)

        framePremiRimanenti.rowconfigure(1, weight=1)
        #framePremiRimanenti.rowconfigure(2, weight=1)
        framePremiRimanenti.rowconfigure(3, weight=1)
        #framePremiRimanenti.rowconfigure(4, weight=1)
        framePremiRimanenti.columnconfigure(1, weight=1)
        framePremiRimanenti.columnconfigure(3, weight=1)

        framePremiRimanenti.grid(row=1, column=0, padx=30, sticky="nesw")


        self.frameClassProvCPU=tk.LabelFrame(frameDestro, text=" Classifica:", bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_titolo_fg_color)

        self.frameClassProvCPU.columnconfigure(0, weight=1)
        self.frameClassProvCPU.columnconfigure(1, weight=1)
        self.frameClassProvCPU.columnconfigure(2, weight=1)

        lblPos=tk.Label(self.frameClassProvCPU, text="Posizione", font=("Helvetica", int((self.altezza/128) + (self.larghezza/228)), "bold"), borderwidth=0.5, highlightbackground="black", relief=tk.SOLID, bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color).grid(row=0, column=0, sticky="nesw")
        lblNome=tk.Label(self.frameClassProvCPU, text="Nome", font=("Helvetica", int((self.altezza/128) + (self.larghezza/228)), "bold"), borderwidth=0.5, highlightbackground="black", relief=tk.SOLID, bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color).grid(row=0, column=1, sticky="nesw")
        lblPunt=tk.Label(self.frameClassProvCPU, text="Punteggio", font=("Helvetica", int((self.altezza/128) + (self.larghezza/228)), "bold"), borderwidth=0.5, highlightbackground="black", relief=tk.SOLID, bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color).grid(row=0, column=2, sticky="nesw")


        self.frameClassProvCPU.grid(row=3, column=0, pady=50, padx=30, sticky="n")

        frameDestro.rowconfigure(2, weight=1)
        frameDestro.rowconfigure(3, weight=1)

        frameDestro.grid(row=0, rowspan=3, column=3, pady=30, padx=35, sticky="nesw")

        #tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=3, column=0)

        frameTabNEstr=tk.Frame(self.frameGiocoCPU, bg=self.gioco_sfondo_bg_color)

        # Tabellone
        #todo DA COMPATTARE
        frameTabellone=tk.LabelFrame(frameTabNEstr, text=" Tabellone:", highlightbackground="black", highlightthickness=1, bg=self.gioco_tabellone_unset_bg_color, fg=self.gioco_titolo_fg_color)
        self.arrTabellone=[]
        row=0
        column=-1
        for i in range(90):
            column=column+1
            if i == 10:
                row = 1
                column=0
            elif i == 20:
                row = 2
                column=0
            elif i == 30:
                row = 3
                column=0
            elif i == 40:
                row = 4
                column=0
            elif i == 50:
                row = 5
                column=0
            elif i == 60:
                row = 6
                column=0
            elif i == 70:
                row = 7
                column=0
            elif i == 80:
                row = 8
                column=0
            elif i == 90:
                row = 9
                column=0
            lbl=tk.Label(frameTabellone, text=i+1, font=("Helvetica", int((self.altezza/120) + (self.larghezza/190))), width=self.larghezzaCellaTabellone, height=2, bg=self.gioco_tabellone_unset_bg_color, fg=self.gioco_tabellone_unset_fg_color) #8 / 10
            lbl.grid(row=row, column=column, sticky="nesw")
            tupla1 = (lbl, i+1)
            self.arrTabellone.append(lbl)
        frameTabellone.grid(row=0, column=0)
        #self.update()
        #print("larghezza: ", frameTabellone.winfo_width())
        #print("altezza: ", frameTabellone.winfo_height())
        #faketabellone=tk.Frame(self.frameGioco, bg=self.gioco_sfondo_bg_color, height=191, width=182).grid(row=0, rowspan=4, column=1, columnspan=3)
        #frameTabellone.grid(row=0, column=0, sticky="ne", padx=50, pady=20)

        frameNEstratto = tk.Frame(frameTabNEstr, bg=self.gioco_sfondo_bg_color)

        self.btnNEstrattoCPU = tk.Button(frameNEstratto, text="Estrai", command=lambda: self.estraiCPUSuono(), bg=self.gioco_label_nestratto_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)), "bold"),fg=self.gioco_label_nestratto_fg_color)
        self.btnNEstrattoCPU.grid(row=0, column=0)
        self.lblNEstrattoCPU = tk.Label(frameNEstratto, text="", fg=self.gioco_nestratto_fg_color, bg=self.gioco_nestratto_bg_color, width=2, height=2, font=('Helvetica', int((self.altezza/102) + (self.larghezza/182)))) #15
        self.lblNEstrattoCPU.grid(row=0, column=1, padx=20)

        frameNEstratto.grid(row=1, column=0, pady=20)

        frameTabNEstr.grid(row=1, rowspan=2, column=1, pady=30, padx=35, sticky="w")

        #tk.Label(self.frameGioco, text="", bg="red").grid(row=5, column=0)

        #Schedine segnaposto                                          SCHEDINE
        self.arrSchedineCPU = []
        h = 0
        for nSchedina in range(self.nSchedineCPU.get() * 2):
            h += 1
            arrSchedina = []
            arrRow1 = []
            arrRow2 = []
            arrRow3 = []
            schedina = tk.Frame(frameSchedine, bg=self.gioco_sfondo_bg_color)
            if (nSchedina % 2) == 0:
                # Riga
                for riga in range(3):
                    # Colonna
                    for colonna in range(9):
                        cella = tk.Button(schedina, text="N", bg=self.gioco_schedine_unset_bg_color, disabledforeground=self.gioco_schedine_disabled_fg_color, font=("Helvetica", int((self.altezza/100) + (self.larghezza/170))), width=self.larghezzaCellaSchedine, bd=1, highlightthickness=0, highlightcolor="black", relief=tk.RAISED)
                        cella.grid(row=riga, column=colonna)
                        if riga==0:
                            arrRow1.append(cella)
                            if colonna==8:
                                arrSchedina.append(arrRow1)
                        if riga==1:
                            arrRow2.append(cella)
                            if colonna==8:
                                arrSchedina.append(arrRow2)
                        if riga==2:
                            arrRow3.append(cella)
                            if colonna==8:
                                arrSchedina.append(arrRow3)
                self.arrSchedineCPU.append(arrSchedina)
            else:
                if self.nSchedineCPU.get() > 0 and self.nSchedineCPU.get() < 4:
                    tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=h+1, column=0)
                elif self.nSchedineCPU.get() == 4:
                    tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=1, column=h)
                elif self.nSchedineCPU.get() == 5:
                    if nSchedina < 5:
                        tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=1, column=h)
                    else:
                        tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=h + 2, column=2)
                else:
                    if nSchedina < 5:
                        tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=1, column=h)
                    else:
                        tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=h + 1, column=1)

            if self.nSchedineCPU.get() > 0 and self.nSchedineCPU.get() < 4:
                schedina.grid(row=h+1, column=0)
            elif self.nSchedineCPU.get() == 4:
                if nSchedina + 1 <= 4:
                    schedina.grid(row=0, column=h)
                    if nSchedina + 1 == 4:
                        h = 0
                elif nSchedina + 1 > 4 and nSchedina + 1 <= 8:
                    schedina.grid(row=2, column=h)
                    if nSchedina + 1 == 8:
                        h = 0
            elif self.nSchedineCPU.get() == 5:
                if nSchedina + 1 <= 4:
                    schedina.grid(row=0, column=h)
                    if nSchedina + 1 == 4:
                        h = 0
                elif nSchedina + 1 > 4 and nSchedina + 1 <= 8:
                    schedina.grid(row=2, column=h)
                    if nSchedina + 1 == 8:
                        h = 0
                else:
                    schedina.grid(row=4, column=h, columnspan=3)
                    h = 0
            elif self.nSchedineCPU.get() == 6:
                if nSchedina + 1 <= 4:
                    schedina.grid(row=0, column=h)
                    if nSchedina + 1 == 4:
                        h = 0
                elif nSchedina + 1 > 4 and nSchedina + 1 <= 8:
                    schedina.grid(row=2, column=h)
                    if nSchedina + 1 == 8:
                        h = 0
                elif nSchedina + 1 > 8 and nSchedina + 1 <= 12:
                    schedina.grid(row=4, column=h)
                    if nSchedina + 1 == 12:
                        h = 0

        #schedine
        for i in range(len(self.arrSchedineCPU)):
            #righe
            for t in range(len(self.arrSchedineCPU[i])):
                #celle
                for l in range(len(self.arrSchedineCPU[i][t])):
                    #print(self.arrSchedine[i][t][l].cget("text"))
                    self.setCommandCelleCPU(i, t, l)

        #tk.Label(self.frameGioco, text="", bg="red", height=1).grid(row=9, column=2)

        #self.frameGioco.rowconfigure(2, weight=1)
        #self.frameGioco.columnconfigure(0, weight=1)
        self.frameGiocoCPU.columnconfigure(2, weight=1)
        #self.frameGioco.columnconfigure(4, weight=1)
        #self.frameGioco.rowconfigure(2, weight=1)
        self.frameGiocoCPU.rowconfigure(1, weight=1)

        frameSchedine.grid(row=1, column=2)


#TODO*****************************************************************************************************************\
# ******************************************  GIOCO GIOCATORI  *******************************************************\
# *********************************************************************************************************************

        self.frameGiocoGioc = tk.Frame(self, bg=self.gioco_sfondo_bg_color)

        #self.lblSfondoGioco=tk.Label(self.frameGioco, image=self.imgSfondoGioco).grid(row=0, column=0, columnspan=10, rowspan=10, sticky="nesw")

        frameSchedine = tk.LabelFrame(self.frameGiocoGioc, text=" Schedine:", bg=self.gioco_sfondo_bg_color, fg=self.gioco_schedine_unset_fg_color)

        #margineAltoDx=tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color, width=14).grid(row=0, column=0)

        #tk.Label(self.frameGioco, text="", width=160, bg=self.gioco_sfondo_bg_color, font=("Helvetica", 11, "bold")).grid(row=0, column=0, columnspan=10, sticky="nesw")

        self.btnTornaAlMenuGioco=tk.Button(self.frameGiocoGioc, text="←", bg=self.gioco_sfondo_bg_color, fg=self.gioco_schedine_set_fg_color, highlightthickness=0, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bd=0, command=lambda:self.TornaAlMenuGiocaSuono(), relief="solid")
        self.btnTornaAlMenuGioco.grid(row=0, column=0, columnspan=2, sticky="w")
        #self.update()
        #print("Altezza",btnTornaAlMenu.winfo_height())
        #print("larghezza", btnTornaAlMenu.winfo_width())
        #fakebtnTornaAlMenu = tk.Button(self.frameGioco, bg=self.gioco_sfondo_bg_color, highlightthickness=0, state=tk.DISABLED, relief=tk.FLAT, height=4, width=17).grid(row=1, column=9)



        #spazioTraTitoloESchedine=tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=2, column=0)

        frameLogs=tk.LabelFrame(self.frameGiocoGioc, text=" Logs:", bg=self.gioco_logs_bg_color, fg=self.gioco_titolo_fg_color)

        self.txtLogs=tk.Text(frameLogs, width=45, height=6, font=("Helvetica", int((self.altezza/85) + (self.larghezza/151))), state=tk.DISABLED, bd=0, bg=self.gioco_logs_bg_color, fg=self.gioco_logs_fg_color)
        self.txtLogs.insert(1.0, "")
        self.txtLogs.grid()
        scrollTxtLogs=tk.Scrollbar(self.frameGiocoGioc, command=self.txtLogs.xview())
        self.txtLogs.configure(yscrollcommand=scrollTxtLogs.set)

        frameLogs.grid(row=2, column=2, sticky="n", pady=30)


        self.btnPronto=tk.Button(self.frameGiocoGioc, text="pronto", font=("Helvetica", int((self.altezza/85) + (self.larghezza/151)), "bold"), fg="green", bg="red", command=lambda: self.setPronto())
        self.btnPronto.grid(row=1, column=1, sticky="n", pady=30 ) #sopra a tabellone
        #self.btnPronto.grid(row=2, column=1, sticky="s", pady=40 ) sotto a tabellone e nEstratto
        #self.btnPronto.grid(row=2, column=2, sticky="n")  #in mezzo alle schedine e logs


        frameDestro=tk.Frame(self.frameGiocoGioc, bg=self.gioco_framedestro_bg_color)

        frameNomeGioc=tk.LabelFrame(frameDestro, text=" Nome:", bg=self.gioco_framedestro_bg_color, fg=self.gioco_titolo_fg_color)

        #frameNome=tk.LabelFrame(frameNomeGioc, text=" Nome:", bg=self.gioco_framedestro_bg_color, fg=self.gioco_titolo_fg_color)
        nick=str(self.nickname.get())
        self.lblTitoloGiocoGioc = tk.Label(frameNomeGioc, text=nick, justify=tk.CENTER, width=12, fg=self.gioco_titolo_fg_color, bg=self.gioco_framedestro_bg_color, font=('Helvetica', int((self.altezza/102) + (self.larghezza/182))))
        """self.enTitoloGioco = tk.Entry(frameNomeGioc, text=self.nickname, validate="key", justify=tk.CENTER, width=12, fg=self.gioco_titolo_fg_color, bg=self.gioco_framedestro_bg_color, font=('Helvetica', int((self.altezza/102) + (self.larghezza/182))))
        self.enTitoloGioco.configure(validatecommand=lambda: self.updateNomeGiocatore(self.enTitoloGioco.get(), self.currentPlayer))
        self.enTitoloGioco.grid(row=1, column=1)"""
        self.lblTitoloGiocoGioc.grid(row=1, column=1)
        #frameNome.grid(row=1, column=1)

        self.btnPrevPlayerGioc=tk.Button(frameNomeGioc, text="<", highlightthickness=0, disabledforeground=self.gioco_framedestro_bg_color, state=tk.DISABLED, bg=self.gioco_label_nestratto_bg_color, fg=self.gioco_label_nestratto_fg_color, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182)), "bold"), command=lambda:self.switchPlayerGiocSuono("<"))
        self.btnPrevPlayerGioc.grid(row=1, column=0, sticky="w")
        self.btnNextPlayerGioc=tk.Button(frameNomeGioc, text=">", highlightthickness=0, disabledforeground=self.gioco_framedestro_bg_color, bg=self.gioco_label_nestratto_bg_color, fg=self.gioco_label_nestratto_fg_color, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182)), "bold"), command=lambda:self.switchPlayerGiocSuono(">"))
        self.btnNextPlayerGioc.grid(row=1, column=2, sticky="e")

        frameNomeGioc.grid(row=0, column=0, pady=10)


        framePremiRimanenti=tk.LabelFrame(frameDestro, text=" Premi Disponibili:", bg=self.gioco_premi_bg_color, fg=self.gioco_premi_titolo_fg_color)

        blank=tk.Label(framePremiRimanenti, text="", width=2, bg=self.gioco_premi_bg_color).grid(row=0, column=0)

        self.btnAmbo=tk.Button(framePremiRimanenti, text="AMBO", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnAmbo.grid(row=1, column=1, pady=30, sticky="nesw")

        self.btnTerna=tk.Button(framePremiRimanenti, text="TERNA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnTerna.grid(row=1, column=3, pady=30, sticky="nesw")

        blank2=tk.Label(framePremiRimanenti, text="", width=2, bg=self.gioco_premi_bg_color).grid(row=2, column=2)

        self.btnQuaterna=tk.Button(framePremiRimanenti, text="QUATERNA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnQuaterna.grid(row=2, column=1, pady=30, sticky="nesw")

        self.btnCinquina=tk.Button(framePremiRimanenti, text="CINQUINA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/290))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnCinquina.grid(row=2, column=3, pady=30, sticky="nesw")

        blank1=tk.Label(framePremiRimanenti, text="", width=2, bg=self.gioco_premi_bg_color).grid(row=5, column=4)

        framePremiRimanenti.rowconfigure(1, weight=1)
        #framePremiRimanenti.rowconfigure(2, weight=1)
        framePremiRimanenti.rowconfigure(3, weight=1)
        #framePremiRimanenti.rowconfigure(4, weight=1)
        framePremiRimanenti.columnconfigure(1, weight=1)
        framePremiRimanenti.columnconfigure(3, weight=1)

        framePremiRimanenti.grid(row=1, column=0, padx=30, sticky="nesw")


        self.frameClassProvGioc=tk.LabelFrame(frameDestro, text=" Classifica:", bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_titolo_fg_color)

        self.frameClassProvGioc.columnconfigure(0, weight=1)
        self.frameClassProvGioc.columnconfigure(1, weight=1)
        self.frameClassProvGioc.columnconfigure(2, weight=1)

        lblPos=tk.Label(self.frameClassProvGioc, text="Posizione", font=("Helvetica", int((self.altezza/128) + (self.larghezza/228)), "bold"), borderwidth=0.5, highlightbackground="black", relief=tk.SOLID, bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color).grid(row=0, column=0, sticky="nesw")
        lblNome=tk.Label(self.frameClassProvGioc, text="Nome", font=("Helvetica", int((self.altezza/128) + (self.larghezza/228)), "bold"), borderwidth=0.5, highlightbackground="black", relief=tk.SOLID, bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color).grid(row=0, column=1, sticky="nesw")
        lblPunt=tk.Label(self.frameClassProvGioc, text="Punteggio", font=("Helvetica", int((self.altezza/128) + (self.larghezza/228)), "bold"), borderwidth=0.5, highlightbackground="black", relief=tk.SOLID, bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color).grid(row=0, column=2, sticky="nesw")


        self.frameClassProvGioc.grid(row=3, column=0, pady=50, padx=30, sticky="n")

        frameDestro.rowconfigure(2, weight=1)
        frameDestro.rowconfigure(3, weight=1)

        frameDestro.grid(row=0, rowspan=3, column=3, pady=30, padx=35, sticky="nesw")

        #tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=3, column=0)

        frameTabNEstr=tk.Frame(self.frameGiocoGioc, bg=self.gioco_sfondo_bg_color)

        # Tabellone
        #todo DA COMPATTARE
        frameTabellone=tk.LabelFrame(frameTabNEstr, text=" Tabellone:", highlightbackground="black", highlightthickness=1, bg=self.gioco_tabellone_unset_bg_color, fg=self.gioco_titolo_fg_color)
        self.arrTabellone=[]
        row=0
        column=-1
        for i in range(90):
            column=column+1
            if i == 10:
                row = 1
                column=0
            elif i == 20:
                row = 2
                column=0
            elif i == 30:
                row = 3
                column=0
            elif i == 40:
                row = 4
                column=0
            elif i == 50:
                row = 5
                column=0
            elif i == 60:
                row = 6
                column=0
            elif i == 70:
                row = 7
                column=0
            elif i == 80:
                row = 8
                column=0
            elif i == 90:
                row = 9
                column=0
            lbl=tk.Label(frameTabellone, text=i+1, font=("Helvetica", int((self.altezza/120) + (self.larghezza/190))), width=self.larghezzaCellaTabellone, height=2, bg=self.gioco_tabellone_unset_bg_color, fg=self.gioco_tabellone_unset_fg_color) #8 / 10
            lbl.grid(row=row, column=column, sticky="nesw")
            tupla1 = (lbl, i+1)
            self.arrTabellone.append(lbl)
        frameTabellone.grid(row=0, column=0)
        #self.update()
        #print("larghezza: ", frameTabellone.winfo_width())
        #print("altezza: ", frameTabellone.winfo_height())
        #faketabellone=tk.Frame(self.frameGioco, bg=self.gioco_sfondo_bg_color, height=191, width=182).grid(row=0, rowspan=4, column=1, columnspan=3)
        #frameTabellone.grid(row=0, column=0, sticky="ne", padx=50, pady=20)

        frameNEstratto = tk.Frame(frameTabNEstr, bg=self.gioco_sfondo_bg_color)

        self.btnNEstrattoGioc = tk.Button(frameNEstratto, text="Estrai", command=lambda: self.estraiGiocSuono(), bg=self.gioco_label_nestratto_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)), "bold"),fg=self.gioco_label_nestratto_fg_color)
        self.btnNEstrattoGioc.grid(row=0, column=0)
        self.lblNEstrattoGioc = tk.Label(frameNEstratto, text="", fg=self.gioco_nestratto_fg_color, bg=self.gioco_nestratto_bg_color, width=2, height=2, font=('Helvetica', int((self.altezza/102) + (self.larghezza/182)))) #15
        self.lblNEstrattoGioc.grid(row=0, column=1, padx=20)

        frameNEstratto.grid(row=1, column=0, pady=20)

        frameTabNEstr.grid(row=1, rowspan=2, column=1, pady=30, padx=35, sticky="w")

        #tk.Label(self.frameGioco, text="", bg="red").grid(row=5, column=0)

        #Schedine segnaposto                                          SCHEDINE
        self.arrSchedineGioc = []
        h = 0
        for nSchedina in range(self.nSchedineGioc.get() * 2):
            h += 1
            arrSchedina = []
            arrRow1 = []
            arrRow2 = []
            arrRow3 = []
            schedina = tk.Frame(frameSchedine, bg=self.gioco_sfondo_bg_color)
            if (nSchedina % 2) == 0:
                # Riga
                for riga in range(3):
                    # Colonna
                    for colonna in range(9):
                        cella = tk.Button(schedina, text="N", bg=self.gioco_schedine_unset_bg_color, disabledforeground=self.gioco_schedine_disabled_fg_color, font=("Helvetica", int((self.altezza/100) + (self.larghezza/170))), width=self.larghezzaCellaSchedine, bd=1, highlightthickness=0, highlightcolor="black", relief=tk.RAISED)
                        cella.grid(row=riga, column=colonna)
                        if riga==0:
                            arrRow1.append(cella)
                            if colonna==8:
                                arrSchedina.append(arrRow1)
                        if riga==1:
                            arrRow2.append(cella)
                            if colonna==8:
                                arrSchedina.append(arrRow2)
                        if riga==2:
                            arrRow3.append(cella)
                            if colonna==8:
                                arrSchedina.append(arrRow3)
                self.arrSchedineGioc.append(arrSchedina)
            else:
                if self.nSchedineGioc.get() > 0 and self.nSchedineGioc.get() < 4:
                    tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=h+1, column=0)
                elif self.nSchedineGioc.get() == 4:
                    tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=1, column=h)
                elif self.nSchedineGioc.get() == 5:
                    if nSchedina < 5:
                        tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=1, column=h)
                    else:
                        tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=h + 2, column=2)
                else:
                    if nSchedina < 5:
                        tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=1, column=h)
                    else:
                        tk.Label(frameSchedine, text="  ", font=("Helvetica", int((self.altezza/307) + (self.larghezza/546))), bg=self.gioco_sfondo_bg_color).grid(row=h + 1, column=1)

            if self.nSchedineGioc.get() > 0 and self.nSchedineGioc.get() < 4:
                schedina.grid(row=h+1, column=0)
            elif self.nSchedineGioc.get() == 4:
                if nSchedina + 1 <= 4:
                    schedina.grid(row=0, column=h)
                    if nSchedina + 1 == 4:
                        h = 0
                elif nSchedina + 1 > 4 and nSchedina + 1 <= 8:
                    schedina.grid(row=2, column=h)
                    if nSchedina + 1 == 8:
                        h = 0
            elif self.nSchedineGioc.get() == 5:
                if nSchedina + 1 <= 4:
                    schedina.grid(row=0, column=h)
                    if nSchedina + 1 == 4:
                        h = 0
                elif nSchedina + 1 > 4 and nSchedina + 1 <= 8:
                    schedina.grid(row=2, column=h)
                    if nSchedina + 1 == 8:
                        h = 0
                else:
                    schedina.grid(row=4, column=h, columnspan=3)
                    h = 0
            elif self.nSchedineGioc.get() == 6:
                if nSchedina + 1 <= 4:
                    schedina.grid(row=0, column=h)
                    if nSchedina + 1 == 4:
                        h = 0
                elif nSchedina + 1 > 4 and nSchedina + 1 <= 8:
                    schedina.grid(row=2, column=h)
                    if nSchedina + 1 == 8:
                        h = 0
                elif nSchedina + 1 > 8 and nSchedina + 1 <= 12:
                    schedina.grid(row=4, column=h)
                    if nSchedina + 1 == 12:
                        h = 0

        #schedine
        for i in range(len(self.arrSchedineGioc)):
            #righe
            for t in range(len(self.arrSchedineGioc[i])):
                #celle
                for l in range(len(self.arrSchedineGioc[i][t])):
                    #print(self.arrSchedine[i][t][l].cget("text"))
                    self.setCommandCelleGioc(i, t, l)

        #tk.Label(self.frameGioco, text="", bg="red", height=1).grid(row=9, column=2)

        #self.frameGioco.rowconfigure(2, weight=1)
        #self.frameGioco.columnconfigure(0, weight=1)
        self.frameGiocoGioc.columnconfigure(2, weight=1)
        #self.frameGioco.columnconfigure(4, weight=1)
        #self.frameGioco.rowconfigure(2, weight=1)
        self.frameGiocoGioc.rowconfigure(1, weight=1)

        frameSchedine.grid(row=1, column=2)

#TODO*****************************************************************************************************************\
# *********************************************  TIPO GIOCO  *********************************************************\
# *********************************************************************************************************************
        self.frameTipoGioco=tk.Frame(self, bg=self.pregioco_sfondo_bg_color)
        self.titoloTipoGioco=tk.Label(self.frameTipoGioco, text="Modalita di Gioco", fg=self.pregioco_titolo_fg_color, bg=self.pregioco_titolo_bg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54)))).grid(row=1, column=1, columnspan=3, sticky="nesw")

        spazioTraTitoloETop = tk.Label(self.frameTipoGioco, bg=self.pregioco_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=0, column=2) #20

        frameOpzioniTipoGioco=tk.Frame(self.frameTipoGioco, bg=self.pregioco_sfondo_bg_color)

        self.btnCpuTipoGioco=tk.Button(frameOpzioniTipoGioco, text="CPU", command=lambda: self.PreGiocoCPUSuono(), font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color) #30
        self.btnCpuTipoGioco.grid(row=0, column=1, sticky="w")

        spazioTraColonnes=tk.Label(frameOpzioniTipoGioco, text=" ", width=15, bg=self.pregioco_sfondo_bg_color).grid(row=0, column=2)

        self.btnMultiplayerTipoGioco=tk.Button(frameOpzioniTipoGioco, text="Multiplayer\nLocale", command=lambda: self.PreGiocoGiocSuono(), width=15, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182))), bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color) #15
        self.btnMultiplayerTipoGioco.grid(row=0, column=3, sticky="e")

        spazioTraTitoloETop = tk.Label(frameOpzioniTipoGioco, bg=self.pregioco_sfondo_bg_color, font=("Helvetica", int((self.altezza / 76) + (self.larghezza / 136)))).grid(row=1, column=2)  # 20

        self.btnAnnullaTipoGioco = tk.Button(frameOpzioniTipoGioco, text="Annulla", command=lambda: self.MenuSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.btnAnnullaTipoGioco.grid(row=2, column=1, columnspan=3)

        frameOpzioniTipoGioco.grid(row=3, column=1)

        self.frameTipoGioco.columnconfigure(1, weight=1)
        self.frameTipoGioco.rowconfigure(3, weight=1)

#TODO*****************************************************************************************************************\
# ********************************************  PRE GIOCO CPU  *******************************************************\
# *********************************************************************************************************************
        self.framePreGiocoCPU=tk.Frame(self, bg=self.pregioco_sfondo_bg_color)

        spazioTraTitoloETop = tk.Label(self.framePreGiocoCPU, bg=self.pregioco_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=0, column=2) #20

        self.lblTitoloImpostazioni = tk.Label(self.framePreGiocoCPU, text="Impostazioni Pre Gioco", fg=self.pregioco_titolo_fg_color, bg=self.pregioco_titolo_bg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54)))) #50
        self.lblTitoloImpostazioni.grid(row=1, column=1, columnspan=3, sticky="nesw")

        spazioTraTitoloEScelte = tk.Label(self.framePreGiocoCPU, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_sfondo_bg_color).grid(row=2, column=2) #30



        frameOpzioni=tk.Frame(self.framePreGiocoCPU, bg=self.pregioco_sfondo_bg_color)

        self.lblNickGiocatore=tk.Label(frameOpzioni, text="Nickname", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_labels_bg_color, fg=self.pregioco_labels_fg_color) #30
        self.lblNickGiocatore.grid(row=0, column=1, columnspan=2, sticky="w")

        self.enNickGiocatori=tk.Entry(frameOpzioni, textvariable=self.nickname, width=15, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182))), bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color) #15
        self.enNickGiocatori.grid(row=0, column=2, columnspan=2, sticky="e")

        spazioTraScelte = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=1, column=2) #20

        self.lblNGiocatori = tk.Label(frameOpzioni, text="N Giocatori", fg=self.pregioco_labels_fg_color, bg=self.pregioco_labels_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.lblNGiocatori.grid(row=2, column=1, columnspan=2, sticky="w")

        self.spnNGiocatori = tk.OptionMenu(frameOpzioni, self.nGiocatoriCPU, "2","3","4","5","6","7","8","9","10")
        self.spnNGiocatori.configure(highlightthickness=0, bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), width=5) #20
        self.spnNGiocatori.grid(row=2, column=2, columnspan=2, sticky="e")

        spazioTraScelte1 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=3, column=2) #20

        self.lblNSchedine = tk.Label(frameOpzioni, text="N Schedine", fg=self.pregioco_labels_fg_color, bg=self.pregioco_labels_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.lblNSchedine.grid(row=4, column=1, columnspan=2, sticky="w")

        self.spnNSchedine = tk.OptionMenu(frameOpzioni, self.nSchedineCPU, "1", "2", "3", "4", "5", "6")
        self.spnNSchedine.configure(highlightthickness=0, bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), width=5) #20
        self.spnNSchedine.grid(row=4, column=2, columnspan=2, sticky="e")

        spazioTraScelte2 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=5, column=2) #20

        self.btnAnnulla = tk.Button(frameOpzioni, text="Annulla", command=lambda: self.indietroPreGiocoCPUSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.btnAnnulla.grid(row=6, column=1)

        spazioTraColonne=tk.Label(frameOpzioni, text=" ", width=15, bg=self.pregioco_sfondo_bg_color).grid(row=6, column=2)

        self.btnInizia = tk.Button(frameOpzioni, text="Inizia", command=lambda: self.GiocaCPUSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.btnInizia.grid(row=6, column=3)



        frameOpzioni.grid(row=3, column=1)



        spazioTraScelteEBottom = tk.Label(self.framePreGiocoCPU, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_sfondo_bg_color).grid(row=4, column=1)

        self.framePreGiocoCPU.columnconfigure(1, weight=1)
        self.framePreGiocoCPU.rowconfigure(3, weight=1)


#TODO*****************************************************************************************************************\
# *****************************************  PRE GIOCO GIOCATORI  ****************************************************\
# *********************************************************************************************************************
        self.framePreGiocoGioc=tk.Frame(self, bg=self.pregioco_sfondo_bg_color)

        spazioTraTitoloETop = tk.Label(self.framePreGiocoGioc, bg=self.pregioco_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=0, column=2) #20

        self.lblTitoloImpostazioni = tk.Label(self.framePreGiocoGioc, text="Impostazioni Pre Gioco", fg=self.pregioco_titolo_fg_color, bg=self.pregioco_titolo_bg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54)))) #50
        self.lblTitoloImpostazioni.grid(row=1, column=1, columnspan=3, sticky="nesw")

        spazioTraTitoloEScelte = tk.Label(self.framePreGiocoGioc, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_sfondo_bg_color).grid(row=2, column=2) #30



        frameOpzioni=tk.Frame(self.framePreGiocoGioc, bg=self.pregioco_sfondo_bg_color)

        self.lblNickGiocatore=tk.Label(frameOpzioni, text="Nickname", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_labels_bg_color, fg=self.pregioco_labels_fg_color) #30
        self.lblNickGiocatore.grid(row=0, column=1, columnspan=2, sticky="w")

        self.enNickGiocatori=tk.Entry(frameOpzioni, textvariable=self.nickname, width=15, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182))), bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color) #15
        self.enNickGiocatori.grid(row=0, column=2, columnspan=2, sticky="e")

        spazioTraScelte = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=1, column=2) #20

        self.lblNGiocatori = tk.Label(frameOpzioni, text="N Giocatori", fg=self.pregioco_labels_fg_color, bg=self.pregioco_labels_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.lblNGiocatori.grid(row=2, column=1, columnspan=2, sticky="w")

        self.spnNGiocatori = tk.OptionMenu(frameOpzioni, self.nGiocatoriGioc, "2","3","4","5","6","7","8","9","10")
        self.spnNGiocatori.configure(highlightthickness=0, bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), width=5) #20
        self.spnNGiocatori.grid(row=2, column=2, columnspan=2, sticky="e")

        spazioTraScelte1 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=3, column=2) #20

        self.lblNSchedine = tk.Label(frameOpzioni, text="N Schedine", fg=self.pregioco_labels_fg_color, bg=self.pregioco_labels_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.lblNSchedine.grid(row=4, column=1, columnspan=2, sticky="w")

        self.spnNSchedine = tk.OptionMenu(frameOpzioni, self.nSchedineGioc, "1", "2", "3", "4", "5", "6")
        self.spnNSchedine.configure(highlightthickness=0, bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), width=5) #20
        self.spnNSchedine.grid(row=4, column=2, columnspan=2, sticky="e")

        spazioTraScelte2 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=5, column=2) #20

        self.btnAnnulla = tk.Button(frameOpzioni, text="Annulla", command=lambda: self.indietroPreGiocoGiocSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.btnAnnulla.grid(row=6, column=1)

        spazioTraColonne=tk.Label(frameOpzioni, text=" ", width=15, bg=self.pregioco_sfondo_bg_color).grid(row=6, column=2)

        self.btnInizia = tk.Button(frameOpzioni, text="Inizia", command=lambda: self.GiocaGiocSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.btnInizia.grid(row=6, column=3)



        frameOpzioni.grid(row=3, column=1)



        spazioTraScelteEBottom = tk.Label(self.framePreGiocoGioc, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_sfondo_bg_color).grid(row=4, column=1)

        self.framePreGiocoGioc.columnconfigure(1, weight=1)
        self.framePreGiocoGioc.rowconfigure(3, weight=1)


#TODO*****************************************************************************************************************\
# ********************************************  IMPOSTAZIONI  ********************************************************\
# *********************************************************************************************************************

        self.frameImpostazioni=tk.Frame(self, bg=self.impostazioni_sfondo_bg_color)

        #margineAltoSx = tk.Label(self.frameImpostazioni, width="20", bg=self.impostazioni_sfondo_bg_color).grid(row=0, column=0)
        #margineAltoDx = tk.Label(self.frameImpostazioni, width="20", bg=self.impostazioni_sfondo_bg_color).grid(row=0, column=4)

        spazioTraTitoloETop = tk.Label(self.frameImpostazioni, bg=self.impostazioni_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=0, column=2)

        self.btnTornaAlMenuImpostazioni = tk.Button(self.frameImpostazioni, text="←", bg=self.impostazioni_sfondo_bg_color, fg=self.impostazioni_titolo_fg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bd=0, command=lambda:self.indietroSuono(), relief=tk.FLAT)
        self.btnTornaAlMenuImpostazioni.grid(row=1, column=0)

        self.lblTitoloImpostazioni = tk.Label(self.frameImpostazioni, text="Impostazioni", fg=self.impostazioni_titolo_fg_color, bg=self.impostazioni_titolo_bg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54))))
        self.lblTitoloImpostazioni.grid(row=1, column=1, columnspan=3, sticky="nesw")

        spazioTraTitoloEScelte = tk.Label(self.frameImpostazioni, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.impostazioni_sfondo_bg_color).grid(row=2, column=2)



        frameOpzioni=tk.Frame(self.frameImpostazioni, bg=self.impostazioni_sfondo_bg_color)


        frameTema=tk.Frame(frameOpzioni, bg=self.impostazioni_options_bg_color)

        lblTema = tk.Label(frameTema, text="Tema", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), fg=self.impostazioni_labels_fg_color, bg=self.impostazioni_labels_bg_color).grid(row=0, column=0)

        spazioTraScelteTema=tk.Label(frameTema, text=" ", bg=self.impostazioni_sfondo_bg_color, width=28).grid(row=0, column=1, sticky="nesw")

        self.rbtnTema1 = tk.Radiobutton(frameTema, text="Colorato", variable=self.tema, command=lambda :self.playSuono(), selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Normale", bg=self.impostazioni_options_bg_color).grid(row=0, column=2)
        self.rbtnTema2 = tk.Radiobutton(frameTema, text="Scuro", variable=self.tema, command=lambda :self.playSuono(), selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Scuro", bg=self.impostazioni_options_bg_color).grid(row=0, column=3)

        frameTema.grid(row=0, column=1, sticky="nesw")


        spazioTraScelte1 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.impostazioni_sfondo_bg_color).grid(row=1, column=2)


        frameVolume=tk.Frame(frameOpzioni, bg=self.impostazioni_sfondo_bg_color)

        self.lblVolume=tk.Label(frameVolume, text="Volume", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), fg=self.impostazioni_labels_fg_color, bg=self.impostazioni_labels_bg_color).grid(row=0, column=0)

        spazioTraScelteVolume=tk.Label(frameVolume, text=" ", bg=self.impostazioni_sfondo_bg_color, width=20).grid(row=0, column=1, sticky="nesw")

        #scaleNViagg2=Scale(frameNViagg, from_=1, to=5, variable=nViagg, orient=HORIZONTAL, showvalue=0, length=125, bg="#00DF80", fg=formFgColor, highlightthickness=0, troughcolor=formBgColor, bd=1).grid(row=0, column=1, sticky="ns")
        self.sliderVolume=tk.Scale(frameVolume, from_=0, to=100, variable=self.volume, orient=tk.HORIZONTAL, showvalue=1, length=200, bg=self.impostazioni_options_bg_color, fg=self.impostazioni_options_fg_color, highlightthickness=0, troughcolor=self.impostazioni_options_bg_color, bd=1)
        self.sliderVolume.grid(row=0, column=2, sticky="w")

        frameVolume.grid(row=2, column=1, sticky="nesw")


        spazioTraScelte1 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.impostazioni_sfondo_bg_color).grid(row=3, column=2)


        frameTipoSchedine=tk.Frame(frameOpzioni, bg=self.impostazioni_options_bg_color)

        lblTipoSched = tk.Label(frameTipoSchedine, text="Schedina", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), fg="gray", bg=self.impostazioni_labels_bg_color).grid(row=0, column=0)

        spazioTraScelteTema=tk.Label(frameTipoSchedine, text=" ", bg=self.impostazioni_sfondo_bg_color, width=15).grid(row=0, column=1, sticky="nesw")

        self.rbtnTpoSched1 = tk.Radiobutton(frameTipoSchedine, state=tk.DISABLED, text="Tombolone", command=lambda :self.playSuono(), variable=self.tipoSched, selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Tombolone", bg=self.impostazioni_options_bg_color).grid(row=0, column=2)
        self.rbtnTpoSched2 = tk.Radiobutton(frameTipoSchedine, state=tk.DISABLED, text="Classic", command=lambda :self.playSuono(), variable=self.tipoSched, selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Classic", bg=self.impostazioni_options_bg_color).grid(row=0, column=3)

        frameTipoSchedine.grid(row=4, column=1, sticky="nesw")


        spazioTraScelte2 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.impostazioni_sfondo_bg_color).grid(row=5, column=2)


        self.btnSalva = tk.Button(frameOpzioni, text="Salva", command=lambda: self.salvaSuono(), fg=self.impostazioni_options_fg_color, bg=self.impostazioni_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))))
        self.btnSalva.grid(row=6, column=1, columnspan=3)

        frameOpzioni.grid(row=3, column=1)



        spazioTraScelteEBottom = tk.Label(self.frameImpostazioni, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.impostazioni_sfondo_bg_color).grid(row=4, column=1)

        self.frameImpostazioni.columnconfigure(1, weight=1)
        self.frameImpostazioni.rowconfigure(3, weight=1)

    def setPronto(self, event=None):
        self.playSuono()
        self.giocatoriGioc[self.currentPlayer].setFlagPronto(True)
        self.btnPronto.configure(bg="yellow")
        self.verificaPronti()

    def ordinaClassificaGioc(self):
        giocatoriClassificaOrdinata = []
        punteggi = []
        cosse = []
        giaMessi = []
        for i in range(len(self.giocatoriGioc)):
            cosse.append([self.giocatoriGioc[i].getNome(), self.giocatoriGioc[i].getPunteggioCorrente()])
            punteggi.append(self.giocatoriGioc[i].getPunteggioCorrente())
        punteggi.sort(reverse=True)
        for h in range(len(punteggi)):
            for j in range(len(cosse)):
                for l in range(len(self.giocatoriGioc)):
                    if self.giocatoriGioc[l].getNome() == cosse[j][0] and punteggi[h] == cosse[j][1]:
                        if giaMessi.count(self.giocatoriGioc[l].getNome()) == 0:
                            giaMessi.append(self.giocatoriGioc[l].getNome())
                            giocatoriClassificaOrdinata.append(self.giocatoriGioc[l])
        return giocatoriClassificaOrdinata

    def ordinaClassificaCPU(self):
        giocatoriClassificaOrdinata = []
        punteggi = []
        cosse = []
        giaMessi = []
        for i in range(len(self.giocatoriCpu)):
            cosse.append([self.giocatoriCpu[i].getNome(), self.giocatoriCpu[i].getPunteggioCorrente()])
            punteggi.append(self.giocatoriCpu[i].getPunteggioCorrente())
        punteggi.sort(reverse=True)
        for h in range(len(punteggi)):
            for j in range(len(cosse)):
                for l in range(len(self.giocatoriCpu)):
                    if self.giocatoriCpu[l].getNome() == cosse[j][0] and punteggi[h] == cosse[j][1]:
                        if giaMessi.count(self.giocatoriCpu[l].getNome()) == 0:
                            giaMessi.append(self.giocatoriCpu[l].getNome())
                            giocatoriClassificaOrdinata.append(self.giocatoriCpu[l])
        return giocatoriClassificaOrdinata

    def updateClassProvGioc(self):
        giocatoriClassificaOrdinata=self.ordinaClassificaGioc()

        column=0
        for row in range(len(giocatoriClassificaOrdinata)):
            self.plyrPos = tk.Label(self.frameClassProvGioc, text=((row+1),"°"), borderwidth=0.5, highlightbackground="black",relief=tk.SOLID, font=("Helvetica", int((self.altezza/128) + (self.larghezza/228))), bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color)
            self.plyrPos.grid(row=row + 1, column=column, sticky="nesw")
            self.plyrNome = tk.Label(self.frameClassProvGioc, text=giocatoriClassificaOrdinata[row].getNome(), borderwidth=0.5, highlightbackground="black",relief=tk.SOLID, font=("Helvetica", int((self.altezza/128) + (self.larghezza/228))), bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color)
            self.plyrNome.grid(row=row + 1, column=column + 1, sticky="nesw")
            self.plyrPunt = tk.Label(self.frameClassProvGioc, text=giocatoriClassificaOrdinata[row].getPunteggioCorrente(), borderwidth=0.5, highlightbackground="black",relief=tk.SOLID, font=("Helvetica", int((self.altezza/128) + (self.larghezza/228))), bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color)
            self.plyrPunt.grid(row=row + 1, column=column + 2, sticky="nesw")

    def updateClassProvCPU(self):
        giocatoriClassificaOrdinata=self.ordinaClassificaCPU()

        column=0
        for row in range(len(giocatoriClassificaOrdinata)):
            self.plyrPos = tk.Label(self.frameClassProvCPU, text=((row+1),"°"), borderwidth=0.5, highlightbackground="black",relief=tk.SOLID, font=("Helvetica", int((self.altezza/128) + (self.larghezza/228))), bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color)
            self.plyrPos.grid(row=row + 1, column=column, sticky="nesw")
            self.plyrNome = tk.Label(self.frameClassProvCPU, text=giocatoriClassificaOrdinata[row].getNome(), borderwidth=0.5, highlightbackground="black",relief=tk.SOLID, font=("Helvetica", int((self.altezza/128) + (self.larghezza/228))), bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color)
            self.plyrNome.grid(row=row + 1, column=column + 1, sticky="nesw")
            self.plyrPunt = tk.Label(self.frameClassProvCPU, text=giocatoriClassificaOrdinata[row].getPunteggioCorrente(), borderwidth=0.5, highlightbackground="black",relief=tk.SOLID, font=("Helvetica", int((self.altezza/128) + (self.larghezza/228))), bg=self.gioco_classifica_bg_color, fg=self.gioco_classifica_tabella_fg_color)
            self.plyrPunt.grid(row=row + 1, column=column + 2, sticky="nesw")

    def creaSchedineGiocatoriGioc(self, plyr):
        # Creo una pseudo-schedina con una tupla
        # contenente il numero e lo stato (set o unset)

        arrSchedine = []
        h = 0
        for nSchedina in range(self.nSchedineGioc.get() * 2):
            h += 1
            arrSchedina = []
            arrRow1 = []
            arrRow2 = []
            arrRow3 = []
            if nSchedina % 2 == 0:
                # Riga
                for riga in range(3):
                    counterBlank = 0
                    counterNum = 0
                    print("\nRiga ", riga+1, " | plyr ",plyr+1,": ")
                    # Colonna
                    for colonna in range(9):
                        whiteOrNot = random.randint(1, 2)
                        if counterNum != 5 and whiteOrNot == 1:
                            if riga == 0:
                                if colonna == 0:
                                    numCella = random.randint((colonna * 10) + 1, (colonna * 10) + 3)
                                    print("\tda:", (colonna * 10) + 1, " a: ", (colonna * 10) + 3, " estraggo: ", numCella, end="\t|")
                                else:
                                    numCella = random.randint((colonna * 10), (colonna * 10) + 3)
                                    print("\tda:", colonna * 10, " a: ", (colonna * 10) + 3, " estraggo: ", numCella, end="\t|")
                            elif riga == 1:
                                numCella = random.randint((colonna * 10) + 4, (colonna * 10) + 6)
                                print("\tda:", (colonna * 10) + 4, " a: ", (colonna * 10) + 6, " estraggo: ", numCella, end="\t|")
                            elif riga == 2:
                                if colonna == 8:
                                    numCella = random.randint((colonna * 10) + 7, (colonna * 10) + 9 + 1)
                                    print("\tda:", (colonna * 10) + 7, " a: ", (colonna * 10) + 9 + 1, " estraggo: ", numCella, end="\t|")
                                else:
                                    numCella = random.randint((colonna * 10) + 7, (colonna * 10) + 9)
                                    print("\tda:", (colonna * 10) + 7, " a: ", (colonna * 10) + 9, " estraggo: ", numCella, end="\t|")

                            cella = [numCella, "unset"]
                            if riga == 0:
                                arrRow1.append(cella)
                                if colonna == 8:
                                    arrSchedina.append(arrRow1)
                            if riga == 1:
                                arrRow2.append(cella)
                                if colonna == 8:
                                    arrSchedina.append(arrRow2)
                            if riga == 2:
                                arrRow3.append(cella)
                                if colonna == 8:
                                    arrSchedina.append(arrRow3)
                            counterNum += 1
                            #arrCounterBlanksCols[colonna].set(1)
                        else:
                            if counterBlank != 4:
                                cella = [" ", "unset"]
                                print("\tda:", colonna * 10, " a: ", (colonna * 10) + 9, " estraggo: NULLA", end="\t|")
                                counterBlank += 1
                                if riga == 0:
                                    arrRow1.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow1)
                                if riga == 1:
                                    arrRow2.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow2)
                                if riga == 2:
                                    arrRow3.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow3)
                            else:
                                if riga == 0:
                                    if colonna == 0:
                                        numCella = random.randint((colonna * 10) + 1, (colonna * 10) + 3)
                                        print("\tda:", (colonna * 10) + 1, " a: ", (colonna * 10) + 3, " estraggo: ", numCella, end="\t|")
                                    else:
                                        numCella = random.randint((colonna * 10), (colonna * 10) + 3)
                                        print("\tda:", colonna * 10, " a: ", (colonna * 10) + 3, " estraggo: ", numCella, end="\t|")
                                elif riga == 1:
                                    numCella = random.randint((colonna * 10) + 4, (colonna * 10) + 6)
                                    print("\tda:", (colonna * 10) + 4, " a: ", (colonna * 10) + 6, " estraggo: ", numCella, end="\t|")
                                elif riga == 2:
                                    if colonna == 8:
                                        numCella = random.randint((colonna * 10) + 7, (colonna * 10) + 9 + 1)
                                        print("\tda:", (colonna * 10) + 7, " a: ", (colonna * 10) + 9 + 1, " estraggo: ", numCella, end="\t|")
                                    else:
                                        numCella = random.randint((colonna * 10) + 7, (colonna * 10) + 9)
                                        print("\tda:", (colonna * 10) + 7, " a: ", (colonna * 10) + 9, " estraggo: ", numCella, end="\t|")

                                # cella = tk.Button(self.schedina, text=numCella, bg="yellow", font=("Helvetica", 17), width=2, bd=1, highlightcolor="black", relief=tk.SOLID).grid(row=riga, column=colonna)
                                cella = [numCella, "unset"]
                                if riga == 0:
                                    arrRow1.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow1)
                                if riga == 1:
                                    arrRow2.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow2)
                                if riga == 2:
                                    arrRow3.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow3)
                print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                arrSchedine.append(arrSchedina)
        return arrSchedine

    def creaSchedineGiocatoriCPU(self, plyr):
        # Creo una pseudo-schedina con una tupla
        # contenente il numero e lo stato (set o unset)

        arrSchedine = []
        h = 0
        for nSchedina in range(self.nSchedineCPU.get() * 2):
            h += 1
            arrSchedina = []
            arrRow1 = []
            arrRow2 = []
            arrRow3 = []
            if nSchedina % 2 == 0:
                # Riga
                for riga in range(3):
                    counterBlank = 0
                    counterNum = 0
                    print("\nRiga ", riga+1, " | plyr ",plyr+1,": ")
                    # Colonna
                    for colonna in range(9):
                        whiteOrNot = random.randint(1, 2)
                        if counterNum != 5 and whiteOrNot == 1:
                            if riga == 0:
                                if colonna == 0:
                                    numCella = random.randint((colonna * 10) + 1, (colonna * 10) + 3)
                                    print("\tda:", (colonna * 10) + 1, " a: ", (colonna * 10) + 3, " estraggo: ", numCella, end="\t|")
                                else:
                                    numCella = random.randint((colonna * 10), (colonna * 10) + 3)
                                    print("\tda:", colonna * 10, " a: ", (colonna * 10) + 3, " estraggo: ", numCella, end="\t|")
                            elif riga == 1:
                                numCella = random.randint((colonna * 10) + 4, (colonna * 10) + 6)
                                print("\tda:", (colonna * 10) + 4, " a: ", (colonna * 10) + 6, " estraggo: ", numCella, end="\t|")
                            elif riga == 2:
                                if colonna == 8:
                                    numCella = random.randint((colonna * 10) + 7, (colonna * 10) + 9 + 1)
                                    print("\tda:", (colonna * 10) + 7, " a: ", (colonna * 10) + 9 + 1, " estraggo: ", numCella, end="\t|")
                                else:
                                    numCella = random.randint((colonna * 10) + 7, (colonna * 10) + 9)
                                    print("\tda:", (colonna * 10) + 7, " a: ", (colonna * 10) + 9, " estraggo: ", numCella, end="\t|")

                            cella = [numCella, "unset"]
                            if riga == 0:
                                arrRow1.append(cella)
                                if colonna == 8:
                                    arrSchedina.append(arrRow1)
                            if riga == 1:
                                arrRow2.append(cella)
                                if colonna == 8:
                                    arrSchedina.append(arrRow2)
                            if riga == 2:
                                arrRow3.append(cella)
                                if colonna == 8:
                                    arrSchedina.append(arrRow3)
                            counterNum += 1
                            #arrCounterBlanksCols[colonna].set(1)
                        else:
                            if counterBlank != 4:
                                cella = [" ", "unset"]
                                print("\tda:", colonna * 10, " a: ", (colonna * 10) + 9, " estraggo: NULLA", end="\t|")
                                counterBlank += 1
                                if riga == 0:
                                    arrRow1.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow1)
                                if riga == 1:
                                    arrRow2.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow2)
                                if riga == 2:
                                    arrRow3.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow3)
                            else:
                                if riga == 0:
                                    if colonna == 0:
                                        numCella = random.randint((colonna * 10) + 1, (colonna * 10) + 3)
                                        print("\tda:", (colonna * 10) + 1, " a: ", (colonna * 10) + 3, " estraggo: ", numCella, end="\t|")
                                    else:
                                        numCella = random.randint((colonna * 10), (colonna * 10) + 3)
                                        print("\tda:", colonna * 10, " a: ", (colonna * 10) + 3, " estraggo: ", numCella, end="\t|")
                                elif riga == 1:
                                    numCella = random.randint((colonna * 10) + 4, (colonna * 10) + 6)
                                    print("\tda:", (colonna * 10) + 4, " a: ", (colonna * 10) + 6, " estraggo: ", numCella, end="\t|")
                                elif riga == 2:
                                    if colonna == 8:
                                        numCella = random.randint((colonna * 10) + 7, (colonna * 10) + 9 + 1)
                                        print("\tda:", (colonna * 10) + 7, " a: ", (colonna * 10) + 9 + 1, " estraggo: ", numCella, end="\t|")
                                    else:
                                        numCella = random.randint((colonna * 10) + 7, (colonna * 10) + 9)
                                        print("\tda:", (colonna * 10) + 7, " a: ", (colonna * 10) + 9, " estraggo: ", numCella, end="\t|")

                                # cella = tk.Button(self.schedina, text=numCella, bg="yellow", font=("Helvetica", 17), width=2, bd=1, highlightcolor="black", relief=tk.SOLID).grid(row=riga, column=colonna)
                                cella = [numCella, "unset"]
                                if riga == 0:
                                    arrRow1.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow1)
                                if riga == 1:
                                    arrRow2.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow2)
                                if riga == 2:
                                    arrRow3.append(cella)
                                    if colonna == 8:
                                        arrSchedina.append(arrRow3)
                print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                arrSchedine.append(arrSchedina)
        return arrSchedine

    def assegnaSchedineGiocatoriGioc(self):
        # Per ogni nGiocatore creo una pseudoschedina
        # contenente solo un numero e lo stato(set o unset)

        giocatore = Giocatore("boh", [])

        # Giocatori
        for t in range(self.nGiocatoriGioc.get()):
            arrSchedine = self.creaSchedineGiocatoriGioc(t)
            """if self.giocatore.getSchedine() == []:
                self.giocatore.setSchedine(arrSchedine)
                giocatore = self.giocatore
            else:
                giocatore = Giocatore("CPU " + str(t), arrSchedine)"""
            if self.giocatoriGioc == []:
                giocatore = Giocatore(self.nickname.get(), arrSchedine)
            else:
                #n=t+1
                giocatore = Giocatore("Giocatore " + str(t), arrSchedine)
            self.giocatoriGioc.append(giocatore)

        # STAMPO COSSEH

        #DEBUG
        # giocatori
        for t in range(len(self.giocatoriGioc)):
            print("Nome Giocatore: " + self.giocatoriGioc[t].getNome())
            # schedina
            for i in range(len(self.giocatoriGioc[t].getSchedine())):
                print("\tN Schedina: ", i)
                # riga
                for y in range(len(self.giocatoriGioc[t].getSchedine()[i])):
                    print("\t\tN Riga: ", y)
                    # cella
                    print("\t\t\tCelle: ", end="")
                    for z in range(len(self.giocatoriGioc[t].getSchedine()[i][y])):
                        print("\t", self.giocatoriGioc[t].getSchedine()[i][y][z], end="")
                    print()

    def assegnaSchedineGiocatoriCPU(self):
        # Per ogni nGiocatore creo una pseudoschedina
        # contenente solo un numero e lo stato(set o unset)
        nomiGiaEstratti = []

        giocatore = Giocatore("boh", [])

        # Giocatori
        for t in range(self.nGiocatoriCPU.get()):
            arrSchedine = self.creaSchedineGiocatoriCPU(t)
            if self.giocatore.getSchedine() == []:
                self.giocatore.setSchedine(arrSchedine)
                giocatore = self.giocatore
            else:
                nome = self.nomiCpu[random.randint(0, len(self.nomiCpu) - 1)]
                while nomiGiaEstratti.count(nome) != 0:
                    nome = self.nomiCpu[random.randint(0, len(self.nomiCpu) - 1)]
                nomiGiaEstratti.append(nome)
                # giocatore = Giocatore("CPU " + str(t), arrSchedine)
                giocatore = Giocatore(nome, arrSchedine)
            self.giocatoriCpu.append(giocatore)

        # STAMPO COSSEH

        # DEBUG
        # giocatori
        for t in range(len(self.giocatoriCpu)):
            print("Nome Giocatore: " + self.giocatoriCpu[t].getNome())
            # schedina
            for i in range(len(self.giocatoriCpu[t].getSchedine())):
                print("\tN Schedina: ", i)
                # riga
                for y in range(len(self.giocatoriCpu[t].getSchedine()[i])):
                    print("\t\tN Riga: ", y)
                    # cella
                    print("\t\t\tCelle: ", end="")
                    for z in range(len(self.giocatoriCpu[t].getSchedine()[i][y])):
                        print("\t", self.giocatoriCpu[t].getSchedine()[i][y][z], end="")
                    print()

    def setCommandCelleCPU(self, nScheda, nRiga, nCella):
        self.arrSchedineCPU[nScheda][nRiga][nCella].configure(command=lambda: self.clickCPUSuono(self.currentPlayer, nScheda, nRiga, nCella, "plyr"))

    def setCommandCelleGioc(self, nScheda, nRiga, nCella):
        self.arrSchedineGioc[nScheda][nRiga][nCella].configure(command=lambda: self.clickGiocSuono(self.currentPlayer, nScheda, nRiga, nCella, "plyr"))

    def verificaPronti(self):
        countFalse = 0
        countTrue = 0
        for l in range(len(self.giocatoriGioc)):
            print("FlagPronto di " + self.giocatoriGioc[l].getNome() + ": " + str(self.giocatoriGioc[l].getFlagPronto()))
            if self.giocatoriGioc[l].getFlagPronto() == False:
                countFalse += 1
            elif self.giocatoriGioc[l].getFlagPronto() == True:
                countTrue += 1

        print("CounterFalse: " + str(countFalse) + "\nCounterTrue: " + str(countTrue) + "\nLen di GiocatoriCpu: " + str(len(self.giocatoriGioc)))

        if countFalse == len(self.giocatoriGioc):
            self.btnNEstrattoGioc.configure(state=tk.DISABLED)
            self.master.bind('<Button-3>', self.setPronto)
            print("sono nel falso")

        elif countTrue == len(self.giocatoriGioc):
            self.btnNEstrattoGioc.configure(state=tk.NORMAL)
            self.master.bind('<Button-3>', self.estraiGioc)
            print("Sono nel vero")

            for i in range(len(self.giocatoriGioc)):
                self.giocatoriGioc[i].setFlagPronto(False)
            self.btnPronto.configure(bg="red")
                #print("Flag di " + self.giocatoriCpu[i].getNome() + " settato")

    def estraiGiocSuono(self):
        self.playSuono()
        self.estraiGioc(event=None)

    def estraiGioc(self, event):
        self.verificaPronti()

        #Estrae i numeri casuali della partita
        randN = random.randint(1, 90)
        if self.nEstratti == []:
            self.lblNEstrattoGioc.configure(text=randN)
            self.nEstratti.append(randN)

            # Tabellone
            for i in range(len(self.arrTabellone)):
                if int(self.arrTabellone[i].cget("text")) == randN:
                    self.arrTabellone[i].configure(bg=self.gioco_tabellone_set_bg_color)
            # DEBUG  print("N Estratto: ", randN)

        elif self.nEstratti.count(randN) != 0:
            self.estraiGioc(event=None)
        else:
            self.lblNEstrattoGioc.configure(text=randN)
            self.nEstratti.append(randN)

            # Tabellone
            for i in range(len(self.arrTabellone)):
                if int(self.arrTabellone[i].cget("text")) == randN:
                    self.arrTabellone[i].configure(bg=self.gioco_tabellone_set_bg_color)

        # self.master.bind("<Button-3>", self.doNothing)
        # self.btnNEstratto.configure(state=tk.DISABLED)

        self.updateClassProvGioc()

        # Le CPU aspettano un tot prima di selezionare le celle e dichiarare i premi
        """if self.nSchedine.get() == 1 or self.nSchedine.get() == 2:
            sec = random.randint(1000, 3000)
        elif self.nSchedine.get() == 3 or self.nSchedine.get() == 4:
            sec = random.randint(2000, 5000)
        elif self.nSchedine.get() == 5 or self.nSchedine.get() == 6:
            sec = random.randint(4000, 7000)"""
        # DEBUG print("Le CPU aspetteranno ",sec," prima di effettuare la verifica del numero ",randN)
        # self.after(sec, lambda:self.selectCelleCpu(randN))

    def estraiCPUSuono(self):
        self.playSuono()
        self.estraiCPU(event=None)

    def estraiCPU(self, event):
        #Estrae i numeri casuali della partita

        randN=random.randint(1, 90)
        if self.nEstratti == []:
            self.lblNEstrattoCPU.configure(text=randN)
            self.nEstratti.append(randN)

            # Tabellone
            for i in range(len(self.arrTabellone)):
                if int(self.arrTabellone[i].cget("text")) == randN:
                    self.arrTabellone[i].configure(bg=self.gioco_tabellone_set_bg_color)
            #DEBUG  print("N Estratto: ", randN)

        elif self.nEstratti.count(randN) != 0:
            self.estraiCPU(event=None)
        else:
            self.lblNEstrattoCPU.configure(text=randN)
            self.nEstratti.append(randN)

            # Tabellone
            for i in range(len(self.arrTabellone)):
                if int(self.arrTabellone[i].cget("text")) == randN:
                    self.arrTabellone[i].configure(bg=self.gioco_tabellone_set_bg_color)

        self.master.bind("<Button-3>", self.doNothing)
        self.btnNEstrattoCPU.configure(state=tk.DISABLED)

        self.updateClassProvCPU()

        #Le CPU aspettano un tot prima di selezionare le celle e dichiarare i premi
        if self.nSchedineCPU.get() == 1 or self.nSchedineCPU.get() == 2:
            sec = random.randint(1000, 3000)
        elif self.nSchedineCPU.get() == 3 or self.nSchedineCPU.get() == 4:
            sec = random.randint(2000, 5000)
        elif self.nSchedineCPU.get() == 5 or self.nSchedineCPU.get() == 6:
            sec = random.randint(4000, 7000)
        #DEBUG print("Le CPU aspetteranno ",sec," prima di effettuare la verifica del numero ",randN)
        self.after(sec, lambda:self.selectCelleCpu(randN))

    def selectCelleCpu(self, nEstratto):
        # Ogni volta che estraggo un numero verifico
        # se le cpu ce l'hanno nelle loro schedine
        # e setto lo stato di quella "cella" a set

        #giocatori
        for i in range(len(self.giocatoriCpu)):
            if i > 0:
                #sec = random.randint(1000, 5000)
                #time.sleep(sec)
                #schedine
                for l in range(len(self.giocatoriCpu[i].getSchedine())):
                    #righe
                    for y in range(len(self.giocatoriCpu[i].getSchedine()[l])):
                        #celle
                        for t in range(len(self.giocatoriCpu[i].getSchedine()[l][y])):
                            if self.giocatoriCpu[i].getSchedine()[l][y][t][0] == nEstratto:
                                arr = self.giocatoriCpu[i].getSchedine()
                                num = self.giocatoriCpu[i].getSchedine()[l][y][t][0]
                                commnd = "set"
                                tupla = [num, commnd]
                                arr[l][y][t] = tupla
                                self.giocatoriCpu[i].setSchedine(arr)
                                if self.giocatoriCpu[i].getSchedine()[l][y][t][0] != " ":
                                    if self.giocatoriCpu[i].getNome() == self.giocatoriCpu[self.currentPlayer].getNome():
                                        # DEBUG print("l:",l," y:",y," t:",t)
                                        self.arrSchedineCPU[l][y][t].configure(bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color, relief=tk.SUNKEN)
                                        self.clickCPU(i, l, y, self.giocatoriCpu[i].getSchedine()[l][y][t][0], "cpu")
                                    else:
                                        self.clickCPU(i, l, y, self.giocatoriCpu[i].getSchedine()[l][y][t][0], "cpu")
        self.master.bind("<Button-3>", self.estraiCPU)
        self.btnNEstrattoCPU.configure(state=tk.NORMAL)
        #self.checkByVarsMulti()

    def globals(self):
        # Setto le variabili "globali"
        self.nomiCpu=["Gianfranco", "Francesco", "Pippo", "Eric", "Claudio Hilario", "Geltrude", "Pino", "Costantina", "Simone", "Morena", "Kledi", "Gabriele", "Topolino", "Daniele", "Minni", "Paperino"]
        self.volume=tk.IntVar(self, 50)
        self.nickname=tk.StringVar(self, "Default Nick")
        self.nEstratti=[]
        self.currentPlayer=0
        self.giocatore=Giocatore(self.nickname.get(), [])
        self.giocatoriCpu=[]
        self.giocatoriGioc=[]
        self.nGiocatoriGioc=tk.IntVar(self, 2)
        self.nGiocatoriCPU = tk.IntVar(self, 2)
        self.nSchedineGioc=tk.IntVar(self, 1)
        self.nSchedineCPU=tk.IntVar(self, 1)
        self.tema=tk.StringVar(self, "Normale")
        self.tipoSched=tk.StringVar(self, "Classic")
        self.punteggio=0
        self.ambo = False
        self.terna = False
        self.quaterna = False
        self.cinquina = False
        self.decina = False
        self.tombola = False
        self.tombolino = False

    def EsciSuono(self):
        self.playSuono()
        self.Esci(event=None)

    def Esci(self, event):
        self.master.quit()

    def doNothing(self, event):
        pass

    def TipoGiocoSuono(self):
        self.playSuono()
        self.TipoGioco(event=None)

    def TipoGioco(self, event):
        self.master.bind('Left', self.doNothing)
        self.master.bind('Right', self.doNothing)
        self.master.bind('<Button-3>', self.doNothing)
        self.master.bind('<Return>', self.doNothing)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Escape>', self.Menu)

        self.framePreGiocoGioc.grid_forget()
        self.framePreGiocoCPU.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.frameGiocoCPU.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameMenu.grid_forget()
        self.framePunteggio.grid_forget()
        self.frameTipoGioco.grid(row=0, column=0, sticky="nesw")

    def PunteggioSuono(self):
        self.playSuono()
        self.Punteggio(event=None)

    def Punteggio(self, event):
        self.master.bind('Left', self.doNothing)
        self.master.bind('Right', self.doNothing)
        self.master.bind('<Button-3>', self.doNothing)
        self.master.bind('<Return>', self.doNothing)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Escape>', self.Menu)

        #self.lblPunteggioTotale.configure(text=self.giocatoriCpu[0].getPunteggioCorrente())

        self.framePreGiocoGioc.grid_forget()
        self.framePreGiocoCPU.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.frameGiocoCPU.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameMenu.grid_forget()
        self.frameTipoGioco.grid_forget()
        self.framePunteggio.grid(row=0, column=0, sticky="nesw")

    def TornaAlMenuGiocaSuono(self):
        self.playSuono()
        self.TornaAlMenuGioca(event=None)

    def TornaAlMenuGioca(self, event):
        pygame.mixer.music.pause()
        pygame.mixer.music.load(self.currentDirectory+"/Files/Musica/ColonneSonore/Shake.ogg")
        pygame.mixer.music.play(-1)
        self.Menu(event=None)

    def MenuSuono(self):
        self.playSuono()
        self.Menu(event=None)

    def Menu(self, event):
        # Porta in primo piano il Menu

        self.master.bind('Left', self.doNothing)
        self.master.bind('Right', self.doNothing)
        self.master.bind('<Button-3>', self.doNothing)
        self.master.bind('<Return>', self.TipoGioco)
        self.master.bind('<Tab>', self.Impostazioni)
        self.master.bind('<Escape>', self.Esci)

        self.checkTema()

        #self.master.configure(bg=self.menu_sfondo_bg_color)

        self.currentWindow="Menu"

        self.framePreGiocoGioc.grid_forget()
        self.framePreGiocoCPU.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.frameGiocoCPU.grid_forget()
        self.framePunteggio.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameTipoGioco.grid_forget()
        #self.frameMenu.grid_anchor(anchor="n")
        #self.frameMenu.columnconfigure(1, weight=1)
        self.frameMenu.grid(row=0, column=0, sticky="nesw")
        #self.frameGioco.pack_forget()
        #self.frameImpostazioni.pack_forget()
        #self.frameMenu.pack(expand=True, anchor=tk.CENTER, side=tk.LEFT, fill=tk.BOTH)

    def GiocaGiocSuono(self):
        self.playSuono()
        self.GiocaGioc(event=None)

    def GiocaGioc(self, event):
        pygame.mixer.music.pause()
        pygame.mixer.music.load(self.currentDirectory+"/Files/Musica/ColonneSonore/Gaiety.ogg")
        pygame.mixer.music.play(-1)

        self.master.bind('<Return>', self.estraiGioc)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Left>', self.doNothing)
        self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayer(direction, event))
        self.master.bind('<Button-3>', self.estraiGioc)
        self.master.bind('<Escape>', self.Menu)


        # Porta in primo piano la schermata del gioco
        self.CreateWidgets()


        self.currentPlayer=0
        self.nickname.set(self.enNickGiocatori.get())
        self.giocatore=Giocatore(self.nickname.get(), [])
        self.giocatoriGioc=[]
        self.assegnaSchedineGiocatoriGioc()
        self.switchPlayerGioc("", event=None)
        self.nEstratti=[]
        self.estraiGioc(event)
        self.ambo = False
        self.terna = False
        self.quaterna = False
        self.cinquina = False
        self.decina = False
        self.tombola = False
        self.tombolino = False

        #self.master.configure(bg=self.gioco_sfondo_bg_color)

        self.currentWindow = "Gioco"

        self.framePunteggio.grid_forget()
        self.frameMenu.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.framePreGiocoGioc.grid_forget()
        self.framePreGiocoCPU.grid_forget()
        self.frameGiocoCPU.grid_forget()
        self.frameTipoGioco.grid_forget()
        self.frameGiocoGioc.grid(row=0, column=0, sticky="nesw")
        #self.frameMenu.pack_forget()
        #self.frameImpostazioni.pack_forget()
        #self.frameGioco.pack()

    def PreGiocoGiocSuono(self):
        self.playSuono()
        self.PreGiocoGioc(event=None)

    def PreGiocoGioc(self, event):
        self.master.bind('Left', self.doNothing)
        self.master.bind('Right', self.doNothing)
        self.master.bind('<Button-3>', self.doNothing)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Escape>', self.indietroPreGiocoGioc)
        self.master.bind('<Return>', self.GiocaGioc)

        self.punteggio = 0

        self.framePunteggio.grid_forget()
        self.frameMenu.grid_forget()
        self.framePreGiocoCPU.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.frameGiocoCPU.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameTipoGioco.grid_forget()
        self.framePreGiocoGioc.grid(row=0, column=0, sticky="nesw")

        self.oldNickname = self.nickname.get()
        self.oldNGiocatoriGioc = self.nGiocatoriGioc.get()
        self.oldNSchedineGioc = self.nSchedineGioc.get()

    def GiocaCPUSuono(self):
        self.playSuono()
        self.GiocaCPU(event=None)

    def GiocaCPU(self, event):
        pygame.mixer.music.pause()
        pygame.mixer.music.load(self.currentDirectory+"/Files/Musica/ColonneSonore/Gaiety.ogg")
        pygame.mixer.music.play(-1)

        self.master.bind('<Return>', self.estraiCPU)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Left>', self.doNothing)
        self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayer(direction, event))
        self.master.bind('<Button-3>', self.estraiCPU)
        self.master.bind('<Escape>', self.Menu)


        # Porta in primo piano la schermata del gioco
        self.CreateWidgets()


        self.currentPlayer=0
        self.nickname.set(self.enNickGiocatori.get())
        self.giocatore=Giocatore(self.nickname.get(), [])
        self.giocatoriCpu=[]
        self.assegnaSchedineGiocatoriCPU()
        self.switchPlayerCPU("", event=None)
        self.nEstratti=[]
        self.estraiCPU(event)
        self.ambo = False
        self.terna = False
        self.quaterna = False
        self.cinquina = False
        self.decina = False
        self.tombola = False
        self.tombolino = False

        #self.master.configure(bg=self.gioco_sfondo_bg_color)

        self.currentWindow = "Gioco"

        self.framePunteggio.grid_forget()
        self.frameMenu.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.framePreGiocoGioc.grid_forget()
        self.framePreGiocoCPU.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.frameTipoGioco.grid_forget()
        self.frameGiocoCPU.grid(row=0, column=0, sticky="nesw")
        #self.frameMenu.pack_forget()
        #self.frameImpostazioni.pack_forget()
        #self.frameGioco.pack()

    def PreGiocoCPUSuono(self):
        self.playSuono()
        self.PreGiocoCPU(event=None)

    def PreGiocoCPU(self, event):
        self.master.bind('Left', self.doNothing)
        self.master.bind('Right', self.doNothing)
        self.master.bind('<Button-3>', self.doNothing)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Escape>', self.indietroPreGiocoCPU)
        self.master.bind('<Return>', self.GiocaCPU)

        self.punteggio = 0

        self.framePunteggio.grid_forget()
        self.frameMenu.grid_forget()
        self.framePreGiocoGioc.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.frameGiocoCPU.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameTipoGioco.grid_forget()
        self.framePreGiocoCPU.grid(row=0, column=0, sticky="nesw")

        self.oldNickname = self.nickname.get()
        self.oldNGiocatoriCPU = self.nGiocatoriCPU.get()
        self.oldNSchedineCPU = self.nSchedineCPU.get()

    def switchPlayerCPUSuono(self, direction):
        self.playSuono()
        self.switchPlayerCPU(direction, event=None)

    def switchPlayerCPU(self, direction, event):
        # Cambia giocatore e colora i
        # button segnaposto nella grid

        if direction == "<":
            self.currentPlayer -= 1
        if direction == ">":
            self.currentPlayer += 1
        """#Per goTOPlayerClassifica()
        if direction is int:
            print("Sono in switch player booooh")
            self.currentPlayer = direction"""

        if self.currentPlayer == 0:
            self.master.bind('<Left>', self.doNothing)
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayerCPU(direction, event))
            self.btnPrevPlayerCPU.configure(state=tk.DISABLED)
            self.btnNextPlayerCPU.configure(state=tk.NORMAL)
            self.btnPrevPlayerCPU.configure(bg=self.gioco_framedestro_bg_color, relief=tk.FLAT)
            self.btnNextPlayerCPU.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)

            #self.btnPrevPlayer.grid_forget()
            #self.btnNextPlayer.grid(row=11, column=4)

        elif self.currentPlayer == len(self.giocatoriCpu)-1:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchPlayerCPU(direction, event))
            self.master.bind('<Right>', self.doNothing)
            self.btnPrevPlayerCPU.configure(state=tk.NORMAL)
            self.btnNextPlayerCPU.configure(state=tk.DISABLED)
            self.btnPrevPlayerCPU.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            self.btnNextPlayerCPU.configure(bg=self.gioco_framedestro_bg_color, relief=tk.FLAT)

            #self.btnPrevPlayer.grid(row=11, column=1)
            #self.btnNextPlayer.grid_forget()

        else:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchPlayerCPU(direction, event))
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayerCPU(direction, event))
            self.btnPrevPlayerCPU.configure(state=tk.NORMAL)
            self.btnNextPlayerCPU.configure(state=tk.NORMAL)
            self.btnPrevPlayerCPU.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            self.btnNextPlayerCPU.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)

            #self.btnPrevPlayer.grid(row=11, column=1)
            #self.btnNextPlayer.grid(row=11, column=4)

        """#DEBUG
        print("CurrentPlayer: ", self.currentPlayer)
        print("nGiocatori: ", self.nGiocatori.get())
        print("nGiocatori-1: ", self.nGiocatori.get()-1)
        print("Len: ", len(self.giocatoriCpu))
        for h in range(len(self.giocatoriCpu)):
            print("\t"+self.giocatoriCpu[h].getNome())
        print("Len ArrSchedine: ", len(self.arrSchedine))"""

        self.lblTitoloGiocoCPU.configure(text=self.giocatoriCpu[self.currentPlayer].getNome())

        # Schedine
        for i in range(len(self.arrSchedineCPU)):
            # Righe
            for l in range(len(self.arrSchedineCPU[i])):
                # Celle
                for k in range(len(self.arrSchedineCPU[i][l])):
                    """print("i: ",i, end=" ")
                    print("l: ",l, end=" ")
                    print("k: ",k)"""
                    if self.giocatoriCpu[self.currentPlayer].getNome() == self.nickname.get():
                        #print(self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][0])
                        if self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][0] != " ":
                            self.arrSchedineCPU[i][l][k].configure(state=tk.NORMAL)
                        else:
                            self.arrSchedineCPU[i][l][k].configure(state=tk.DISABLED)
                    else:
                        self.arrSchedineCPU[i][l][k].configure(state=tk.DISABLED)
                    self.arrSchedineCPU[i][l][k].configure(text=self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][0])

                    if self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][1] == "unset":
                        self.arrSchedineCPU[i][l][k].configure(bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color)
                        self.arrSchedineCPU[i][l][k].configure(relief=tk.RAISED)
                    elif self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][1] == "set":
                        self.arrSchedineCPU[i][l][k].configure(bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color)
                        self.arrSchedineCPU[i][l][k].configure(relief=tk.SOLID)
        #print("-------------------------------------------------------------")

    def switchPlayerGiocSuono(self, direction):
        self.playSuono()
        self.switchPlayerGioc(direction, event=None)

    def switchPlayerGioc(self, direction, event):
        # Cambia giocatore e colora i
        # button segnaposto nella grid

        if direction == "<":
            self.currentPlayer -= 1
        if direction == ">":
            self.currentPlayer += 1
        """#Per goTOPlayerClassifica()
        if direction is int:
            print("Sono in switch player booooh")
            self.currentPlayer = direction"""



        if self.currentPlayer == 0:
            self.master.bind('<Left>', self.doNothing)
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayer(direction, event))
            self.btnPrevPlayerGioc.configure(state=tk.DISABLED)
            self.btnNextPlayerGioc.configure(state=tk.NORMAL)
            self.btnPrevPlayerGioc.configure(bg=self.gioco_framedestro_bg_color, relief=tk.FLAT)
            self.btnNextPlayerGioc.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)

            #self.btnPrevPlayer.grid_forget()
            #self.btnNextPlayer.grid(row=11, column=4)

        elif self.currentPlayer == len(self.giocatoriGioc)-1:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchPlayer(direction, event))
            self.master.bind('<Right>', self.doNothing)
            self.btnPrevPlayerGioc.configure(state=tk.NORMAL)
            self.btnNextPlayerGioc.configure(state=tk.DISABLED)
            self.btnPrevPlayerGioc.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            self.btnNextPlayerGioc.configure(bg=self.gioco_framedestro_bg_color, relief=tk.FLAT)

            #self.btnPrevPlayer.grid(row=11, column=1)
            #self.btnNextPlayer.grid_forget()

        else:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchPlayerGioc(direction, event))
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayerGioc(direction, event))
            self.btnPrevPlayerGioc.configure(state=tk.NORMAL)
            self.btnNextPlayerGioc.configure(state=tk.NORMAL)
            self.btnPrevPlayerGioc.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            self.btnNextPlayerGioc.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)

            #self.btnPrevPlayer.grid(row=11, column=1)
            #self.btnNextPlayer.grid(row=11, column=4)

        """#DEBUG
        print("CurrentPlayer: ", self.currentPlayer)
        print("nGiocatori: ", self.nGiocatori.get())
        print("nGiocatori-1: ", self.nGiocatori.get()-1)
        print("Len: ", len(self.giocatoriCpu))
        for h in range(len(self.giocatoriCpu)):
            print("\t"+self.giocatoriCpu[h].getNome())
        print("Len ArrSchedine: ", len(self.arrSchedine))"""

        print(self.giocatoriGioc[self.currentPlayer].getFlagPronto())
        if not self.giocatoriGioc[self.currentPlayer].getFlagPronto():
            self.btnPronto.configure(bg="red")
        elif self.giocatoriGioc[self.currentPlayer].getFlagPronto():
            self.btnPronto.configure(bg="yellow")

        self.lblTitoloGiocoGioc.configure(text=self.giocatoriGioc[self.currentPlayer].getNome())
        #self.enTitoloGioco.configure(text=self.giocatoriCpu[self.currentPlayer].getNome())

        # Schedine
        for i in range(len(self.arrSchedineGioc)):
        #for i in range(len(self.giocatoriCpu[self.currentPlayer].getSchedine())):
            # Righe
            for l in range(len(self.arrSchedineGioc[i])):
            #for l in range(len(self.giocatoriCpu[self.currentPlayer].getSchedine()[i])):
                # Celle
                for k in range(len(self.arrSchedineGioc[i][l])):
                #for k in range(len(self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l])):
                    """print("i: ",i, end=" ")
                    print("l: ",l, end=" ")
                    print("k: ",k)"""
                    if self.giocatoriGioc[self.currentPlayer].getSchedine()[i][l][k][0] == " ":
                        self.arrSchedineGioc[i][l][k].configure(state=tk.DISABLED)
                    else:
                        self.arrSchedineGioc[i][l][k].configure(state=tk.NORMAL)
                    """if self.giocatoriCpu[self.currentPlayer].getNome() == self.nickname.get():
                        #print(self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][0])
                        if self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][0] != " ":
                            self.arrSchedine[i][l][k].configure(state=tk.NORMAL)
                        else:
                            self.arrSchedine[i][l][k].configure(state=tk.DISABLED)
                    else:
                        self.arrSchedine[i][l][k].configure(state=tk.DISABLED)"""
                    self.arrSchedineGioc[i][l][k].configure(text=self.giocatoriGioc[self.currentPlayer].getSchedine()[i][l][k][0])

                    if self.giocatoriGioc[self.currentPlayer].getSchedine()[i][l][k][1] == "unset":
                        self.arrSchedineGioc[i][l][k].configure(bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color)
                        self.arrSchedineGioc[i][l][k].configure(relief=tk.RAISED)
                    elif self.giocatoriGioc[self.currentPlayer].getSchedine()[i][l][k][1] == "set":
                        self.arrSchedineGioc[i][l][k].configure(bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color)
                        self.arrSchedineGioc[i][l][k].configure(relief=tk.SUNKEN)
        #print("-------------------------------------------------------------")

    def salvaSuono(self):
        self.playSuono()
        self.salva(event=None)

    def salva(self, event):
        self.updateVolumeMusica()
        self.Menu(event=None)

    def ImpostazioniSuono(self):
        self.playSuono()
        self.Impostazioni(event=None)

    def Impostazioni(self, event):
        # Porta in primo piano la schermata delle Impostazioni

        self.master.bind('Left', self.doNothing)
        self.master.bind('Right', self.doNothing)
        self.master.bind('<Button-3>', self.doNothing)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Return>', self.salva)  #Salva
        self.master.bind('<Escape>', self.indietro)

        #self.master.configure(bg=self.impostazioni_sfondo_bg_color)

        self.currentWindow = "Impostazioni"

        self.framePunteggio.grid_forget()
        self.frameMenu.grid_forget()
        self.frameGiocoCPU.grid_forget()
        self.framePreGiocoCPU.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.framePreGiocoGioc.grid_forget()
        self.frameTipoGioco.grid_forget()
        self.frameImpostazioni.grid(row=0, column=0, sticky="nesw")
        #self.frameGioco.pack_forget()
        #self.frameMenu.pack_forget()
        #self.frameImpostazioni.pack()

        self.oldVolume=self.volume.get()
        self.oldTema=self.tema.get()
        self.old_menu_sfondo_bg_color = self.menu_sfondo_bg_color
        self.old_menu_titolo_bg_color= self.menu_titolo_bg_color
        self.old_menu_titolo_fg_color=self.menu_titolo_fg_color
        self.old_menu_buttons_bg_color=self.menu_buttons_bg_color
        self.old_menu_buttons_fg_color=self.menu_buttons_fg_color

        self.old_gioco_sfondo_bg_color=self.gioco_sfondo_bg_color
        self.old_gioco_titolo_bg_color=self.gioco_titolo_bg_color
        self.old_gioco_titolo_fg_color=self.gioco_titolo_fg_color
        self.old_gioco_label_bg_nestratto=self.gioco_label_nestratto_bg_color
        self.old_gioco_label_fg_nestratto=self.gioco_label_nestratto_fg_color
        self.old_gioco_nestratto_bg_color=self.gioco_nestratto_bg_color
        self.old_gioco_nestratto_fg_color=self.gioco_nestratto_fg_color
        self.old_gioco_tabellone_unset_bg_color=self.gioco_tabellone_unset_bg_color
        self.old_gioco_tabellone_unset_fg_color=self.gioco_tabellone_unset_fg_color
        self.old_gioco_tabellone_set_bg_color=self.gioco_tabellone_set_bg_color
        self.old_gioco_tabellone_set_fg_color=self.gioco_tabellone_set_fg_color
        self.old_gioco_schedine_unset_bg_color=self.gioco_schedine_unset_bg_color
        self.old_gioco_schedine_unset_fg_color=self.gioco_schedine_unset_fg_color
        self.old_gioco_schedine_set_bg_color=self.gioco_schedine_set_bg_color
        self.old_gioco_schedine_set_fg_color=self.gioco_schedine_set_fg_color
        self.old_gioco_schedine_disabled_fg_color=self.gioco_schedine_disabled_fg_color
        self.old_gioco_logs_bg_color = self.gioco_logs_bg_color
        self.old_gioco_logs_fg_color = self.gioco_logs_fg_color
        self.old_gioco_framedestro_bg_color = self.gioco_framedestro_bg_color
        self.old_gioco_classifica_bg_color = self.gioco_classifica_bg_color
        self.old_gioco_classifica_titolo_fg_color = self.gioco_classifica_titolo_fg_color
        self.old_gioco_classifica_tabella_fg_color = self.gioco_classifica_tabella_fg_color
        self.old_gioco_premi_bg_color = self.gioco_premi_bg_color
        self.old_gioco_premi_titolo_fg_color = self.gioco_premi_titolo_fg_color
        self.old_gioco_premi_btns_bg_color = self.gioco_premi_btns_bg_color
        self.old_gioco_premi_btns_fg_color = self.gioco_premi_btns_fg_color

        self.old_pregioco_sfondo_bg_color = self.pregioco_sfondo_bg_color
        self.old_pregioco_titolo_bg_color = self.pregioco_titolo_bg_color
        self.old_pregioco_titolo_fg_color = self.pregioco_titolo_fg_color
        self.old_pregioco_labels_bg_color = self.pregioco_labels_bg_color
        self.old_pregioco_labels_fg_color = self.pregioco_labels_fg_color
        self.old_pregioco_options_bg_color = self.pregioco_options_bg_color
        self.old_pregioco_options_fg_color = self.pregioco_options_fg_color
        self.old_pregioco_rbtn_circle_bg_color = self.pregioco_rbtn_circle_bg_color

        self.old_impostazioni_sfondo_bg_color=self.impostazioni_sfondo_bg_color
        self.old_impostazioni_titolo_bg_color=self.impostazioni_titolo_bg_color
        self.old_impostazioni_titolo_fg_color=self.impostazioni_titolo_fg_color
        self.old_impostazioni_labels_bg_color=self.impostazioni_labels_bg_color
        self.old_impostazioni_labels_fg_color=self.impostazioni_labels_fg_color
        self.old_impostazioni_options_bg_color=self.impostazioni_options_bg_color
        self.old_impostazioni_options_fg_color=self.impostazioni_options_fg_color
        self.old_impostazioni_rbtn_circle_bg_color=self.impostazioni_rbtn_circle_bg_color

    def indietroSuono(self):
        self.playSuono()
        self.indietro(event=None)

    def indietro(self, event):
        # Se non si salvano le impostazioni selezionate
        # non le aggiorna nelle variabili globali
        self.volume.set(self.oldVolume)
        self.tema.set(self.oldTema)
        self.menu_sfondo_bg_color = self.old_menu_sfondo_bg_color
        self.menu_titolo_bg_color= self.old_menu_titolo_bg_color
        self.menu_titolo_fg_color=self.old_menu_titolo_fg_color
        self.menu_buttons_bg_color=self.old_menu_buttons_bg_color
        self.menu_buttons_fg_color=self.old_menu_buttons_fg_color

        self.gioco_sfondo_bg_color=self.old_gioco_sfondo_bg_color
        self.gioco_titolo_bg_color=self.old_gioco_titolo_bg_color
        self.gioco_titolo_fg_color=self.old_gioco_titolo_fg_color
        self.gioco_label_nestratto_bg_color=self.old_gioco_label_bg_nestratto
        self.gioco_label_nestratto_fg_color=self.old_gioco_label_fg_nestratto
        self.gioco_nestratto_bg_color=self.old_gioco_nestratto_bg_color
        self.gioco_nestratto_fg_color=self.old_gioco_nestratto_fg_color
        self.gioco_tabellone_unset_bg_color=self.old_gioco_tabellone_unset_bg_color
        self.gioco_tabellone_unset_fg_color=self.old_gioco_tabellone_unset_fg_color
        self.gioco_tabellone_set_bg_color=self.old_gioco_tabellone_set_bg_color
        self.gioco_tabellone_set_fg_color=self.old_gioco_tabellone_set_fg_color
        self.gioco_schedine_unset_bg_color=self.old_gioco_schedine_unset_bg_color
        self.gioco_schedine_unset_fg_color=self.old_gioco_schedine_unset_fg_color
        self.gioco_schedine_set_bg_color=self.old_gioco_schedine_set_bg_color
        self.gioco_schedine_set_fg_color=self.old_gioco_schedine_set_fg_color
        self.gioco_schedine_disabled_fg_color=self.old_gioco_schedine_disabled_fg_color
        self.gioco_logs_bg_color = self.old_gioco_logs_bg_color
        self.gioco_logs_fg_color = self.old_gioco_logs_fg_color
        self.gioco_framedestro_bg_color = self.old_gioco_framedestro_bg_color
        self.gioco_classifica_bg_color = self.old_gioco_classifica_bg_color
        self.gioco_classifica_titolo_fg_color = self.old_gioco_classifica_titolo_fg_color
        self.gioco_classifica_tabella_fg_color = self.old_gioco_classifica_tabella_fg_color
        self.gioco_premi_bg_color = self.old_gioco_premi_bg_color
        self.gioco_premi_titolo_fg_color = self.old_gioco_premi_titolo_fg_color
        self.gioco_premi_btns_bg_color = self.old_gioco_premi_btns_bg_color
        self.gioco_premi_btns_fg_color = self.old_gioco_premi_btns_fg_color

        self.pregioco_sfondo_bg_color = self.old_pregioco_sfondo_bg_color
        self.pregioco_titolo_bg_color = self.old_pregioco_titolo_bg_color
        self.pregioco_titolo_fg_color = self.old_pregioco_titolo_fg_color
        self.pregioco_labels_bg_color = self.old_pregioco_labels_bg_color
        self.pregioco_labels_fg_color = self.old_pregioco_labels_fg_color
        self.pregioco_options_bg_color = self.old_pregioco_options_bg_color
        self.pregioco_options_fg_color = self.old_pregioco_options_fg_color
        self.pregioco_rbtn_circle_bg_color = self.old_pregioco_rbtn_circle_bg_color

        self.impostazioni_sfondo_bg_color=self.old_impostazioni_sfondo_bg_color
        self.impostazioni_titolo_bg_color=self.old_impostazioni_titolo_bg_color
        self.impostazioni_titolo_fg_color=self.old_impostazioni_titolo_fg_color
        self.impostazioni_labels_bg_color=self.old_impostazioni_labels_bg_color
        self.impostazioni_labels_fg_color=self.old_impostazioni_labels_fg_color
        self.impostazioni_options_bg_color=self.old_impostazioni_options_bg_color
        self.impostazioni_options_fg_color=self.old_impostazioni_options_fg_color
        self.impostazioni_rbtn_circle_bg_color=self.old_impostazioni_rbtn_circle_bg_color

        self.Menu(event=None)

    def indietroPreGiocoGiocSuono(self):
        self.playSuono()
        self.indietroPreGiocoGioc(event=None)

    def indietroPreGiocoGioc(self, event):
        self.nickname.set(self.oldNickname)
        self.nGiocatoriGioc.set(self.oldNGiocatoriGioc)
        self.nSchedineGioc.set(self.oldNSchedineGioc)

        self.Menu(event=None)

    def indietroPreGiocoCPUSuono(self):
        self.playSuono()
        self.indietroPreGiocoCPU(event=None)

    def indietroPreGiocoCPU(self, event):
        self.nickname.set(self.oldNickname)
        self.nGiocatoriCPU.set(self.oldNGiocatoriCPU)
        self.nSchedineCPU.set(self.oldNSchedineCPU)

        self.Menu(event=None)

    def clickGiocSuono(self, giocatore, nscheda, nriga, ncella, flag):
        self.playSuono()
        self.clickGioc(giocatore, nscheda, nriga, ncella, flag)

    def clickGioc(self, giocatore, nScheda, nRiga, nCella, flag):
        # colora la cella selezionata quando la si
        # clicca nella grid(vale solo per il giocatore)

        #if flag != "cpu":
            # Segna i numeri cliccati nelle schedine
            #if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][nCella][0] != " ":
        if self.arrSchedineGioc[nScheda][nRiga][nCella].cget("bg") == self.gioco_schedine_unset_bg_color:
            self.arrSchedineGioc[nScheda][nRiga][nCella].configure(bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color, relief=tk.SUNKEN)
            arr = self.giocatoriGioc[self.currentPlayer].getSchedine()
            num = self.giocatoriGioc[self.currentPlayer].getSchedine()[nScheda][nRiga][nCella][0]
            commnd = "set"
            tupla = [num, commnd]
            arr[nScheda][nRiga][nCella] = tupla
            self.giocatoriGioc[self.currentPlayer].setSchedine(arr)
        else:
            self.arrSchedineGioc[nScheda][nRiga][nCella].configure(bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color, relief=tk.RAISED)
            arr = self.giocatoriGioc[self.currentPlayer].getSchedine()
            num = self.giocatoriGioc[self.currentPlayer].getSchedine()[nScheda][nRiga][nCella][0]
            commnd = "unset"
            tupla = [num, commnd]
            arr[nScheda][nRiga][nCella] = tupla
            self.giocatoriGioc[self.currentPlayer].setSchedine(arr)
            """"#DEBUG
            print("You clicked:")
            print("\t Giocatore:"+self.giocatoriCpu[giocatore].getNome())
            print("\t nScheda:",nScheda)
            print("\t nRiga:",nRiga)
            print("\t nCella:", nCella)"""

        # Effettua i controlli per i premi
        counterPronto = 0
        for j in range(len(self.giocatoriGioc)):
            if self.giocatoriGioc[j].getFlagPronto():
                counterPronto+=1
        if counterPronto == len(self.giocatoriGioc):
            #self.checkByVars(giocatore, nScheda, nRiga)
            self.checkByVarsMulti()

    def clickCPUSuono(self, giocatore, nscheda, nriga, ncella, flag):
        self.playSuono()
        self.clickCPU(giocatore, nscheda, nriga, ncella, flag)

    def clickCPU(self, giocatore, nScheda, nRiga, nCella, flag):
        # colora la cella selezionata quando la si
        # clicca nella grid(vale solo per il giocatore)

        if flag != "cpu":
            # Segna i numeri cliccati nelle schedine
            if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][nCella][0] != " ":
                if self.arrSchedineCPU[nScheda][nRiga][nCella].cget("bg") == self.gioco_schedine_unset_bg_color:
                    self.arrSchedineCPU[nScheda][nRiga][nCella].configure(bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color, relief=tk.SUNKEN)
                    arr = self.giocatoriCpu[self.currentPlayer].getSchedine()
                    num = self.giocatoriCpu[self.currentPlayer].getSchedine()[nScheda][nRiga][nCella][0]
                    commnd = "set"
                    tupla = [num, commnd]
                    arr[nScheda][nRiga][nCella] = tupla
                    self.giocatoriCpu[self.currentPlayer].setSchedine(arr)
                else:
                    self.arrSchedineCPU[nScheda][nRiga][nCella].configure(bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color, relief=tk.RAISED)
                    arr = self.giocatoriCpu[self.currentPlayer].getSchedine()
                    num = self.giocatoriCpu[self.currentPlayer].getSchedine()[nScheda][nRiga][nCella][0]
                    commnd = "unset"
                    tupla = [num, commnd]
                    arr[nScheda][nRiga][nCella] = tupla
                    self.giocatoriCpu[self.currentPlayer].setSchedine(arr)
            """"#DEBUG
            print("You clicked:")
            print("\t Giocatore:"+self.giocatoriCpu[giocatore].getNome())
            print("\t nScheda:",nScheda)
            print("\t nRiga:",nRiga)
            print("\t nCella:", nCella)"""

        # Effettua i controlli per i premi
        self.checkByVars(giocatore, nScheda, nRiga)

    def checkByVars(self, giocatore, nScheda, nRiga):
        # Controllo chi ha vinto il premio e lo stampo

        #DEBUG
        """print("Giocatore CheckByVars: " + str(giocatore))
        print("NScheda CheckByVars: " + str(nScheda))
        print("NRiga CheckByVars: " + str(nRiga))
        print("------------------------------------------------------")"""

        self.txtLogs.config(state=tk.NORMAL)

        counter=0
        # celle
        for y in range(len(self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga])):
            if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][y][1] == "set":
                for i in range(len(self.arrTabellone)):
                    if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][y][0] != " ":
                        if self.arrTabellone[i].cget("bg") == self.gioco_tabellone_set_bg_color  and  int(self.arrTabellone[i].cget("text")) == int(self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][y][0]):
                            counter+=1

        #Giocatore
        """if self.giocatoriCpu[giocatore].getNome() == self.nickname.get():
            if counter==2 and self.ambo is False:
                self.ambo=True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+2)
                self.punteggio=self.punteggio+2
                self.updateClassProv()
                print("Hai fatto AMBO sulla scheda N." + str(nScheda+1) + " e hai gudagnato 2 punti")
                self.btnAmbo.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
                self.txtLogs.insert(tk.END, "Hai fatto AMBO sulla scheda N." + str(nScheda+1) + " (2 pt)")

                #messagebox.showinfo("CONGRATULAZIONI "+self.giocatoriCpu[giocatore].getNome()+"!!", "Hai fatto AMBO sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 2 punti")
            elif counter==3 and self.terna is False:
                self.terna = True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+3)
                self.punteggio = self.punteggio + 3
                self.updateClassProv()
                print("Hai fatto TERNA sulla scheda N.", nScheda+1 , " e hai gudagnato 3 punti")
                self.btnTerna.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
                self.txtLogs.insert(tk.END, "\nHai fatto TERNA sulla scheda N."+ str(nScheda+1) + " (3 pt)")
                #messagebox.showinfo("CONGRATULAZIONI "+self.giocatoriCpu[giocatore].getNome()+"!!", "Hai fatto TERNA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 3 punti")
            elif counter==4 and self.quaterna is False:
                self.quaterna = True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+4)
                self.punteggio = self.punteggio + 4
                self.updateClassProv()
                print("Hai fatto QUATERNA sulla scheda N.", nScheda+1 , " e hai gudagnato 4 punti")
                self.btnQuaterna.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
                self.txtLogs.insert(tk.END, "\nHai fatto QUATERNA sulla scheda N."+ str(nScheda+1) + " (4 pt)")
                #messagebox.showinfo("CONGRATULAZIONI "+self.giocatoriCpu[giocatore].getNome()+"!!"+ "Hai fatto QUATERNA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 4 punti")
            elif counter==5 and self.cinquina is False:
                self.cinquina = True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+5)
                self.punteggio = self.punteggio + 5
                self.updateClassProv()
                print("Hai fatto CINQUINA sulla scheda N.", nScheda+1 , " e hai gudagnato 5 punti")
                self.btnCinquina.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
                self.txtLogs.insert(tk.END, "\nHai fatto CINQUINA sulla scheda N."+ str(nScheda+1) + " (5 pt)")
                #messagebox.showinfo("CONGRATULAZIONI "+self.giocatoriCpu[giocatore].getNome()+"!!"+"Hai fatto CINQUINA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 5 punti")
        #CPU
        else:"""
        if counter==2 and self.ambo is False:
            self.ambo=True
            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+2)
            self.updateClassProv()
            print(self.giocatoriCpu[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda+1))
            self.btnAmbo.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogs.insert(tk.END, self.giocatoriCpu[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda+1) + " (2 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Ambo sulla scheda N." + str(nScheda + 1))
        elif counter==3 and self.terna is False:
            self.terna = True
            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+3)
            self.updateClassProv()
            print(self.giocatoriCpu[giocatore].getNome() + " ha fatto TERNA sulla scheda N.", nScheda+1)
            self.btnTerna.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogs.insert(tk.END, "\n" + self.giocatoriCpu[giocatore].getNome() + " ha fatto TERNA sulla scheda N."+ str(nScheda+1) + " (3 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Terna sulla scheda N." + str(nScheda + 1))
        elif counter==4 and self.quaterna is False:
            self.quaterna = True
            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+4)
            self.updateClassProv()
            print(self.giocatoriCpu[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N."+ str(nScheda+1))
            self.btnQuaterna.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogs.insert(tk.END, "\n" + self.giocatoriCpu[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N."+ str(nScheda+1) + " (4 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Quaterna sulla scheda N." + str(nScheda + 1))
        elif counter==5 and self.cinquina is False:
            self.cinquina = True
            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+5)
            self.updateClassProv()
            print(self.giocatoriCpu[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N."+ str(nScheda+1))
            self.btnCinquina.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogs.insert(tk.END, "\n" + self.giocatoriCpu[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N."+ str(nScheda+1) + " (5 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Cinquina sulla scheda N." + str(nScheda + 1))



        counterWin1 = 0
        self.previousWinner = ""
        for y in range(len(self.giocatoriCpu[giocatore].getSchedine()[nScheda])):
            for h in range(len(self.giocatoriCpu[giocatore].getSchedine()[nScheda][y])):
                if self.giocatoriCpu[giocatore].getSchedine()[nScheda][y][h][1] == "set":
                    counterWin1 += 1

        if counterWin1 == 15 and self.tombola is False:
            #if self.giocatoriCpu[giocatore].getNome() == self.nickname.get():
            if self.verificaValiditaPremi(giocatore) == True:
                self.tombola = True
                print("HAI VINTOOOOOOOOO!!! Con ",self.giocatoriCpu[giocatore].getPunteggioCorrente(), " punti!")
                self.txtLogs.insert(tk.END, "\n HAI FATTO TOMBOLA sulla scheda N." + str(nScheda+1) + " con " + str(self.giocatoriCpu[giocatore].getPunteggioCorrente()) + " punti!")
                #messagebox.showinfo("GRANDE!!   HAI VINTO!!!", "HAI FATTO TOMBOLA sulla scheda N."+ str(nScheda+1) +" \n con punteggio di "+str(self.giocatoriCpu[giocatore].getPunteggioCorrente())+"!!!")
                #self.previousWinner = self.giocatoriCpu[giocatore].getNome()
                self.showClassifica()
            elif self.verificaValiditaPremi(giocatore) == False:
                print("Non hai vinto perche' hai barato!")
                messagebox.showerror("Non si puo fare >:(", "LA SCHEDINA N. " + str(nScheda+1) + " NON E' VALIDA!!!")
            """else:
                print("Mi dispiace, hai perso...")
                self.txtLogs.insert(tk.END, "\n" + self.giocatoriCpu[giocatore].getNome() + " ha fatto TOMBOLA sulla scheda N." + str(nScheda + 1) + " con " + str(self.giocatoriCpu[giocatore].getPunteggioCorrente()) + " punti!")
                messagebox.showwarning("CHE PECCATO!! Hai perso...  Ma c'e' ancora Tombolino :)", self.giocatoriCpu[giocatore].getNome()+" ha fatto TOMBOLA sulla scheda N." + str(nScheda + 1) + "...")
                self.previousWinner=self.giocatoriCpu[giocatore].getNome()
                self.showClassifica()"""

        """if counterWin1 == 15 and self.tombola is True and self.tombolino is False and self.previousWinner != self.giocatoriCpu[giocatore].getNome():
            self.tombolino = True
            if self.giocatoriCpu[giocatore].getNome() == self.nickname.get():
                if self.verificaValiditaPremi(giocatore) == True:
                    print("Secondo Posto! Con ", self.giocatoriCpu[giocatore].getPunteggioCorrente(), " punti!")
                    messagebox.showinfo("GRANDE!   SEI SECONDO", "HAI FATTO TOMBOLINO sulla scheda N." + str(nScheda + 1)+" \n con un punteggio di "+str(self.giocatoriCpu[giocatore].getPunteggioCorrente()))
                    self.showClassifica()
                elif self.verificaValiditaPremi(giocatore) == False:
                    self.tombolino = False
                    print("Non hai vinto perche' hai barato!")
                    messagebox.showerror("Non si puo fare >:(", "LA SCHEDINA N. " + str(nScheda + 1) + " NON E' VALIDA!!!")
            else:
                print(self.giocatoriCpu[giocatore].getNome()+" ha fatto TOMBOLINO sulla scheda N." + str(nScheda+1))
                print("Tranquillo, hai vinto lo stesso ;)")
                messagebox.showwarning("MHhh...", self.giocatoriCpu[giocatore].getNome()+" ha fatto TOMBOLINO sulla scheda N." + str(nScheda + 1) + "...")
                self.showClassifica()"""

        counterCroupier = 0
        loseByCroupier = 0
        for y in range(len(self.arrTabellone)):
            if self.arrTabellone[y].cget("bg") == self.gioco_tabellone_set_bg_color:
                counterCroupier += 1
        # DEBUG  print("Counter Croupier: ",counter)
        # DEBUG  print("N Estratto: ", randN)

        """if counterCroupier == 90:
            loseByCroupier += 1
            if loseByCroupier == 1:
                self.after(10000, lambda:self.faVincereIlCroupier())"""

        self.txtLogs.config(state=tk.DISABLED)

    def checkByVarsMulti(self):

        giocatore=""
        nScheda=""
        nRiga=""
        cella=""
        #counter=[["", 0]]
        counter=0
        #counterRiga=0

        for nScheda in range(self.nSchedineGioc.get()):
            for nRiga in range(3):
                counter=0
                for giocatore in range(len(self.giocatoriCpu)):
                #for nScheda in range(len(self.giocatoriCpu[giocatore].getSchedine())):
                    for cella in range(len(self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga])):
                        if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][cella][1] == "set":
                            for i in range(len(self.arrTabellone)):
                                if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][cella][0] != " ":
                                    #counterRiga += 1
                                    if self.arrTabellone[i].cget("bg") == self.gioco_tabellone_set_bg_color and int(self.arrTabellone[i].cget("text")) == int(self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][cella][0]):
                                        #counter.append([self.giocatoriCpu[giocatore]])
                                        counter += 1
                                        #if counterRiga == 5:
                                        #    counterRiga=0
                                        #    counter=0
                        #if self.giocatoriCpu[giocatore].getNome() == self.nickname.get():
                        if counter == 2 and self.ambo is False:
                            self.ambo = True
                            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente() + 2)
                            print("Hai fatto AMBO sulla scheda N." + str(nScheda + 1), " e hai gudagnato 2 punti")
                            messagebox.showinfo("CONGRATULAZIONI " + self.giocatoriCpu[giocatore].getNome() + "!!","Hai fatto AMBO sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 2 punti")
                        elif counter == 3 and self.terna is False:
                            self.terna = True
                            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente() + 3)
                            print("Hai fatto TERNA sulla scheda N.", nScheda + 1, " e hai gudagnato 3 punti")
                            messagebox.showinfo("CONGRATULAZIONI " + self.giocatoriCpu[giocatore].getNome() + "!!","Hai fatto TERNA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 3 punti")
                        elif counter == 4 and self.quaterna is False:
                            self.quaterna = True
                            self.giocatoriCpu[giocatore].setPunteggioCorrente(
                                self.giocatoriCpu[giocatore].getPunteggioCorrente() + 4)
                            print("Hai fatto QUATERNA sulla scheda N.", nScheda + 1, " e hai gudagnato 4 punti")
                            messagebox.showinfo("CONGRATULAZIONI " + self.giocatoriCpu[giocatore].getNome() + "!!",
                                                "Hai fatto QUATERNA sulla scheda N." + str(
                                                    nScheda + 1) + "\n   Hai gudagnato 4 punti")
                        elif counter == 5 and self.cinquina is False:
                            self.cinquina = True
                            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente() + 5)
                            print("Hai fatto CINQUINA sulla scheda N.", nScheda + 1, " e hai gudagnato 5 punti")
                            messagebox.showinfo("CONGRATULAZIONI " + self.giocatoriCpu[giocatore].getNome() + "!!","Hai fatto CINQUINA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 5 punti")
                        """# CPU
                        else:
                            if counter == 2 and self.ambo is False:
                                self.ambo = True
                                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente() + 2)
                                print(self.giocatoriCpu[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda + 1))
                                messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Ambo sulla scheda N." + str(nScheda + 1))
                            elif counter == 3 and self.terna is False:
                                self.terna = True
                                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente() + 3)
                                print(self.giocatoriCpu[giocatore].getNome() + " ha fatto TERNA sulla scheda N.",nScheda + 1)
                                messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Terna sulla scheda N." + str(nScheda + 1))
                            elif counter == 4 and self.quaterna is False:
                                self.quaterna = True
                                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente() + 4)
                                print(self.giocatoriCpu[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N.",nScheda + 1)
                                messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Quaterna sulla scheda N." + str(nScheda + 1))
                            elif counter == 5 and self.cinquina is False:
                                self.cinquina = True
                                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente() + 5)
                                print(self.giocatoriCpu[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N.",nScheda + 1)
                                messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Cinquina sulla scheda N." + str(nScheda + 1))"""

    def verificaValiditaPremi(self, giocatore):
        # Controllo se il giocatore ha veramente
        # fatto tombola giocando o se ha selezionato
        # tutte le celle prima che venissero estratti

        counterCellePlayer=0
        #schedine
        for i in range(len(self.giocatoriCpu[giocatore].getSchedine())):
            #righe
            for l in range(len(self.giocatoriCpu[giocatore].getSchedine()[i])):
                #celle
                for y in range(len(self.giocatoriCpu[giocatore].getSchedine()[i][l])):
                    if self.giocatoriCpu[giocatore].getSchedine()[i][l][y][1] == "set":
                        counterCellePlayer+=1
        #DEBUG
        print("CounterCellePlayer: ", counterCellePlayer)

        counterInTabellone = 0
        # schedine
        for i in range(len(self.giocatoriCpu[giocatore].getSchedine())):
            # righe
            for l in range(len(self.giocatoriCpu[giocatore].getSchedine()[i])):
                # celle
                for y in range(len(self.giocatoriCpu[giocatore].getSchedine()[i][l])):
                    if self.giocatoriCpu[giocatore].getSchedine()[i][l][y][1] == "set"   and   self.arrTabellone[y].cget("bg") == self.gioco_tabellone_set_bg_color:
                        counterInTabellone += 1
        # DEBUG
        print("CounterInTabellone: ", counterInTabellone)

        if counterCellePlayer == counterInTabellone:
            return True
        else:
            return False

    def showClassifica(self):
        #Mostro la Classifica
        self.Classifica = tk.Toplevel(self)
        self.Classifica.title("Classifica")
        frameClassifica = tk.Frame(self.Classifica, bg=self.gioco_sfondo_bg_color)
        if self.previousWinner == self.nickname.get():
            lblClassifica = tk.Label(frameClassifica, text="Vittoria", font=("Helvetica", 50), bg=self.gioco_titolo_bg_color, fg="yellow").grid(row=0, column=1, pady=10, padx=20, sticky="nesw")
        else:
            lblClassifica = tk.Label(frameClassifica, text="Sconfitta", font=("Helvetica", 50), bg=self.gioco_titolo_bg_color, fg="red").grid(row=0, column=1, pady=10, padx=20, sticky="nesw")
        frameInfo = tk.Frame(frameClassifica)
        lbl1 = tk.Label(frameInfo, text="Nome", font=("Helvetica", 30), bd=1, bg=self.gioco_sfondo_bg_color, fg=self.gioco_titolo_fg_color).grid(row=0, column=0, sticky="nesw")
        lbl2 = tk.Label(frameInfo, text="Punteggio", font=("Helvetica", 30), bd=1, bg=self.gioco_sfondo_bg_color, fg=self.gioco_titolo_fg_color).grid(row=0, column=1, sticky="nesw")

        classificaGiocatori=self.ordinaClassifica()

        #Giocatori
        for i in range(len(classificaGiocatori)):
            if classificaGiocatori[i].getNome() == self.nickname.get() and classificaGiocatori[i].getPunteggioCorrente() == 0:
                lblNome = tk.Button(frameInfo, disabledforeground=self.gioco_schedine_set_fg_color, state=tk.DISABLED,font=("Helvetica", 30), text=classificaGiocatori[i].getNome(),command=lambda: self.goToPlayerClassifica(self.giocatoriCpu[i].getNome()),relief=tk.SOLID, bg=self.gioco_schedine_set_bg_color,fg=self.gioco_schedine_set_fg_color).grid(row=1, column=0, sticky="nesw")
                lblPunt = tk.Button(frameInfo, disabledforeground=self.gioco_schedine_set_fg_color, state=tk.DISABLED,font=("Helvetica", 30), text=classificaGiocatori[i].getPunteggioCorrente(),command=lambda: self.goToPlayerClassifica(classificaGiocatori.getNome()),relief=tk.SOLID, bg=self.gioco_schedine_set_bg_color,fg=self.gioco_schedine_set_fg_color).grid(row=1, column=1, sticky="nesw")
            elif self.previousWinner == classificaGiocatori[i].getNome():
                lblNome=tk.Button(frameInfo, disabledforeground=self.gioco_schedine_unset_fg_color, state=tk.DISABLED, font=("Helvetica", 30), text=classificaGiocatori[i].getNome(), command=lambda:self.goToPlayerClassifica(self.giocatoriCpu[i].getNome()), relief=tk.SOLID, bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color).grid(row=2, column=0, sticky="nesw")
                lblPunt=tk.Button(frameInfo, disabledforeground=self.gioco_schedine_unset_fg_color, state=tk.DISABLED, font=("Helvetica", 30), text=classificaGiocatori[i].getPunteggioCorrente(), command=lambda:self.goToPlayerClassifica(classificaGiocatori.getNome()), relief=tk.SOLID, bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color).grid(row=2, column=1, sticky="nesw")
            elif classificaGiocatori[i].getPunteggioCorrente() != 0:
                lblNome = tk.Button(frameInfo, disabledforeground=self.gioco_schedine_set_fg_color, state=tk.DISABLED, font=("Helvetica", 30), text=classificaGiocatori[i].getNome(), command=lambda:self.goToPlayerClassifica(self.giocatoriCpu[i].getNome()), relief=tk.SOLID, bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color).grid( row=i + 3, column=0, sticky="nesw")
                lblPunt = tk.Button(frameInfo, disabledforeground=self.gioco_schedine_set_fg_color, state=tk.DISABLED, font=("Helvetica", 30), text=classificaGiocatori[i].getPunteggioCorrente(), command=lambda:self.goToPlayerClassifica(classificaGiocatori.getNome()), relief=tk.SOLID, bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color).grid(row=i + 3, column=1, sticky="nesw")
        frameInfo.grid(row=1, rowspan=10, column=0, columnspan=3, padx=20)
        btnVaialMenu=tk.Button(frameClassifica, font=("Helvetica", 30), text="Rigioca", command=lambda:self.replayClassifica(), bg=self.gioco_sfondo_bg_color, fg=self.gioco_classifica_titolo_fg_color).grid(row=11, column=0, columnspan=2, sticky="nsw")
        btnEsci=tk.Button(frameClassifica, font=("Helvetica", 30), text="Menu", command=lambda:self.goToMenuClassifica(), bg=self.gioco_sfondo_bg_color, fg=self.gioco_classifica_titolo_fg_color).grid(row=11, column=1, columnspan=2, sticky="nes")
        frameClassifica.grid()

    def replayClassifica(self):
        self.playSuono()
        self.Menu(event=None)
        self.Gioca(event=None)
        self.Classifica.destroy()

    def goToMenuClassifica(self):
        self.playSuono()
        pygame.mixer.music.pause()
        pygame.mixer.music.load(self.currentDirectory + "/Files/Musica/ColonneSonore/Shake.ogg")
        pygame.mixer.music.play(-1)
        self.Menu(event=None)
        self.Classifica.destroy()

    def updateVolumeMusica(self):
        pygame.mixer.music.set_volume(self.volume.get()/100)
    
    def playSuono(self):
        pygame.mixer.Sound.play(self.clickSound)



root = Tombolone()

root.mainloop()
