import tkinter as tk
from tkinter import messagebox, filedialog
from os import path
import os, random
import pygame as pygame


class Giocatore():
    def __init__(self, nome):
        self._nomeLogin=""
        self._nome=nome
        self._schedine=[]
        self._punteggioCorrente=0
        self._crediti=50
        self._classifica=[]
        self._flagPronto=False
        self._password=""
        self._ambo=False
        self._terna = False
        self._quaterna = False
        self._cinquina = False

    def setAmbo(self, value):
        self._ambo=value

    def getAmbo(self):
        return self._ambo

    def setTerna(self, value):
        self._terna = value

    def getTerna(self):
        return self._terna

    def setQuaterna(self, value):
        self._quaterna = value

    def getQuaterna(self):
        return self._quaterna

    def setCinquina(self, value):
        self._cinquina = value

    def getCinquina(self):
        return self._cinquina

    def setPassword(self, password):
        self._password=password

    def getPassword(self):
        return self._password

    def setNomeLogin(self, name):
        self._nomeLogin=name

    def getNomeLogin(self):
        return self._nomeLogin

    def setCrediti(self, crediti):
        self._crediti=crediti

    def getCrediti(self):
        return self._crediti

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
        self.fileDirStorico = self.currentDirectory+"/Files/Infos/StoricoPartite.txt"
        self.fileDirCredenziali = self.currentDirectory+"/Files/Infos/Credenziali.txt"
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
        self.master.bind('<Control-Shift-Up>', self.alzaVolume)
        self.master.bind('<Control-Shift-Down>', self.abbassaVolume)
        self.grid()
        print(self.currentDirectory)
        lblAltezza=tk.Label(self, text="", font=("Helvetica", 1), bg="black", height=int(self.altezza/2)).grid(row=0, column=1, sticky="ns")
        lblLarghezza=tk.Label(self, text="", font=("Helvetica", 1), bg="black", width=self.larghezza).grid(row=1, column=0, sticky="ew")
        self.globals()
        self.riempiListaUtenti()
        self.colors()
        pygame.mixer.init()
        pygame.mixer.music.pause()
        pygame.mixer.music.load(self.currentDirectory+"/Files/Musica/ColonneSonore/Shake.ogg")
        pygame.mixer.music.play(-1)
        self.clickSound=pygame.mixer.Sound(file=path.abspath(self.currentDirectory+"/Files/Musica/EffettiSonori/click.ogg"))
        self.CreateWidgets()
        #self.nGiocatoriGioc.trace("w", self.bloccaInizia())
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
        self.lblPunteggioTotale=tk.Label(self.framePunteggio, text="Crediti: "+ str(self.giocatore.getCrediti()), font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.punteggio_labels_bg_color, fg=self.punteggio_labels_fg_color)
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

        self.btnClassificaPersonale=tk.Button(self.frameMenu, text="{}", command=lambda:self.PunteggioSuono(), bg=self.menu_sfondo_bg_color, fg=self.menu_titolo_fg_color, font=("Helvetica", 15, "bold"), highlightthickness=0)
        self.btnClassificaPersonale.grid(row=0, column=0, columnspan=2, sticky="sw")

        self.lblTitoloMenu=tk.Label(self.frameMenu, text="Tombolone", bg=self.menu_titolo_bg_color, fg=self.menu_titolo_fg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54)))) #50
        self.lblTitoloMenu.grid(row=1, column=1, sticky="nesw")

        self.btnLoginMenu=tk.Button(self.frameMenu, text="Login", command=lambda: self.Login(), bg=self.menu_buttons_bg_color, fg=self.menu_buttons_fg_color, font=('Helvetica', int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0)
        self.btnLoginMenu.grid(row=0, rowspan=2, column=1, columnspan=2, sticky="ne")

        #spazioTraTitoloEScelte=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))).grid(row=2, column=1)


        self.frameBtns=tk.Frame(self.frameMenu, bg=self.menu_sfondo_bg_color)

        self.btnGioca=tk.Button(self.frameBtns, text="Gioca", width=14, command=lambda:self.TipoGiocoSuono(), bg=self.menu_buttons_bg_color, fg=self.menu_buttons_fg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0)
        #self.btnGioca.bind("<Return>", (lambda event: self.Gioca()))
        self.btnGioca.grid(row=0, column=1)

        spazioTraScelte=tk.Label(self.frameBtns, bg=self.menu_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=1, column=1) #20

        self.btnImpostazioni=tk.Button(self.frameBtns, text="Impostazioni", width=14, command=lambda:self.ImpostazioniSuono(), font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), fg=self.menu_buttons_fg_color, bg=self.menu_buttons_bg_color, highlightthickness=0)
        self.btnImpostazioni.grid(row=2, column=1)

        spazioTraScelte1=tk.Label(self.frameBtns, bg=self.menu_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=3, column=1)

        self.btnEsci=tk.Button(self.frameBtns, text="Esci", command=lambda: self.EsciSuono(), fg=self.menu_buttons_fg_color, bg=self.menu_buttons_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0)
        self.btnEsci.grid(row=4, column=1)


        self.frameBtns.grid(row=2, column=1)

        spazioTraScelteEBottom=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))).grid(row=3, column=1)

        self.frameMenu.columnconfigure(1, weight=1)
        self.frameMenu.rowconfigure(2, weight=2)


        # TODO*****************************************************************************************************************\
        #  **********************************************  LOG IN  ************************************************************\
        #  *********************************************************************************************************************

        self.frameLogin = tk.Frame(self.frameMenu, bg=self.impostazioni_sfondo_bg_color)


        self.lblTitoloLogin = tk.Label(self.frameLogin, text="Login", font=('Helvetica', int((self.altezza/30) + (self.larghezza/54))), bg=self.impostazioni_titolo_bg_color, fg=self.impostazioni_titolo_fg_color)
        self.lblTitoloLogin.grid(row=0, column=1, columnspan=2, pady=15)

        self.btnTornaAlMenuLogin = tk.Button(self.frameLogin, text="←", bg=self.impostazioni_titolo_bg_color, fg=self.impostazioni_titolo_fg_color, highlightthickness=0, font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))),bd=0, command=lambda: self.MenuSuono(), relief="solid")
        self.btnTornaAlMenuLogin.grid(row=0, column=0, columnspan=2, sticky="w")

        self.lblNomeLogin = tk.Label(self.frameLogin, text="Nome", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.impostazioni_labels_bg_color, fg=self.impostazioni_labels_fg_color)
        self.lblNomeLogin.grid(row=1, column=1, columnspan=2)

        self.nomeLogin = tk.StringVar(self, "")
        self.enNomeLogin = tk.Entry(self.frameLogin, textvariable=self.nomeLogin, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), width=20, bg=self.impostazioni_labels_bg_color, fg=self.impostazioni_labels_fg_color, highlightthickness=0)
        self.enNomeLogin.grid(row=2, column=1, columnspan=2)

        self.lblPasswordLogin = tk.Label(self.frameLogin, text="Password", font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))),bg=self.impostazioni_labels_bg_color, fg=self.impostazioni_labels_fg_color)
        self.lblPasswordLogin.grid(row=3, column=1, columnspan=2)

        self.passwordLogin = tk.StringVar(self, "")
        self.enPasswordLogin = tk.Entry(self.frameLogin, textvariable=self.passwordLogin, font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))), width=20, bg=self.impostazioni_labels_bg_color, fg=self.impostazioni_labels_fg_color, highlightthickness=0)
        self.enPasswordLogin.grid(row=4, column=1, columnspan=2)

        self.btnSignupLogin=tk.Button(self.frameLogin, text="Signup", width=7, command=lambda: self.Signup(), font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))), bg=self.impostazioni_options_bg_color, fg=self.impostazioni_options_fg_color, highlightthickness=0)
        self.btnSignupLogin.grid(row=5, column=1, pady=20)

        self.btnLoginLogin=tk.Button(self.frameLogin, text="Login", width=7, command=lambda: self.checkLogin(), font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))), bg=self.impostazioni_options_bg_color, fg=self.impostazioni_options_fg_color, highlightthickness=0)
        self.btnLoginLogin.grid(row=5, column=2)

        self.frameLogin.rowconfigure(1, weight=1)
        self.frameLogin.rowconfigure(2, weight=1)
        self.frameLogin.rowconfigure(3, weight=1)
        self.frameLogin.rowconfigure(4, weight=1)
        #self.frameLogin.rowconfigure(5, weight=1)

        self.frameLogin.grid(row=2, column=1, pady=20)


        # TODO*****************************************************************************************************************\
        #  **********************************************  SIGN UP  ***********************************************************\
        #  *********************************************************************************************************************

        self.frameSignup = tk.Frame(self.frameMenu, bg=self.impostazioni_sfondo_bg_color)

        self.lblTitoloSignup = tk.Label(self.frameSignup, text="Signup", font=('Helvetica', int((self.altezza/30) + (self.larghezza/54))), bg=self.impostazioni_titolo_bg_color,fg=self.impostazioni_titolo_fg_color)
        self.lblTitoloSignup.grid(row=0, column=1, columnspan=2, pady=20)

        self.btnTornaAlMenuSignup = tk.Button(self.frameSignup, text="←", bg=self.impostazioni_titolo_bg_color, fg=self.impostazioni_titolo_fg_color, highlightthickness=0, font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))), bd=0, command=lambda: self.MenuSuono(), relief="solid")
        self.btnTornaAlMenuSignup.grid(row=0, column=0, columnspan=2, sticky="w")

        self.lblNomeSignup = tk.Label(self.frameSignup, text="Nome", font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))),bg=self.impostazioni_labels_bg_color, fg=self.impostazioni_labels_fg_color)
        self.lblNomeSignup.grid(row=1, column=1, columnspan=2)

        self.nomeSignup = tk.StringVar(self, "")
        self.enNicknameSignup = tk.Entry(self.frameSignup, textvariable=self.nomeSignup, font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))), width=20,bg=self.impostazioni_labels_bg_color, fg=self.impostazioni_labels_fg_color, highlightthickness=0)
        self.enNicknameSignup.grid(row=2, column=1, columnspan=2)

        self.lblPassword1Signup = tk.Label(self.frameSignup, text="Password", font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))),bg=self.impostazioni_labels_bg_color, fg=self.impostazioni_labels_fg_color)
        self.lblPassword1Signup.grid(row=3, column=1, columnspan=2)

        self.password1Signup=tk.StringVar(self, "")
        self.enPassword1Signup = tk.Entry(self.frameSignup, textvariable=self.password1Signup, font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))),width=20, bg=self.impostazioni_labels_bg_color,fg=self.impostazioni_labels_fg_color, highlightthickness=0)
        self.enPassword1Signup.grid(row=4, column=1, columnspan=2)

        self.lblPassword2Signup = tk.Label(self.frameSignup, text="Conferma Password", font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))),bg=self.impostazioni_labels_bg_color, fg=self.impostazioni_labels_fg_color)
        self.lblPassword2Signup.grid(row=5, column=1, columnspan=2)

        self.password2Signup=tk.StringVar(self, "")
        self.enPassword2Signup = tk.Entry(self.frameSignup, textvariable=self.password2Signup, font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))),width=20, bg=self.impostazioni_labels_bg_color,fg=self.impostazioni_labels_fg_color, highlightthickness=0)
        self.enPassword2Signup.grid(row=6, column=1, columnspan=2)

        self.btnSignupSignup = tk.Button(self.frameSignup, text="Signup", width=7, command=lambda: self.checkSignup(), font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))),bg=self.impostazioni_options_bg_color, fg=self.impostazioni_options_fg_color, highlightthickness=0)
        self.btnSignupSignup.grid(row=7, column=2, pady=20)

        self.btnLoginSignup = tk.Button(self.frameSignup, text="Login", width=7, command=lambda: self.Login(), font=("Helvetica", int((self.altezza / 51) + (self.larghezza / 91))),bg=self.impostazioni_options_bg_color, fg=self.impostazioni_options_fg_color, highlightthickness=0)
        self.btnLoginSignup.grid(row=7, column=1)

        self.frameSignup.rowconfigure(1, weight=1)
        self.frameSignup.rowconfigure(3, weight=1)
        self.frameSignup.rowconfigure(5, weight=1)
        #self.frameSignup.rowconfigure(7, weight=1)

        self.frameSignup.grid(row=2, column=1, pady=20)


        #TODO*****************************************************************************************************************\
        # **********************************************  GIOCO CPU  *********************************************************\
        # *********************************************************************************************************************

        self.frameGiocoCPU = tk.Frame(self, bg=self.gioco_sfondo_bg_color)
        frameSchedine = tk.LabelFrame(self.frameGiocoCPU, text=" Schedine:", bg=self.gioco_sfondo_bg_color, fg=self.gioco_schedine_unset_fg_color)

        #margineAltoDx=tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color, width=14).grid(row=0, column=0)

        #tk.Label(self.frameGioco, text="", width=160, bg=self.gioco_sfondo_bg_color, font=("Helvetica", 11, "bold")).grid(row=0, column=0, columnspan=10, sticky="nesw")

        self.btnTornaAlMenuGiocoCPU=tk.Button(self.frameGiocoCPU, text="←", bg=self.gioco_sfondo_bg_color, fg=self.gioco_schedine_set_fg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), command=lambda:self.MenuSuono(), relief="solid", highlightthickness=0, bd=0)
        self.btnTornaAlMenuGiocoCPU.grid(row=0, column=0, columnspan=2, sticky="w")
        #self.update()
        #print("Altezza",btnTornaAlMenu.winfo_height())
        #print("larghezza", btnTornaAlMenu.winfo_width())
        #fakebtnTornaAlMenu = tk.Button(self.frameGioco, bg=self.gioco_sfondo_bg_color, highlightthickness=0, state=tk.DISABLED, relief=tk.FLAT, height=4, width=17).grid(row=1, column=9)



        #spazioTraTitoloESchedine=tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=2, column=0)

        frameLogs=tk.LabelFrame(self.frameGiocoCPU, text=" Logs:", bg=self.gioco_logs_bg_color, fg=self.gioco_titolo_fg_color)

        self.txtLogsCPU=tk.Text(frameLogs, width=45, height=6, font=("Helvetica", int((self.altezza/85) + (self.larghezza/151))), state=tk.DISABLED, bd=0, bg=self.gioco_logs_bg_color, fg=self.gioco_logs_fg_color)
        self.txtLogsCPU.insert(1.0, "")
        self.txtLogsCPU.grid()
        scrollTxtLogs=tk.Scrollbar(self.frameGiocoCPU, command=self.txtLogsCPU.xview())
        self.txtLogsCPU.configure(yscrollcommand=scrollTxtLogs.set)

        frameLogs.grid(row=2, column=2, sticky="n", pady=30)


        frameDestro=tk.Frame(self.frameGiocoCPU, bg=self.gioco_framedestro_bg_color)

        frameNomeGioc=tk.LabelFrame(frameDestro, text=" Nome:", bg=self.gioco_framedestro_bg_color, fg=self.gioco_titolo_fg_color)

        #frameNome=tk.LabelFrame(frameNomeGioc, text=" Nome:", bg=self.gioco_framedestro_bg_color, fg=self.gioco_titolo_fg_color)
        nick=str(self.nicknameCPU.get())
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

        self.btnAmboCPU=tk.Button(framePremiRimanenti, text="AMBO", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnAmboCPU.grid(row=1, column=1, pady=30, sticky="nesw")

        self.btnTernaCPU=tk.Button(framePremiRimanenti, text="TERNA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnTernaCPU.grid(row=1, column=3, pady=30, sticky="nesw")

        blank2=tk.Label(framePremiRimanenti, text="", width=2, bg=self.gioco_premi_bg_color).grid(row=2, column=2)

        self.btnQuaternaCPU=tk.Button(framePremiRimanenti, text="QUATERNA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnQuaternaCPU.grid(row=2, column=1, pady=30, sticky="nesw")

        self.btnCinquinaCPU=tk.Button(framePremiRimanenti, text="CINQUINA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/290))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnCinquinaCPU.grid(row=2, column=3, pady=30, sticky="nesw")

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
        self.arrTabelloneCPU=[]
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
            self.arrTabelloneCPU.append(lbl)
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

        self.btnTornaAlMenuGiocoGioc=tk.Button(self.frameGiocoGioc, text="←", bg=self.gioco_sfondo_bg_color, fg=self.gioco_schedine_set_fg_color, highlightthickness=0, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bd=0, command=lambda:self.MenuSuono(), relief="solid")
        self.btnTornaAlMenuGiocoGioc.grid(row=0, column=0, columnspan=2, sticky="w")
        #self.update()
        #print("Altezza",btnTornaAlMenu.winfo_height())
        #print("larghezza", btnTornaAlMenu.winfo_width())
        #fakebtnTornaAlMenu = tk.Button(self.frameGioco, bg=self.gioco_sfondo_bg_color, highlightthickness=0, state=tk.DISABLED, relief=tk.FLAT, height=4, width=17).grid(row=1, column=9)



        #spazioTraTitoloESchedine=tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=2, column=0)

        frameLogs=tk.LabelFrame(self.frameGiocoGioc, text=" Logs:", bg=self.gioco_logs_bg_color, fg=self.gioco_titolo_fg_color)

        self.txtLogsGioc=tk.Text(frameLogs, width=45, height=6, font=("Helvetica", int((self.altezza/85) + (self.larghezza/151))), state=tk.DISABLED, bd=0, bg=self.gioco_logs_bg_color, fg=self.gioco_logs_fg_color)
        self.txtLogsGioc.insert(1.0, "")
        self.txtLogsGioc.grid()
        scrollTxtLogs=tk.Scrollbar(self.frameGiocoGioc, command=self.txtLogsGioc.xview())
        self.txtLogsGioc.configure(yscrollcommand=scrollTxtLogs.set)

        frameLogs.grid(row=2, column=2, sticky="n", pady=30)


        self.btnPronto=tk.Button(self.frameGiocoGioc, text="pronto", font=("Helvetica", int((self.altezza/85) + (self.larghezza/151)), "bold"), fg="green", bg="red", command=lambda: self.setPronto())
        self.btnPronto.grid(row=1, column=1, sticky="n", pady=30 ) #sopra a tabellone
        #self.btnPronto.grid(row=2, column=1, sticky="s", pady=40 ) sotto a tabellone e nEstratto
        #self.btnPronto.grid(row=2, column=2, sticky="n")  #in mezzo alle schedine e logs


        frameDestro=tk.Frame(self.frameGiocoGioc, bg=self.gioco_framedestro_bg_color)

        frameNomeGioc=tk.LabelFrame(frameDestro, text=" Nome:", bg=self.gioco_framedestro_bg_color, fg=self.gioco_titolo_fg_color)

        #frameNome=tk.LabelFrame(frameNomeGioc, text=" Nome:", bg=self.gioco_framedestro_bg_color, fg=self.gioco_titolo_fg_color)
        nick=str(self.nicknameGioc.get())
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

        self.btnAmboGioc=tk.Button(framePremiRimanenti, text="AMBO", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnAmboGioc.grid(row=1, column=1, pady=30, sticky="nesw")

        self.btnTernaGioc=tk.Button(framePremiRimanenti, text="TERNA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnTernaGioc.grid(row=1, column=3, pady=30, sticky="nesw")

        blank2=tk.Label(framePremiRimanenti, text="", width=2, bg=self.gioco_premi_bg_color).grid(row=2, column=2)

        self.btnQuaternaGioc=tk.Button(framePremiRimanenti, text="QUATERNA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/280))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnQuaternaGioc.grid(row=2, column=1, pady=30, sticky="nesw")

        self.btnCinquinaGioc=tk.Button(framePremiRimanenti, text="CINQUINA", height=2, width=8, font=("Helvetica", int((self.altezza/160) + (self.larghezza/290))), bg=self.gioco_premi_btns_bg_color, fg=self.gioco_premi_btns_fg_color, disabledforeground=self.gioco_premi_btns_fg_color, state=tk.DISABLED)
        self.btnCinquinaGioc.grid(row=2, column=3, pady=30, sticky="nesw")

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
        self.arrTabelloneGioc=[]
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
            self.arrTabelloneGioc.append(lbl)
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
        self.titoloTipoGioco=tk.Label(self.frameTipoGioco, text="Modalita di Gioco", fg=self.pregioco_titolo_fg_color, bg=self.pregioco_titolo_bg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54)))).grid(row=1, column=1, sticky="nesw")

        spazioTraTitoloETop = tk.Label(self.frameTipoGioco, bg=self.pregioco_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=0, column=2) #20

        frameOpzioniTipoGioco=tk.Frame(self.frameTipoGioco, bg=self.pregioco_sfondo_bg_color)

        self.btnCpuTipoGioco=tk.Button(frameOpzioniTipoGioco, text="Contro CPU", command=lambda: self.PreGiocoCPUSuono(), font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, highlightthickness=0) #30
        self.btnCpuTipoGioco.grid(row=0, column=1, sticky="nesw")

        spazioTraRows=tk.Label(frameOpzioniTipoGioco, text=" ", height=2, bg=self.pregioco_sfondo_bg_color).grid(row=1, column=1)

        self.btnMultiplayerTipoGioco=tk.Button(frameOpzioniTipoGioco, text="Multiplayer Locale", command=lambda: self.PreGiocoGiocSuono(), width=15, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, highlightthickness=0) #15
        self.btnMultiplayerTipoGioco.grid(row=2, column=1, sticky="nesw")

        spazioTraRows = tk.Label(frameOpzioniTipoGioco, bg=self.pregioco_sfondo_bg_color, height=2, font=("Helvetica", int((self.altezza / 76) + (self.larghezza / 136)))).grid(row=3, column=1)  # 20

        self.btnAnnullaTipoGioco = tk.Button(frameOpzioniTipoGioco, text="Annulla", command=lambda: self.MenuSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0) #30
        self.btnAnnullaTipoGioco.grid(row=4, column=1)

        frameOpzioniTipoGioco.grid(row=2, column=1)


        self.frameTipoGioco.columnconfigure(1, weight=1)
        self.frameTipoGioco.rowconfigure(2, weight=1)

        #TODO*****************************************************************************************************************\
        # ********************************************  PRE GIOCO CPU  *******************************************************\
        # *********************************************************************************************************************
        self.framePreGiocoCPU=tk.Frame(self, bg=self.pregioco_sfondo_bg_color)

        spazioTraTitoloETop = tk.Label(self.framePreGiocoCPU, bg=self.pregioco_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=0, column=2) #20

        self.lblTitoloPreGiocoCPU = tk.Label(self.framePreGiocoCPU, text="Impostazioni Pre Gioco", fg=self.pregioco_titolo_fg_color, bg=self.pregioco_titolo_bg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54)))) #50
        self.lblTitoloPreGiocoCPU.grid(row=1, column=1, columnspan=3, sticky="nesw")

        spazioTraTitoloEScelte = tk.Label(self.framePreGiocoCPU, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_sfondo_bg_color).grid(row=2, column=2) #30



        self.frameOpzioniCPU=tk.Frame(self.framePreGiocoCPU, bg=self.pregioco_sfondo_bg_color)

        self.lblNickGiocatoreCPU=tk.Label(self.frameOpzioniCPU, text="Nickname", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_labels_bg_color, fg=self.pregioco_labels_fg_color) #30
        self.lblNickGiocatoreCPU.grid(row=0, column=1, columnspan=2, sticky="w")

        self.enNickGiocatoriCPU=tk.Entry(self.frameOpzioniCPU, textvariable=self.nicknameCPU, width=15, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182))), bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, highlightthickness=0) #15
        self.enNickGiocatoriCPU.grid(row=0, column=2, columnspan=2, sticky="e")

        spazioTraScelte = tk.Label(self.frameOpzioniCPU, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=1, column=2) #20

        self.lblNGiocatoriCPU = tk.Label(self.frameOpzioniCPU, text="N Giocatori", fg=self.pregioco_labels_fg_color, bg=self.pregioco_labels_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.lblNGiocatoriCPU.grid(row=2, column=1, columnspan=2, sticky="w")

        self.spnNGiocatoriCPU = tk.OptionMenu(self.frameOpzioniCPU, self.nGiocatoriCPU, "2","3","4","5","6","7","8","9","10")
        self.spnNGiocatoriCPU.configure(highlightthickness=0, bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), width=5) #20
        self.spnNGiocatoriCPU.grid(row=2, column=2, columnspan=2, sticky="e")

        spazioTraScelte1 = tk.Label(self.frameOpzioniCPU, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=3, column=2) #20

        self.lblNSchedineCPU = tk.Label(self.frameOpzioniCPU, text="N Schedine", fg=self.pregioco_labels_fg_color, bg=self.pregioco_labels_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.lblNSchedineCPU.grid(row=4, column=1, columnspan=2, sticky="w")

        self.spnNSchedineCPU = tk.OptionMenu(self.frameOpzioniCPU, self.nSchedineCPU, "1", "2", "3", "4", "5", "6")
        self.spnNSchedineCPU.configure(highlightthickness=0, bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), width=5) #20
        self.spnNSchedineCPU.grid(row=4, column=2, columnspan=2, sticky="e")

        spazioTraScelte2 = tk.Label(self.frameOpzioniCPU, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=5, column=2) #20

        self.btnAnnullaCPU = tk.Button(self.frameOpzioniCPU, text="Annulla", command=lambda: self.indietroPreGiocoCPUSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0) #30
        self.btnAnnullaCPU.grid(row=6, column=1)

        spazioTraColonne=tk.Label(self.frameOpzioniCPU, text=" ", width=15, bg=self.pregioco_sfondo_bg_color).grid(row=6, column=2)

        self.btnIniziaCPU = tk.Button(self.frameOpzioniCPU, text="Inizia", command=lambda: self.GiocaCPUSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0) #30
        self.btnIniziaCPU.grid(row=6, column=3)



        self.frameOpzioniCPU.grid(row=3, column=1)



        spazioTraScelteEBottom = tk.Label(self.framePreGiocoCPU, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_sfondo_bg_color).grid(row=4, column=1)

        self.framePreGiocoCPU.columnconfigure(1, weight=1)
        self.framePreGiocoCPU.rowconfigure(3, weight=1)


        #TODO*****************************************************************************************************************\
        # *****************************************  PRE GIOCO GIOCATORI  ****************************************************\
        # *********************************************************************************************************************
        self.framePreGiocoGioc=tk.Frame(self, bg=self.pregioco_sfondo_bg_color)

        spazioTraTitoloETop = tk.Label(self.framePreGiocoGioc, bg=self.pregioco_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=0, column=2) #20

        self.lblTitoloPreGiocoGioc = tk.Label(self.framePreGiocoGioc, text="Impostazioni Pre Gioco", fg=self.pregioco_titolo_fg_color, bg=self.pregioco_titolo_bg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54)))) #50
        self.lblTitoloPreGiocoGioc.grid(row=1, column=1, columnspan=3, sticky="nesw")

        spazioTraTitoloEScelte = tk.Label(self.framePreGiocoGioc, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_sfondo_bg_color).grid(row=2, column=2) #30



        self.frameOpzioniGioc=tk.Frame(self.framePreGiocoGioc, bg=self.pregioco_sfondo_bg_color)

        """self.lblNickGiocatoreGioc=tk.Label(frameOpzioni, text="Nickname", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_labels_bg_color, fg=self.pregioco_labels_fg_color) #30
        self.lblNickGiocatoreGioc.grid(row=0, column=1, columnspan=2, sticky="w")

        self.enNickGiocatoriGioc=tk.Entry(frameOpzioni, textvariable=self.nicknameGioc, width=15, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182))), bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color) #15
        self.enNickGiocatoriGioc.grid(row=0, column=2, columnspan=2, sticky="e")"""

        self.btnScegliNicks=tk.Button(self.frameOpzioniGioc, text="Scegli Nickname Giocatori", command=lambda: self.ScegliNicks(), fg=self.pregioco_labels_fg_color, bg=self.pregioco_labels_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0) #30
        self.btnScegliNicks.grid(row=0, column=1, columnspan=3, sticky="nesw")

        spazioTraScelte = tk.Label(self.frameOpzioniGioc, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=1, column=2) #20

        self.lblNGiocatoriGioc = tk.Label(self.frameOpzioniGioc, text="N Giocatori", fg=self.pregioco_labels_fg_color, bg=self.pregioco_labels_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.lblNGiocatoriGioc.grid(row=2, column=1, columnspan=2, sticky="w")

        self.spnNGiocatoriGioc = tk.OptionMenu(self.frameOpzioniGioc, self.nGiocatoriGioc, "2","3","4","5","6","7","8","9","10")
        self.spnNGiocatoriGioc.configure(highlightthickness=0, bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), width=5) #20
        self.spnNGiocatoriGioc.grid(row=2, column=2, columnspan=2, sticky="e")

        spazioTraScelte1 = tk.Label(self.frameOpzioniGioc, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=3, column=2) #20

        self.lblNSchedineGioc = tk.Label(self.frameOpzioniGioc, text="N Schedine", fg=self.pregioco_labels_fg_color, bg=self.pregioco_labels_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91)))) #30
        self.lblNSchedineGioc.grid(row=4, column=1, columnspan=2, sticky="w")

        self.spnNSchedineGioc = tk.OptionMenu(self.frameOpzioniGioc, self.nSchedineGioc, "1", "2", "3", "4", "5", "6")
        self.spnNSchedineGioc.configure(highlightthickness=0, bg=self.pregioco_options_bg_color, fg=self.pregioco_options_fg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), width=5) #20
        self.spnNSchedineGioc.grid(row=4, column=2, columnspan=2, sticky="e")

        spazioTraScelte2 = tk.Label(self.frameOpzioniGioc, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.pregioco_sfondo_bg_color).grid(row=5, column=2) #20

        self.btnAnnullaGioc = tk.Button(self.frameOpzioniGioc, text="Annulla", command=lambda: self.indietroPreGiocoGiocSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0) #30
        self.btnAnnullaGioc.grid(row=6, column=1)

        spazioTraColonne=tk.Label(self.frameOpzioniGioc, text=" ", width=15, bg=self.pregioco_sfondo_bg_color).grid(row=6, column=2)

        self.btnIniziaGioc = tk.Button(self.frameOpzioniGioc, text="Inizia", command=lambda: self.GiocaGiocSuono(), fg=self.pregioco_options_fg_color, bg=self.pregioco_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0) #30
        self.btnIniziaGioc.grid(row=6, column=3)



        self.frameOpzioniGioc.grid(row=3, column=1)



        spazioTraScelteEBottom = tk.Label(self.framePreGiocoGioc, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.pregioco_sfondo_bg_color).grid(row=4, column=1)

        self.framePreGiocoGioc.columnconfigure(1, weight=1)
        self.framePreGiocoGioc.rowconfigure(3, weight=1)

        # TODO*****************************************************************************************************************\
        #  *********************************************  SCEGLI NICK  ********************************************************\
        #  *********************************************************************************************************************
        self.frameScegliNicks=tk.Frame(self.framePreGiocoGioc, bg=self.gioco_sfondo_bg_color)


        self.btnTornaAlMenuScegliNick=tk.Button(self.frameScegliNicks, text="←", bg=self.gioco_sfondo_bg_color, fg=self.gioco_titolo_fg_color, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182))), bd=0,command=lambda: self.toPregiocoSuono(), relief="solid", highlightthickness=0)
        self.btnTornaAlMenuScegliNick.grid(row=0, column=0)

        self.lblTitoloScegliNick = tk.Label(self.frameScegliNicks, text="Scegli Nickname", font=("Helvetica", int((self.altezza/30) + (self.larghezza/54))), bg=self.gioco_titolo_bg_color, fg=self.gioco_titolo_fg_color)
        self.lblTitoloScegliNick.grid(row=1, column=1, columnspan=5, sticky="nesw")

        self.lblNomegiocSceglinick=tk.Label(self.frameScegliNicks, text="", bg=self.gioco_titolo_bg_color, fg=self.gioco_premi_titolo_fg_color, font=("Helvetica", int((self.altezza / 72) + (self.larghezza / 152)), "bold"))
        self.lblNomegiocSceglinick.grid(row=2, column=1, columnspan=5, sticky="nesw")

        self.lblAsSceglliNick=tk.Label(self.frameScegliNicks, text="as", bg=self.gioco_titolo_bg_color, fg=self.gioco_premi_titolo_fg_color, font=("Helvetica", int((self.altezza / 82) + (self.larghezza / 162)), "bold"))
        self.lblAsSceglliNick.grid(row=3, column=3)

        self.btnPrevNick=tk.Button(self.frameScegliNicks, text="<", highlightthickness=0, disabledforeground=self.gioco_titolo_bg_color, state=tk.DISABLED, bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color, font=("Helvetica", int((self.altezza / 102) + (self.larghezza / 182)), "bold"), command=lambda: self.switchNicknameSuono("<"))
        self.btnPrevNick.grid(row=4, column=1)

        self.currNick=tk.StringVar(self, "")
        self.enNomeSceglliNick=tk.Entry(self.frameScegliNicks, textvariable=self.currNick, width=15, font=("Helvetica", int((self.altezza/102) + (self.larghezza/182))), bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color, highlightthickness=0)
        self.enNomeSceglliNick.grid(row=4, column=2, columnspan=3, sticky="nesw")

        self.btnNextNick=tk.Button(self.frameScegliNicks, text=">", highlightthickness=0, disabledforeground=self.gioco_titolo_bg_color, bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color, font=("Helvetica", int((self.altezza / 102) + (self.larghezza / 182)), "bold"), command=lambda: self.switchNicknameSuono(">"))
        self.btnNextNick.grid(row=4, column=5)

        self.lblSpazio1=tk.Label(self.frameScegliNicks, text="", bg=self.gioco_sfondo_bg_color)
        self.lblSpazio1.grid(row=5, columns=3)

        self.btnProntoScegliNick=tk.Button(self.frameScegliNicks, text="Fatto", command=lambda:self.setProntoNicknames(), disabledforeground=self.gioco_schedine_unset_fg_color, bg=self.gioco_premi_titolo_fg_color, fg=self.gioco_schedine_unset_fg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0)
        self.btnProntoScegliNick.grid(row=6, column=2, sticky="nesw")

        self.btnSalvaScegliNick = tk.Button(self.frameScegliNicks, text="Salva", state=tk.DISABLED, command=lambda:self.SalvaNicknames(), highlightthickness=0, bg=self.gioco_premi_bg_color, relief=tk.FLAT, fg=self.gioco_schedine_unset_fg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))))
        self.btnSalvaScegliNick.grid(row=6, column=4, sticky="nesw")

        self.lblSpazio = tk.Label(self.frameScegliNicks, text="", width=2, bg=self.gioco_sfondo_bg_color)
        self.lblSpazio.grid(row=7, column=6)

        self.frameScegliNicks.grid(row=1, rowspan=3, column=1)



        #TODO*****************************************************************************************************************\
        # ********************************************  IMPOSTAZIONI  ********************************************************\
        # *********************************************************************************************************************

        self.frameImpostazioni=tk.Frame(self, bg=self.impostazioni_sfondo_bg_color)

        #margineAltoSx = tk.Label(self.frameImpostazioni, width="20", bg=self.impostazioni_sfondo_bg_color).grid(row=0, column=0)
        #margineAltoDx = tk.Label(self.frameImpostazioni, width="20", bg=self.impostazioni_sfondo_bg_color).grid(row=0, column=4)

        spazioTraTitoloETop = tk.Label(self.frameImpostazioni, bg=self.impostazioni_sfondo_bg_color, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136)))).grid(row=0, column=2)

        self.btnTornaAlMenuImpostazioni = tk.Button(self.frameImpostazioni, text="←", bg=self.impostazioni_sfondo_bg_color, fg=self.impostazioni_titolo_fg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bd=0, command=lambda:self.indietroSuono(), relief=tk.FLAT, highlightthickness=0)
        self.btnTornaAlMenuImpostazioni.grid(row=1, column=0)

        self.lblTitoloImpostazioni = tk.Label(self.frameImpostazioni, text="Impostazioni", fg=self.impostazioni_titolo_fg_color, bg=self.impostazioni_titolo_bg_color, font=('Helvetica', int((self.altezza/30) + (self.larghezza/54))))
        self.lblTitoloImpostazioni.grid(row=1, column=1, columnspan=3, sticky="nesw")

        spazioTraTitoloEScelte = tk.Label(self.frameImpostazioni, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), bg=self.impostazioni_sfondo_bg_color).grid(row=2, column=2)



        frameOpzioni=tk.Frame(self.frameImpostazioni, bg=self.impostazioni_sfondo_bg_color)


        frameTema=tk.Frame(frameOpzioni, bg=self.impostazioni_options_bg_color)

        self.lblTema = tk.Label(frameTema, text="Tema", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), fg=self.impostazioni_labels_fg_color, bg=self.impostazioni_labels_bg_color)
        self.lblTema.grid(row=0, column=0)

        spazioTraScelteTema=tk.Label(frameTema, text=" ", bg=self.impostazioni_sfondo_bg_color, width=28).grid(row=0, column=1, sticky="nesw")

        self.rbtnTema1 = tk.Radiobutton(frameTema, text="Colorato", variable=self.tema, command=lambda :self.playSuono(), selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Normale", bg=self.impostazioni_options_bg_color).grid(row=0, column=2)
        self.rbtnTema2 = tk.Radiobutton(frameTema, text="Scuro", variable=self.tema, command=lambda :self.playSuono(), selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Scuro", bg=self.impostazioni_options_bg_color).grid(row=0, column=3)

        frameTema.grid(row=0, column=1, sticky="nesw")


        spazioTraScelte1 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.impostazioni_sfondo_bg_color).grid(row=1, column=2)


        frameVolume=tk.Frame(frameOpzioni, bg=self.impostazioni_sfondo_bg_color)

        self.lblVolume=tk.Label(frameVolume, text="Volume", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), fg=self.impostazioni_labels_fg_color, bg=self.impostazioni_labels_bg_color)
        self.lblVolume.grid(row=0, column=0)


        spazioTraScelteVolume=tk.Label(frameVolume, text=" ", bg=self.impostazioni_sfondo_bg_color, width=20).grid(row=0, column=1, sticky="nesw")

        #scaleNViagg2=Scale(frameNViagg, from_=1, to=5, variable=nViagg, orient=HORIZONTAL, showvalue=0, length=125, bg="#00DF80", fg=formFgColor, highlightthickness=0, troughcolor=formBgColor, bd=1).grid(row=0, column=1, sticky="ns")
        self.sliderVolume=tk.Scale(frameVolume, from_=0, to=100, variable=self.volume, orient=tk.HORIZONTAL, showvalue=1, length=200, bg=self.impostazioni_options_bg_color, fg=self.impostazioni_options_fg_color, highlightthickness=0, troughcolor=self.impostazioni_options_bg_color, bd=1)
        self.sliderVolume.grid(row=0, column=2, sticky="w")

        frameVolume.grid(row=2, column=1, sticky="nesw")


        spazioTraScelte1 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.impostazioni_sfondo_bg_color).grid(row=3, column=2)


        frameTipoSchedine=tk.Frame(frameOpzioni, bg=self.impostazioni_options_bg_color)

        self.lblTipoSched = tk.Label(frameTipoSchedine, text="Schedina", font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), fg="gray", bg=self.impostazioni_labels_bg_color)
        self.lblTipoSched.grid(row=0, column=0)

        spazioTraScelteTema=tk.Label(frameTipoSchedine, text=" ", bg=self.impostazioni_sfondo_bg_color, width=15).grid(row=0, column=1, sticky="nesw")

        self.rbtnTpoSched1 = tk.Radiobutton(frameTipoSchedine, state=tk.DISABLED, text="Tombolone", command=lambda :self.playSuono(), variable=self.tipoSched, selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Tombolone", bg=self.impostazioni_options_bg_color).grid(row=0, column=2)
        self.rbtnTpoSched2 = tk.Radiobutton(frameTipoSchedine, state=tk.DISABLED, text="Classic", command=lambda :self.playSuono(), variable=self.tipoSched, selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Classic", bg=self.impostazioni_options_bg_color).grid(row=0, column=3)

        frameTipoSchedine.grid(row=4, column=1, sticky="nesw")


        spazioTraScelte2 = tk.Label(frameOpzioni, font=("Helvetica", int((self.altezza/76) + (self.larghezza/136))), bg=self.impostazioni_sfondo_bg_color).grid(row=5, column=2)


        self.btnSalva = tk.Button(frameOpzioni, text="Salva", command=lambda: self.salvaSuono(), fg=self.impostazioni_options_fg_color, bg=self.impostazioni_options_bg_color, font=("Helvetica", int((self.altezza/51) + (self.larghezza/91))), highlightthickness=0)
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



        # Giocatori
        for t in range(self.nGiocatoriGioc.get()):
            arrSchedine = self.creaSchedineGiocatoriGioc(t)
            giocatore = Giocatore(self.plyrNicks[t].getNome())
            giocatore.setSchedine(arrSchedine)
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
                giocatore = Giocatore(nome)
                giocatore.setSchedine(arrSchedine)
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

        #DEBUG
        # print("CounterFalse: " + str(countFalse) + "\nCounterTrue: " + str(countTrue) + "\nLen di GiocatoriCpu: " + str(len(self.giocatoriGioc)))

        if countFalse == len(self.giocatoriGioc):
            self.btnNEstrattoGioc.configure(state=tk.DISABLED)
            self.master.bind('<Button-3>', self.setPronto)
            self.master.bind('<Return>', self.setPronto)
            #DEBUG
            # print("sono nel falso")

        elif countTrue == len(self.giocatoriGioc):
            self.btnNEstrattoGioc.configure(state=tk.NORMAL)
            self.master.bind('<Button-3>', self.estraiGioc)
            self.master.bind('<Return>', self.estraiGioc)
            self.checkByVarsMulti()
            #DEBUG
            # print("Sono nel vero")

            #for i in range(len(self.giocatoriGioc)):
                #self.giocatoriGioc[i].setFlagPronto(False)
                #DEBUG
                # print("Flag di " + self.giocatoriCpu[i].getNome() + " settato")

    def estraiGiocSuono(self):
        self.playSuono()
        self.estraiGioc(event=None)

    def estraiGioc(self, event):
        self.btnPronto.configure(bg="red")
        self.verificaPronti()
        for i in range(len(self.giocatoriGioc)):
            self.giocatoriGioc[i].setFlagPronto(False)

        #Estrae i numeri casuali della partita
        randN = random.randint(1, 90)
        if self.nEstratti == []:
            self.lblNEstrattoGioc.configure(text=randN)
            self.nEstratti.append(randN)

            # Tabellone
            for i in range(len(self.arrTabelloneGioc)):
                if int(self.arrTabelloneGioc[i].cget("text")) == randN:
                    self.arrTabelloneGioc[i].configure(bg=self.gioco_tabellone_set_bg_color)
            # DEBUG  print("N Estratto: ", randN)

        elif self.nEstratti.count(randN) != 0:
            self.estraiGioc(event=None)
        else:
            self.lblNEstrattoGioc.configure(text=randN)
            self.nEstratti.append(randN)

            # Tabellone
            for i in range(len(self.arrTabelloneGioc)):
                if int(self.arrTabelloneGioc[i].cget("text")) == randN:
                    self.arrTabelloneGioc[i].configure(bg=self.gioco_tabellone_set_bg_color)

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
            for i in range(len(self.arrTabelloneCPU)):
                if int(self.arrTabelloneCPU[i].cget("text")) == randN:
                    self.arrTabelloneCPU[i].configure(bg=self.gioco_tabellone_set_bg_color)
            #DEBUG  print("N Estratto: ", randN)

        elif self.nEstratti.count(randN) != 0:
            self.estraiCPU(event=None)
        else:
            self.lblNEstrattoCPU.configure(text=randN)
            self.nEstratti.append(randN)

            # Tabellone
            for i in range(len(self.arrTabelloneCPU)):
                if int(self.arrTabelloneCPU[i].cget("text")) == randN:
                    self.arrTabelloneCPU[i].configure(bg=self.gioco_tabellone_set_bg_color)

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
        self.nicknameCPU = tk.StringVar(self, "GUEST")
        self.nicknameGioc = tk.StringVar(self, "Default Nick")
        self.nEstratti=[]
        self.currentPlayer=0
        self.currentNick=0
        self.plyrNicks=[]
        self.old_plyrNicks=[]
        self.giocatore=Giocatore(self.nicknameCPU.get())
        self.logged=False
        self.giocatoriCpu=[]
        self.giocatoriGioc=[]
        self.Utenti = []
        self.nGiocatoriGioc = tk.IntVar(self, 2)
        self.nGiocatoriCPU = tk.IntVar(self, 2)
        self.nSchedineGioc = tk.IntVar(self, 1)
        self.nSchedineCPU = tk.IntVar(self, 1)
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
        self.master.bind('<Left>', self.doNothing)
        self.master.bind('<Right>', self.doNothing)
        self.master.bind('<Button-3>', self.doNothing)
        self.master.bind('<Return>', self.doNothing)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Control-Tab>', self.revealKeyBindTipoGioco)
        self.master.bind('<Control-b>', self.PreGiocoGioc)
        self.master.bind('<Control-a>', self.PreGiocoCPU)
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
        self.master.bind('<Control-Down>', self.doNothing)
        self.master.bind('<Control-Up>', self.doNothing)
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

    def MenuSuono(self):
        self.playSuono()
        self.Menu(event=None)

    def Menu(self, event):
        self.playColSonMenu()
        # Porta in primo piano il Menu


        self.master.bind('Left', self.doNothing)
        self.master.bind('Right', self.doNothing)
        self.master.bind('<Control-a>', self.doNothing)
        self.master.bind('<Control-A>', self.doNothing)
        self.master.bind('<Control-b>', self.doNothing)
        self.master.bind('<Control-B>', self.doNothing)
        self.master.bind('<Control-c>', self.Punteggio)
        self.master.bind('<Control-p>', self.Login)
        self.master.bind('<Button-3>', self.doNothing)
        self.master.bind('<Control-Tab>', self.revealKeyBindMenu)
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
        if self.logged == True:
            self.master.bind('<Control-p>', self.esciAccount)
            self.btnLoginMenu.configure(text=self.giocatore.getNomeLogin()+"\n Ω x", command=lambda:self.esciAccount())
        self.frameLogin.grid_forget()
        self.frameSignup.grid_forget()
        #self.frameGioco.pack_forget()
        #self.frameImpostazioni.pack_forget()
        #self.frameMenu.pack(expand=True, anchor=tk.CENTER, side=tk.LEFT, fill=tk.BOTH)

    def GiocaGiocSuono(self):
        self.playSuono()
        self.GiocaGioc(event=None)

    def GiocaGioc(self, event):
        self.playColSonGioco()

        self.master.bind('<Return>', self.estraiGioc)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Left>', self.doNothing)
        self.master.bind('<Button-4>', self.doNothing)
        self.master.bind('<Control-a>', self.doNothing)
        self.master.bind('<Control-A>', self.doNothing)
        self.master.bind('<Control-b>', self.doNothing)
        self.master.bind('<Control-B>', self.doNothing)
        self.master.bind('<Control-c>', self.doNothing)
        self.master.bind('<Control-Tab>', self.revealKeyBindGioco)
        self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayerGioc(direction, event))
        self.master.bind('<Button-5>', lambda event=None, direction=">": self.switchPlayerGioc(direction, event))
        self.master.bind('<Button-3>', self.estraiGioc)
        self.master.bind('<Escape>', self.Menu)


        # Porta in primo piano la schermata del gioco
        self.CreateWidgets()


        self.currentPlayer=0
        self.nicknameGioc.set(self.currNick.get())
        #self.giocatore=Giocatore(self.nickname.get())
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
        self.master.bind('<Control-b>', self.downGiocatoriGioc)
        self.master.bind('<Control-B>', self.upGiocatoriGioc)
        self.master.bind('<Control-c>', self.downSchedineGioc)
        self.master.bind('<Control-C>', self.upSchedineGioc)
        self.master.bind('<Control-a>', self.ScegliNicks)
        self.master.bind('<Control-Tab>', self.revealKeyBindPreGioco)
        self.master.bind('<Escape>', self.indietroPreGiocoGioc)
        #self.master.bind('<Return>', self.GiocaGioc)

        self.punteggio = 0
        self.plyrNicks = []

        self.framePunteggio.grid_forget()
        self.frameMenu.grid_forget()
        self.framePreGiocoCPU.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.frameGiocoCPU.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameTipoGioco.grid_forget()
        self.framePreGiocoGioc.grid(row=0, column=0, sticky="nesw")
        self.frameScegliNicks.grid_forget()

        self.checkIfSettedNicks()

        self.oldNGiocatoriGioc = self.nGiocatoriGioc.get()
        self.oldNSchedineGioc = self.nSchedineGioc.get()

    def checkIfSettedNicks(self):
        if self.plyrNicks == []:
            self.btnIniziaGioc.configure(state=tk.DISABLED)
            self.master.bind("<Return>", self.doNothing)
        else:
            self.btnIniziaGioc.configure(state=tk.NORMAL)
            self.master.bind("<Return>", self.GiocaGioc)

    def GiocaCPUSuono(self):
        self.playSuono()
        self.GiocaCPU(event=None)

    def GiocaCPU(self, event):

        self.master.bind('<Return>', self.estraiCPU)
        self.master.bind('<Tab>', self.doNothing)
        self.master.bind('<Left>', self.doNothing)
        self.master.bind('<Button-4>', self.estraiCPU)
        self.master.bind('<Control-a>', self.doNothing)
        self.master.bind('<Control-A>', self.doNothing)
        self.master.bind('<Control-b>', self.doNothing)
        self.master.bind('<Control-B>', self.doNothing)
        self.master.bind('<Control-c>', self.doNothing)
        self.master.bind('<Control-Tab>', self.revealKeyBindGioco)
        self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayerCPU(direction, event))
        self.master.bind('<Button-5>', lambda event=None, direction=">": self.switchPlayerCPU(direction, event))
        self.master.bind('<Button-3>', self.estraiCPU)
        self.master.bind('<Escape>', self.Menu)


        # Porta in primo piano la schermata del gioco
        self.CreateWidgets()


        self.currentPlayer=0
        self.nicknameCPU.set(self.enNickGiocatoriCPU.get())
        #self.giocatore=Giocatore(self.nickname.get())
        self.giocatore.setNome(self.nicknameCPU.get())
        self.giocatore.setSchedine([])
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

        flagPlay=False
        crediti=self.giocatore.getCrediti()
        credit=crediti
        for i in range(self.nSchedineCPU.get()):
            if credit != 0:
                credit-=5
            else:
                flagPlay=True

        #self.master.configure(bg=self.gioco_sfondo_bg_color)

        self.currentWindow = "Gioco"

        self.framePunteggio.grid_forget()
        self.frameMenu.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.framePreGiocoGioc.grid_forget()
        self.frameGiocoGioc.grid_forget()
        self.frameTipoGioco.grid_forget()
        if flagPlay == False:
            self.playColSonGioco()
            self.giocatore.setCrediti(credit)
            self.aggiornaCreditiGiocatore(credit)
            self.framePreGiocoCPU.grid_forget()
            self.frameGiocoCPU.grid(row=0, column=0, sticky="nesw")
        else:
            print("Non hai abbastaza crediti")
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
        self.master.bind('<Control-a>', self.downGiocatoriCPU)
        self.master.bind('<Control-A>', self.upGiocatoriCPU)
        self.master.bind('<Control-b>', self.downSchedineCPU)
        self.master.bind('<Control-B>', self.upSchedineCPU)
        self.master.bind('<Control-c>', self.doNothing)
        self.master.bind('<Control-Tab>', self.revealKeyBindPreGioco)
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

        self.oldNicknameCPU = self.nicknameCPU.get()
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
            self.master.bind('<Button-4>', self.doNothing)
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayerCPU(direction, event))
            self.master.bind('<Button-5>', lambda event=None, direction=">": self.switchPlayerCPU(direction, event))
            self.btnPrevPlayerCPU.configure(state=tk.DISABLED)
            self.btnNextPlayerCPU.configure(state=tk.NORMAL)
            self.btnPrevPlayerCPU.configure(bg=self.gioco_framedestro_bg_color, relief=tk.FLAT)
            self.btnNextPlayerCPU.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)

            #self.btnPrevPlayer.grid_forget()
            #self.btnNextPlayer.grid(row=11, column=4)

        elif self.currentPlayer == len(self.giocatoriCpu)-1:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchPlayerCPU(direction, event))
            self.master.bind('<Button-4>', lambda event=None, direction="<": self.switchPlayerCPU(direction, event))
            self.master.bind('<Right>', self.doNothing)
            self.master.bind('<Button-5>', self.doNothing)
            self.btnPrevPlayerCPU.configure(state=tk.NORMAL)
            self.btnNextPlayerCPU.configure(state=tk.DISABLED)
            self.btnPrevPlayerCPU.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            self.btnNextPlayerCPU.configure(bg=self.gioco_framedestro_bg_color, relief=tk.FLAT)

            #self.btnPrevPlayer.grid(row=11, column=1)
            #self.btnNextPlayer.grid_forget()

        else:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchPlayerCPU(direction, event))
            self.master.bind('<Button-4>', lambda event=None, direction="<": self.switchPlayerCPU(direction, event))
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayerCPU(direction, event))
            self.master.bind('<Button-5>', lambda event=None, direction=">": self.switchPlayerCPU(direction, event))
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
                    if self.giocatoriCpu[self.currentPlayer].getNome() == self.nicknameCPU.get():
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
            self.master.bind('<Button-4>', self.doNothing)
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayerGioc(direction, event))
            self.master.bind('<Button-5>', lambda event=None, direction=">": self.switchPlayerGioc(direction, event))
            self.btnPrevPlayerGioc.configure(state=tk.DISABLED)
            self.btnNextPlayerGioc.configure(state=tk.NORMAL)
            self.btnPrevPlayerGioc.configure(bg=self.gioco_framedestro_bg_color, relief=tk.FLAT)
            self.btnNextPlayerGioc.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)

            #self.btnPrevPlayer.grid_forget()
            #self.btnNextPlayer.grid(row=11, column=4)

        elif self.currentPlayer == len(self.giocatoriGioc)-1:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchPlayerGioc(direction, event))
            self.master.bind('<Button-4>', lambda event=None, direction="<": self.switchPlayerGioc(direction, event))
            self.master.bind('<Right>', self.doNothing)
            self.master.bind('<Button-5>', self.doNothing)
            self.btnPrevPlayerGioc.configure(state=tk.NORMAL)
            self.btnNextPlayerGioc.configure(state=tk.DISABLED)
            self.btnPrevPlayerGioc.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            self.btnNextPlayerGioc.configure(bg=self.gioco_framedestro_bg_color, relief=tk.FLAT)

            #self.btnPrevPlayer.grid(row=11, column=1)
            #self.btnNextPlayer.grid_forget()

        else:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchPlayerGioc(direction, event))
            self.master.bind('<Button-4>', lambda event=None, direction="<": self.switchPlayerGioc(direction, event))
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchPlayerGioc(direction, event))
            self.master.bind('<Button-5>', lambda event=None, direction=">": self.switchPlayerGioc(direction, event))
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

    def riempiListaUtenti(self):
        self.Utenti=[]
        fileCredenziali=open(self.fileDirCredenziali, "r")
        persone=fileCredenziali.readlines(9000)
        if persone:
            for line in persone:
                if line != "\n":
                    #print(line)
                    listLine = line.split(",")
                    nome=listLine[0].split("=")[1]
                    password=listLine[2].split("=")[1]
                    nickname=listLine[1].split("=")[1]
                    crediti=listLine[3].split("=")[1]
                    gioc = Giocatore(str(nickname))
                    gioc.setCrediti(int(crediti))
                    gioc.setNomeLogin(str(nome))
                    gioc.setPassword(str(password))
                    self.Utenti.append(gioc)
                    #print(gioc.getNomeLogin() + " " + gioc.getPassword())
        fileCredenziali.close()

    def Login(self, event=None):
        self.master.bind("<Return>", self.checkLogin)
        self.master.bind('<Tab>', self.Signup)
        self.master.bind('<Control-Tab>', self.revealKeyBindLogin)
        self.master.bind("<Escape>", self.Menu)

        #self.lblTitoloMenu.grid_forget()
        self.frameBtns.grid_forget()
        self.frameSignup.grid_forget()
        self.frameLogin.grid(row=2, column=1, sticky="ns", pady=20)

    def esciAccount(self, event=None):
        self.nicknameCPU.set("GUEST")
        self.giocatore=Giocatore(self.nicknameCPU.get())
        self.giocatore.setSchedine([])
        self.logged=False
        self.Menu(event=None)

    def checkLogin(self, event=None):
        nome = self.nomeLogin.get()
        password = self.passwordLogin.get()
        flag=False
        if self.Utenti != []:
            for i in range(len(self.Utenti)):
                print("Nome: " + self.Utenti[i].getNomeLogin()+"/" +nome+ " Password: "+self.Utenti[i].getPassword()+"/"+password)
                if self.Utenti[i].getNomeLogin() == nome and self.Utenti[i].getPassword() == password:
                    self.nicknameCPU.set(self.Utenti[i].getNome())
                    self.giocatore.setNome(self.nicknameCPU.get())
                    self.giocatore.setNomeLogin(self.Utenti[i].getNomeLogin())
                    self.giocatore.setCrediti(self.Utenti[i].getCrediti())
                    flag=True
            if flag == False:
                print("Fai prima il signup")
            else:
                self.logged=True
                self.riempiListaUtenti()
                self.CreateWidgets()
                self.Menu(event=None)
        else:
            print("Lista Utenti Vuota")

    def Signup(self, event=None):
        self.master.bind("<Return>", self.checkSignup)
        self.master.bind('<Tab>', self.Login)
        self.master.bind('<Control-Tab>', self.revealKeyBindSignup)
        self.master.bind("<Escape>", self.Menu)

        #self.lblTitoloMenu.grid_forget()
        self.frameBtns.grid_forget()
        self.frameLogin.grid_forget()
        self.frameSignup.grid(row=2, column=1, sticky="ns", pady=20)

    def checkSignup(self, event=None):
        nome = self.nomeSignup.get()
        password1 = self.password1Signup.get()
        password2 = self.password2Signup.get()
        flag=False
        if self.Utenti != []:
            if nome != "" and password1 != "" and password2 != "":
                for i in range(len(self.Utenti)):
                    print("Nome: " + self.Utenti[i].getNomeLogin()+"/" +nome+ " Password: "+self.Utenti[i].getPassword()+"/"+password1)
                    if self.Utenti[i].getNomeLogin() == nome:
                        flag=True
                if flag == False:
                    if password1 == password2:
                        fileCredenziali = open(self.fileDirCredenziali, "a")
                        fileCredenziali.write("\nNome="+nome+",Nickname="+self.nicknameCPU.get()+",Password="+password1+",Crediti="+str(self.giocatore.getCrediti()))
                        fileCredenziali.close()
                        self.riempiListaUtenti()
                        self.CreateWidgets()
                        self.Menu(event=None)
                    else:
                        print("Le password non sono uguali")
                else:
                    print("Nome gia in uso")
            else:
                print("Non puoi lasciare campi vuoti")
        else:
            if nome != "" and password1 != "" and password2 != "":
                if password1 == password2:
                    fileCredenziali = open(self.fileDirCredenziali, "w")
                    fileCredenziali.write("Nome=" + nome + ",Nickname=" + self.nicknameCPU.get() + ",Password=" + password1 + ",Crediti=" + str(self.giocatore.getCrediti()))
                    fileCredenziali.close()
                    self.riempiListaUtenti()
                    self.CreateWidgets()
                    self.Menu(event=None)
                else:
                    print("Le password non sono uguali")
            else:
                print("Non puoi lasciare campi vuoti")

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
        self.master.bind('<Control-a>', self.switchTema)
        self.master.bind('<Control-A>', self.doNothing)
        self.master.bind('<Control-b>', self.abbassaVolume)
        self.master.bind('<Control-B>', self.alzaVolume)
        self.master.bind('<Control-c>', self.doNothing)
        self.master.bind('<Control-Tab>', self.revealKeyBindImpostazioni)
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
        self.nGiocatoriGioc.set(self.oldNGiocatoriGioc)
        self.nSchedineGioc.set(self.oldNSchedineGioc)

        self.Menu(event=None)

    def indietroPreGiocoCPUSuono(self):
        self.playSuono()
        self.indietroPreGiocoCPU(event=None)

    def indietroPreGiocoCPU(self, event):
        self.nicknameCPU.set(self.oldNicknameCPU)
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
            """#DEBUG
            print("You clicked:")
            print("\t Giocatore:"+self.giocatoriCpu[giocatore].getNome())
            print("\t nScheda:",nScheda)
            print("\t nRiga:",nRiga)
            print("\t nCella:", nCella)"""

        #self.checkByVars2(giocatore, nScheda, nRiga)

        """# Effettua i controlli per i premi
        counterPronto = 0
        for j in range(len(self.giocatoriGioc)):
            if self.giocatoriGioc[j].getFlagPronto():
                counterPronto+=1
        if counterPronto == len(self.giocatoriGioc):
            self.checkByVars2(giocatore, nScheda, nRiga)"""
        #self.verificaPronti()

        #FARE UN VERIFICAPRONTI NELLA CLICK DEI GIOC PASSANDOGLI GIOCATORE, NSCHED, NCELLA ECC.
            #self.checkByVarsMulti()

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

        self.txtLogsCPU.config(state=tk.NORMAL)

        counter=0
        # celle
        for y in range(len(self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga])):
            if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][y][1] == "set":
                for i in range(len(self.arrTabelloneCPU)):
                    if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][y][0] != " ":
                        if self.arrTabelloneCPU[i].cget("bg") == self.gioco_tabellone_set_bg_color  and  int(self.arrTabelloneCPU[i].cget("text")) == int(self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][y][0]):
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
            self.updateClassProvCPU()
            if self.giocatoriCpu[giocatore].getNome() == self.giocatore.getNome():
                self.giocatore.setCrediti(self.giocatore.getCrediti()+4)
                self.aggiornaCreditiGiocatore(self.giocatore.getCrediti())
            print(self.giocatoriCpu[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda+1))
            self.btnAmboCPU.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogsCPU.insert(tk.END, self.giocatoriCpu[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda+1) + " (2 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Ambo sulla scheda N." + str(nScheda + 1))
        elif counter==3 and self.terna is False:
            self.terna = True
            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+3)
            self.updateClassProvCPU()
            if self.giocatoriCpu[giocatore].getNome() == self.giocatore.getNome():
                self.giocatore.setCrediti(self.giocatore.getCrediti()+6)
                self.aggiornaCreditiGiocatore(self.giocatore.getCrediti())
            print(self.giocatoriCpu[giocatore].getNome() + " ha fatto TERNA sulla scheda N.", nScheda+1)
            self.btnTernaCPU.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogsCPU.insert(tk.END, "\n" + self.giocatoriCpu[giocatore].getNome() + " ha fatto TERNA sulla scheda N."+ str(nScheda+1) + " (3 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Terna sulla scheda N." + str(nScheda + 1))
        elif counter==4 and self.quaterna is False:
            self.quaterna = True
            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+4)
            self.updateClassProvCPU()
            if self.giocatoriCpu[giocatore].getNome() == self.giocatore.getNome():
                self.giocatore.setCrediti(self.giocatore.getCrediti()+8)
                self.aggiornaCreditiGiocatore(self.giocatore.getCrediti())
            print(self.giocatoriCpu[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N."+ str(nScheda+1))
            self.btnQuaternaCPU.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogsCPU.insert(tk.END, "\n" + self.giocatoriCpu[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N."+ str(nScheda+1) + " (4 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Quaterna sulla scheda N." + str(nScheda + 1))
        elif counter==5 and self.cinquina is False:
            self.cinquina = True
            self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+5)
            self.updateClassProvCPU()
            if self.giocatoriCpu[giocatore].getNome() == self.giocatore.getNome():
                self.giocatore.setCrediti(self.giocatore.getCrediti()+10)
                self.aggiornaCreditiGiocatore(self.giocatore.getCrediti())
            print(self.giocatoriCpu[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N."+ str(nScheda+1))
            self.btnCinquinaCPU.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogsCPU.insert(tk.END, "\n" + self.giocatoriCpu[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N."+ str(nScheda+1) + " (5 pt)")
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
                self.txtLogsCPU.insert(tk.END, "\n HAI FATTO TOMBOLA sulla scheda N." + str(nScheda+1) + " con " + str(self.giocatoriCpu[giocatore].getPunteggioCorrente()) + " punti!")
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
        for y in range(len(self.arrTabelloneCPU)):
            if self.arrTabelloneCPU[y].cget("bg") == self.gioco_tabellone_set_bg_color:
                counterCroupier += 1
        # DEBUG  print("Counter Croupier: ",counter)
        # DEBUG  print("N Estratto: ", randN)

        """if counterCroupier == 90:
            loseByCroupier += 1
            if loseByCroupier == 1:
                self.after(10000, lambda:self.faVincereIlCroupier())"""

        self.txtLogsCPU.config(state=tk.DISABLED)

    """def checkByVars2(self, giocatore, nScheda, nRiga):
        # Controllo chi ha vinto il premio e lo stampo

        #DEBUG
        """"""print("Giocatore CheckByVars: " + str(giocatore))
        print("NScheda CheckByVars: " + str(nScheda))
        print("NRiga CheckByVars: " + str(nRiga))
        print("------------------------------------------------------")""""""

        self.txtLogsGioc.config(state=tk.NORMAL)

        counter=0
        # celle
        for y in range(len(self.giocatoriGioc[giocatore].getSchedine()[nScheda][nRiga])):
            if self.giocatoriGioc[giocatore].getSchedine()[nScheda][nRiga][y][1] == "set":
                for i in range(len(self.arrTabelloneGioc)):
                    if self.giocatoriGioc[giocatore].getSchedine()[nScheda][nRiga][y][0] != " ":
                        if self.arrTabelloneGioc[i].cget("bg") == self.gioco_tabellone_set_bg_color  and  int(self.arrTabelloneGioc[i].cget("text")) == int(self.giocatoriGioc[giocatore].getSchedine()[nScheda][nRiga][y][0]):
                            counter+=1

        if counter==2 and self.ambo is False:
            self.ambo=True
            self.giocatoriGioc[giocatore].setPunteggioCorrente(self.giocatoriGioc[giocatore].getPunteggioCorrente()+2)
            self.updateClassProvGioc()
            print(self.giocatoriGioc[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda+1))
            self.btnAmboGioc.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogsGioc.insert(tk.END, self.giocatoriGioc[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda+1) + " (2 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Ambo sulla scheda N." + str(nScheda + 1))
        elif counter==3 and self.terna is False:
            self.terna = True
            self.giocatoriGioc[giocatore].setPunteggioCorrente(self.giocatoriGioc[giocatore].getPunteggioCorrente()+3)
            self.updateClassProvGioc()
            print(self.giocatoriCpu[giocatore].getNome() + " ha fatto TERNA sulla scheda N.", nScheda+1)
            self.btnTernaGioc.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogsGioc.insert(tk.END, "\n" + self.giocatoriGioc[giocatore].getNome() + " ha fatto TERNA sulla scheda N."+ str(nScheda+1) + " (3 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Terna sulla scheda N." + str(nScheda + 1))
        elif counter==4 and self.quaterna is False:
            self.quaterna = True
            self.giocatoriGioc[giocatore].setPunteggioCorrente(self.giocatoriGioc[giocatore].getPunteggioCorrente()+4)
            self.updateClassProvGioc()
            print(self.giocatoriGioc[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N."+ str(nScheda+1))
            self.btnQuaternaGioc.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogsGioc.insert(tk.END, "\n" + self.giocatoriGioc[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N."+ str(nScheda+1) + " (4 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Quaterna sulla scheda N." + str(nScheda + 1))
        elif counter==5 and self.cinquina is False:
            self.cinquina = True
            self.giocatoriGioc[giocatore].setPunteggioCorrente(self.giocatoriGioc[giocatore].getPunteggioCorrente()+5)
            self.updateClassProvGioc()
            print(self.giocatoriGioc[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N."+ str(nScheda+1))
            self.btnCinquinaGioc.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
            self.txtLogsGioc.insert(tk.END, "\n" + self.giocatoriGioc[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N."+ str(nScheda+1) + " (5 pt)")
            #messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Cinquina sulla scheda N." + str(nScheda + 1))



        counterWin1 = 0
        self.previousWinner = ""
        for y in range(len(self.giocatoriGioc[giocatore].getSchedine()[nScheda])):
            for h in range(len(self.giocatoriGioc[giocatore].getSchedine()[nScheda][y])):
                if self.giocatoriGioc[giocatore].getSchedine()[nScheda][y][h][1] == "set":
                    counterWin1 += 1

        if counterWin1 == 15 and self.tombola is False:
            #if self.giocatoriCpu[giocatore].getNome() == self.nickname.get():
            if self.verificaValiditaPremi2(giocatore) == True:
                self.tombola = True
                print("HAI VINTOOOOOOOOO!!! Con ",self.giocatoriCpu[giocatore].getPunteggioCorrente(), " punti!")
                self.txtLogsCPU.insert(tk.END, "\n HAI FATTO TOMBOLA sulla scheda N." + str(nScheda+1) + " con " + str(self.giocatoriCpu[giocatore].getPunteggioCorrente()) + " punti!")
                #messagebox.showinfo("GRANDE!!   HAI VINTO!!!", "HAI FATTO TOMBOLA sulla scheda N."+ str(nScheda+1) +" \n con punteggio di "+str(self.giocatoriCpu[giocatore].getPunteggioCorrente())+"!!!")
                #self.previousWinner = self.giocatoriCpu[giocatore].getNome()
                self.showClassifica()
            elif self.verificaValiditaPremi2(giocatore) == False:
                print("Non hai vinto perche' hai barato!")
                messagebox.showerror("Non si puo fare >:(", "LA SCHEDINA N. " + str(nScheda+1) + " NON E' VALIDA!!!")

        self.txtLogsGioc.config(state=tk.DISABLED)"""

    def checkByVarsMulti(self):

        giocatore=0
        nScheda=0
        nRiga=0
        cella=0
        #counter=[["", 0]]
        counter=0
        #counterRiga=0

        self.txtLogsGioc.config(state=tk.NORMAL)

        """for nScheda in range(self.nSchedineGioc.get()):
            for nRiga in range(3):
                counter=0"""
        for giocatore in range(len(self.giocatoriGioc)):
            for nScheda in range(len(self.giocatoriGioc[giocatore].getSchedine())):
                for nRiga in range(len(self.giocatoriGioc[giocatore].getSchedine()[nScheda])):
                    counter=0
                    for cella in range(len(self.giocatoriGioc[giocatore].getSchedine()[nScheda][nRiga])):
                        if self.giocatoriGioc[giocatore].getSchedine()[nScheda][nRiga][cella][1] == "set":
                            for i in range(len(self.arrTabelloneGioc)):
                                if self.giocatoriGioc[giocatore].getSchedine()[nScheda][nRiga][cella][0] != " ":
                                    #counterRiga += 1
                                    """"#DEBUG
                                    print("Giocatore: ",giocatore,"\n NScheda: ",nScheda,"\n NRiga: ", nRiga, "\n NCella: ",cella,"\n\n")
                                    print("Num Tabellone: ", self.arrTabelloneGioc[i].cget("text"), "\n Num Cella: ", self.giocatoriGioc[giocatore].getSchedine()[nScheda][nRiga][cella][0], "\n\n")"""
                                    if self.arrTabelloneGioc[i].cget("bg") == self.gioco_tabellone_set_bg_color and int(self.arrTabelloneGioc[i].cget("text")) == int(self.giocatoriGioc[giocatore].getSchedine()[nScheda][nRiga][cella][0]):
                                        #counter.append([self.giocatoriCpu[giocatore]])
                                        counter += 1
                                        #if counterRiga == 5:
                                        #    counterRiga=0
                                        #    counter=0
                        #if self.giocatoriCpu[giocatore].getNome() == self.nickname.get():
                        if counter == 2 and self.giocatoriGioc[giocatore].getAmbo() is False:
                            self.giocatoriGioc[giocatore].setAmbo(True)
                            self.giocatoriGioc[giocatore].setPunteggioCorrente(self.giocatoriGioc[giocatore].getPunteggioCorrente() + 2)
                            self.updateClassProvGioc()
                            print(self.giocatoriGioc[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda + 1))
                            self.btnAmboGioc.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
                            self.txtLogsGioc.insert(tk.END, self.giocatoriGioc[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda + 1) + " (2 pt)\n")

                            #print("Hai fatto AMBO sulla scheda N." + str(nScheda + 1), " e hai gudagnato 2 punti")
                            #messagebox.showinfo("CONGRATULAZIONI " + self.giocatoriCpu[giocatore].getNome() + "!!","Hai fatto AMBO sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 2 punti")
                        elif counter == 3 and self.giocatoriGioc[giocatore].getTerna() is False:
                            self.giocatoriGioc[giocatore].setTerna(True)
                            self.giocatoriGioc[giocatore].setPunteggioCorrente(self.giocatoriGioc[giocatore].getPunteggioCorrente() + 3)
                            self.updateClassProvGioc()
                            print(self.giocatoriGioc[giocatore].getNome() + " ha fatto TERNA sulla scheda N.",nScheda + 1)
                            self.btnTernaGioc.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
                            self.txtLogsGioc.insert(tk.END, "\n" + self.giocatoriGioc[giocatore].getNome() + " ha fatto TERNA sulla scheda N." + str(nScheda + 1) + " (3 pt)\n")
                            #print("Hai fatto TERNA sulla scheda N.", nScheda + 1, " e hai gudagnato 3 punti")
                            #messagebox.showinfo("CONGRATULAZIONI " + self.giocatoriCpu[giocatore].getNome() + "!!","Hai fatto TERNA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 3 punti")
                        elif counter == 4 and self.giocatoriGioc[giocatore].getQuaterna() is False:
                            self.giocatoriGioc[giocatore].setQuaterna(True)
                            self.giocatoriGioc[giocatore].setPunteggioCorrente(self.giocatoriGioc[giocatore].getPunteggioCorrente() + 4)
                            self.updateClassProvGioc()
                            print(self.giocatoriGioc[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N." + str(nScheda + 1))
                            self.btnQuaternaGioc.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
                            self.txtLogsGioc.insert(tk.END, "\n" + self.giocatoriGioc[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N." + str(nScheda + 1) + " (4 pt)\n")
                            #print("Hai fatto QUATERNA sulla scheda N.", nScheda + 1, " e hai gudagnato 4 punti")
                            #messagebox.showinfo("CONGRATULAZIONI " + self.giocatoriCpu[giocatore].getNome() + "!!","Hai fatto QUATERNA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 4 punti")
                        elif counter == 5 and self.giocatoriGioc[giocatore].getCinquina() is False:
                            self.giocatoriGioc[giocatore].setCinquina(True)
                            self.giocatoriGioc[giocatore].setPunteggioCorrente(self.giocatoriGioc[giocatore].getPunteggioCorrente() + 5)
                            self.updateClassProvGioc()
                            print(self.giocatoriGioc[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N." + str(nScheda + 1))
                            self.btnCinquinaGioc.configure(relief=tk.FLAT, bg=self.gioco_premi_bg_color)
                            self.txtLogsGioc.insert(tk.END, "\n" + self.giocatoriGioc[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N." + str(nScheda + 1) + " (5 pt)\n")
                            #print("Hai fatto CINQUINA sulla scheda N.", nScheda + 1, " e hai gudagnato 5 punti")
                            #messagebox.showinfo("CONGRATULAZIONI " + self.giocatoriCpu[giocatore].getNome() + "!!","Hai fatto CINQUINA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 5 punti")
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

        self.txtLogsGioc.config(state=tk.DISABLED)

    def aggiornaCreditiGiocatore(self, crediti):
        file = ""
        fileCredenziali=open(self.fileDirCredenziali, "r")
        lines=fileCredenziali.readlines(90000)
        for line in lines:
            if line != "\n":
                linea=line.split(",")
                nome=linea[0].split("=")[1]
                print("COSSE: "+file+"-"+nome)
                print("Nome file:" + nome+"- Nome Gioc: " + self.giocatore.getNomeLogin())
                if self.giocatore.getNomeLogin() == nome:
                    linNick1=line.split("Nickname=")[0]
                    linNick2=line.split("Nickname=")[1].split(",")
                    linNick3=linNick2[1]+linNick2[2]
                    linCred1=linNick3.split("Crediti=")[0]
                    #print("Lin: "+lin)
                    #lin=linea[0]+","+linea[1]+","+linea[2]+",Crediti="+crediti
                    #file = file+lin2+lin+"="+str(self.giocatore.getCrediti())+"\n"
                    file = file+linNick1+"Nickname="+self.giocatore.getNome()+","+linCred1+",Crediti="+str(self.giocatore.getCrediti())
                    print("File True: "+file)
                else:
                    file = file + line
                    print("File False: "+file)
        fileCredenziali.close()
        self.writetofilecrediti(file)

    def writetofilecrediti(self, string):
        fileCredenziali1 = open(self.fileDirCredenziali, "w")
        #print("Sto per scrivere...")
        fileCredenziali1.write(string)
        #print("Ho scritto " + string)
        fileCredenziali1.close()

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
                    if self.giocatoriCpu[giocatore].getSchedine()[i][l][y][1] == "set"   and   self.arrTabelloneCPU[y].cget("bg") == self.gioco_tabellone_set_bg_color:
                        counterInTabellone += 1
        # DEBUG
        print("CounterInTabellone: ", counterInTabellone)

        if counterCellePlayer == counterInTabellone:
            return True
        else:
            return False

    """def verificaValiditaPremi2(self, giocatore):
        # Controllo se il giocatore ha veramente
        # fatto tombola giocando o se ha selezionato
        # tutte le celle prima che venissero estratti

        counterCellePlayer=0
        #schedine
        for i in range(len(self.giocatoriGioc[giocatore].getSchedine())):
            #righe
            for l in range(len(self.giocatoriGioc[giocatore].getSchedine()[i])):
                #celle
                for y in range(len(self.giocatoriGioc[giocatore].getSchedine()[i][l])):
                    if self.giocatoriGioc[giocatore].getSchedine()[i][l][y][1] == "set":
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
                    if self.giocatoriCpu[giocatore].getSchedine()[i][l][y][1] == "set"   and   self.arrTabelloneGioc[y].cget("bg") == self.gioco_tabellone_set_bg_color:
                        counterInTabellone += 1
        # DEBUG
        print("CounterInTabellone: ", counterInTabellone)

        if counterCellePlayer == counterInTabellone:
            return True
        else:
            return False"""

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
        self.TipoGioco(event=None)
        self.Classifica.destroy()

    def goToMenuClassifica(self):
        self.playSuono()
        #pygame.mixer.music.pause()
        #pygame.mixer.music.load(self.currentDirectory + "/Files/Musica/ColonneSonore/Shake.ogg")
        #pygame.mixer.music.play(-1)
        self.Menu(event=None)
        self.Classifica.destroy()

    def playColSonMenu(self):
        pygame.mixer.music.pause()
        pygame.mixer.music.load(self.currentDirectory + "/Files/Musica/ColonneSonore/Shake.ogg")
        pygame.mixer.music.play(-1)
        #pass

    def playColSonGioco(self):
        pygame.mixer.music.pause()
        pygame.mixer.music.load(self.currentDirectory + "/Files/Musica/ColonneSonore/Gaiety.ogg")
        pygame.mixer.music.play(-1)
        #pass

    def updateVolumeMusica(self):
        pygame.mixer.music.set_volume(self.volume.get()/100)
        #pass

    def alzaVolume(self, event):
        self.volume.set(self.volume.get()+1)
        self.updateVolumeMusica()
        #pass

    def abbassaVolume(self, event):
        self.volume.set(self.volume.get()-1)
        self.updateVolumeMusica()
        #pass

    def playSuono(self):
        pygame.mixer.Sound.play(self.clickSound)
        #pass

    def switchTema(self, event):
        if self.tema.get() == "Scuro":
            self.tema.set("Normale")
        else:
            self.tema.set("Scuro")

    def upGiocatoriCPU(self, event):
        if self.nGiocatoriCPU.get() != 10:
            self.nGiocatoriCPU.set(self.nGiocatoriCPU.get() + 1)

    def downGiocatoriCPU(self, event):
        if self.nGiocatoriCPU.get() != 2:
            self.nGiocatoriCPU.set(self.nGiocatoriCPU.get() - 1)

    def upGiocatoriGioc(self, event):
        if self.nGiocatoriCPU.get() != 10:
            self.nGiocatoriGioc.set(self.nGiocatoriGioc.get() + 1)

    def downGiocatoriGioc(self, event):
        if self.nGiocatoriGioc.get() != 2:
            self.nGiocatoriGioc.set(self.nGiocatoriGioc.get() - 1)

    def upSchedineCPU(self, event):
        if self.nSchedineCPU.get() != 6:
            self.nSchedineCPU.set(self.nSchedineCPU.get() + 1)

    def downSchedineCPU(self, event):
        if self.nSchedineCPU.get() != 1:
            self.nSchedineCPU.set(self.nSchedineCPU.get() - 1)

    def upSchedineGioc(self, event):
        if self.nSchedineGioc.get() != 6:
            self.nSchedineGioc.set(self.nSchedineGioc.get() + 1)

    def downSchedineGioc(self, event):
        if self.nSchedineGioc.get() != 1:
            self.nSchedineGioc.set(self.nSchedineGioc.get() - 1)

    def revealKeyBindMenu(self, event):
        if self.btnEsci.cget("text") == "Esci":
            self.btnEsci.configure(text="'Esc'")
            self.btnGioca.configure(text="'Invio'")
            self.btnImpostazioni.configure(text="'Tab'")
            self.btnLoginMenu.configure(text="'Control'+'p'")
            self.btnClassificaPersonale.configure(text="'Control'+'c'")
        else:
            self.btnEsci.configure(text="Esci")
            self.btnGioca.configure(text="Gioca")
            self.btnImpostazioni.configure(text="Impostazioni")
            if self.logged == True:
                self.btnLoginMenu.configure(text=self.giocatore.getNomeLogin()+"\n Ω x")
            else:
                self.btnLoginMenu.configure(text="Login")
            self.btnClassificaPersonale.configure(text="{}")

    def revealKeyBindImpostazioni(self, event):
        if self.btnTornaAlMenuImpostazioni.cget("text") == "←":
            self.btnTornaAlMenuImpostazioni.configure(text="'Esc'")
            self.lblTema.configure(text="'Control'+'A'")
            self.lblVolume.configure(text="'Control'+'B' e\n'Control'+'Shift'+'B'")
            self.lblTipoSched.configure(text="'Control'+'C'")
            self.btnSalva.configure(text="'Invio'")
        else:
            self.btnTornaAlMenuImpostazioni.configure(text="←")
            self.lblTema.configure(text="Tema")
            self.lblVolume.configure(text="Volume")
            self.lblTipoSched.configure(text="Schedina")
            self.btnSalva.configure(text="Salva")

    def revealKeyBindTipoGioco(self, event):
        if self.btnAnnullaTipoGioco.cget("text") == "Annulla":
            self.btnMultiplayerTipoGioco.configure(text="'Control'+'B'")
            self.btnCpuTipoGioco.configure(text="'Control'+'A'")
            self.btnAnnullaTipoGioco.configure(text="'Esc'")
        else:
            self.btnMultiplayerTipoGioco.configure(text="Mutliplayer Locale")
            self.btnCpuTipoGioco.configure(text="Contro CPU")
            self.btnAnnullaTipoGioco.configure(text="Annulla")

    def revealKeyBindPreGioco(self, event):
        if self.btnAnnullaCPU.cget("text") == "Annulla" or self.btnAnnullaGioc.cget("text") == "Annulla":
            self.btnAnnullaCPU.configure(text="'Esc'")
            self.btnAnnullaGioc.configure(text="'Esc'")
            self.btnIniziaCPU.configure(text="'Invio")
            self.btnIniziaGioc.configure(text="'Invio'")
            self.lblNickGiocatoreCPU.configure(text="Nickname")
            self.btnScegliNicks.configure(text="'Control'+'A'")
            self.lblNGiocatoriCPU.configure(text="'Control'+'A' e \n'Control'+'Shift'+'A'")
            self.lblNGiocatoriGioc.configure(text="'Control'+'B' e \n'Control'+'Shift'+'B'")
            self.lblNSchedineCPU.configure(text="'Control'+'B' e \n'Control'+'Shift'+'B'")
            self.lblNSchedineGioc.configure(text="'Control'+'C' e \n'Control'+'Shift'+'C'")
        else:
            self.btnAnnullaCPU.configure(text="Annulla")
            self.btnAnnullaGioc.configure(text="Annulla")
            self.btnIniziaCPU.configure(text="Inizia")
            self.btnIniziaGioc.configure(text="Inizia")
            self.lblNickGiocatoreCPU.configure(text="Nickname")
            self.btnScegliNicks.configure(text="Scegli Nickname Giocatori")
            self.lblNGiocatoriCPU.configure(text="N Giocatori")
            self.lblNGiocatoriGioc.configure(text="N Giocatori")
            self.lblNSchedineCPU.configure(text="N Schedine")
            self.lblNSchedineGioc.configure(text="N Schedine")

    def revealKeyBindGioco(self, event):
        if self.btnTornaAlMenuGiocoCPU.cget("text") == "←":
            self.btnTornaAlMenuGiocoCPU.configure(text="'Esc'")
            self.btnTornaAlMenuGiocoGioc.configure(text="'Esc'")
            self.btnNEstrattoCPU.configure(text="'Mouse Destro'\n o 'Invio'")
            self.btnNEstrattoGioc.configure(text="'Mouse Destro'\n o 'Invio'")
            self.btnPronto.configure(text="'Mouse Destro'\n o 'Invio'")
            self.btnNextPlayerCPU.configure(text="'→'")
            self.btnNextPlayerGioc.configure(text="'→'")
            self.btnPrevPlayerCPU.configure(text="'←'")
            self.btnPrevPlayerGioc.configure(text="'←'")
        else:
            self.btnTornaAlMenuGiocoCPU.configure(text="←")
            self.btnTornaAlMenuGiocoGioc.configure(text="←")
            self.btnNEstrattoCPU.configure(text="Estrai")
            self.btnNEstrattoGioc.configure(text="Estrai")
            self.btnPronto.configure(text="Pronto")
            self.btnNextPlayerCPU.configure(text=">")
            self.btnNextPlayerGioc.configure(text=">")
            self.btnPrevPlayerCPU.configure(text="<")
            self.btnPrevPlayerGioc.configure(text="<")

    def revealKeyBindLogin(self, event=None):
        if self.btnLoginLogin.cget("text") == "Login":
            self.btnLoginLogin.configure(text="'Invio'")
            self.btnSignupLogin.configure(text="'Tab'")
            self.btnTornaAlMenuLogin.configure(text="'Esc'")
        else:
            self.btnLoginLogin.configure(text="Login")
            self.btnSignupLogin.configure(text="Signup")
            self.btnTornaAlMenuLogin.configure(text="←")

    def revealKeyBindSignup(self, event=None):
        if self.btnSignupSignup.cget("text") == "Signup":
            self.btnLoginSignup.configure(text="'Tab'")
            self.btnSignupSignup.configure(text="'Invio'")
            self.btnTornaAlMenuSignup.configure(text="'Esc'")
        else:
            self.btnLoginSignup.configure(text="Login")
            self.btnSignupSignup.configure(text="Signup")
            self.btnTornaAlMenuSignup.configure(text="←")

    def revealKeyBindSceglinicks(self, event=None):
        if self.btnTornaAlMenuScegliNick.cget("text") == "←":
            self.btnTornaAlMenuScegliNick.configure(text="'Esc'")
            self.btnPrevNick.configure(text="'←'")
            self.btnNextNick.configure(text="'→'")
            self.btnProntoScegliNick.configure(text="'Invio'")
            self.btnSalvaScegliNick.configure(text="'Invio'")
        else:
            self.btnTornaAlMenuScegliNick.configure(text="←")
            self.btnPrevNick.configure(text="<")
            self.btnNextNick.configure(text=">")
            self.btnProntoScegliNick.configure(text="Fatto")
            self.btnSalvaScegliNick.configure(text="Salva")

    def bloccaInizia(self):
        self.btnIniziaGioc.configure(state=tk.DISABLED)

    def ScegliNicks(self, event=None):
        self.checkIfSettedNicks()

        self.master.bind("<Return>", self.setProntoNicknames)
        self.master.bind("<Button-3>", self.setProntoNicknames)
        self.master.bind("<Escape>", self.toPreGioco)
        self.master.bind("<Control-Tab>", self.revealKeyBindSceglinicks)

        if self.plyrNicks == []:
            for i in range(self.nGiocatoriGioc.get()):
                self.plyrNicks.append(Giocatore("Giocatore " + str(i+1)))
        #print("OldNGioc: ", self.oldNGiocatoriGioc, "\t NGioc: ", self.nGiocatoriGioc.get())
        if self.oldNGiocatoriGioc != self.nGiocatoriGioc.get():
            self.plyrNicks = []
            for i in range(self.nGiocatoriGioc.get()):
                self.plyrNicks.append(Giocatore("Giocatore " + str(i+1)))
        self.old_plyrNicks=[]
        for l in range(len(self.plyrNicks)):
            self.old_plyrNicks.append(self.plyrNicks[l])
            self.plyrNicks[l].setFlagPronto(False)

        self.frameOpzioniGioc.grid_forget()
        self.frameScegliNicks.grid(row=1, rowspan=3, column=1)
        self.switchNickname(direction="")

    def switchNicknameSuono(self, direction):
        self.playSuono()
        self.switchNickname(direction)

    def switchNickname(self, direction):
        #print("direction: " + direction)
        #print("CurrentNick: " + self.currNick.get())
        if direction == "<":
            self.currentNick -= 1
            #print("CurrentNick - 1: "+ self.currNick.get())
        elif direction == ">":
            self.currentNick += 1
            #print("CurrentNick + 1: "+ self.currNick.get())

        if self.currentNick == 0:
            self.master.bind('<Left>', self.doNothing)
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchNickname(direction))
            self.btnPrevNick.configure(state=tk.DISABLED)
            self.btnNextNick.configure(state=tk.NORMAL)
            self.btnPrevNick.configure(bg=self.gioco_sfondo_bg_color, relief=tk.FLAT)
            self.btnNextNick.configure(bg=self.gioco_schedine_unset_bg_color, relief=tk.RAISED)
        elif self.currentNick == len(self.plyrNicks) - 1:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchNickname(direction))
            self.master.bind('<Right>', self.doNothing)
            self.btnPrevNick.configure(state=tk.NORMAL)
            self.btnNextNick.configure(state=tk.DISABLED)
            self.btnPrevNick.configure(bg=self.gioco_schedine_unset_bg_color, relief=tk.RAISED)
            self.btnNextNick.configure(bg=self.gioco_sfondo_bg_color, relief=tk.FLAT)
        else:
            self.master.bind('<Left>', lambda event=None, direction="<": self.switchNickname(direction))
            self.master.bind('<Right>', lambda event=None, direction=">": self.switchNickname(direction))
            self.btnPrevNick.configure(state=tk.NORMAL)
            self.btnNextNick.configure(state=tk.NORMAL)
            self.btnPrevNick.configure(bg=self.gioco_schedine_unset_bg_color, relief=tk.RAISED)
            self.btnNextNick.configure(bg=self.gioco_schedine_unset_bg_color, relief=tk.RAISED)

        self.lblNomegiocSceglinick.configure(text="Giocatore "+str(self.currentNick+1))
        self.currNick.set(self.plyrNicks[self.currentNick].getNome())

        if self.plyrNicks[self.currentNick].getFlagPronto() == False:
            self.btnProntoScegliNick.configure(bg=self.gioco_premi_titolo_fg_color, state=tk.NORMAL)
        else:
            self.btnProntoScegliNick.configure(bg=self.gioco_premi_bg_color, state=tk.DISABLED)

    def toPregiocoSuono(self):
        self.playSuono()
        self.toPreGioco()

    def toPreGioco(self, event=None):
        self.currentNick=0
        self.plyrNicks=[]
        for i in range(len(self.old_plyrNicks)):
            self.plyrNicks.append(self.old_plyrNicks[i])
            self.plyrNicks[i].setFlagPronto(False)
        self.frameOpzioniGioc.grid(row=3, column=1)
        self.frameScegliNicks.grid_forget()
        self.checkIfSettedNicks()

    def setProntoNicknames(self, event=None):
        self.plyrNicks[self.currentNick].setFlagPronto(True)
        self.plyrNicks[self.currentNick].setNome(self.currNick.get())
        self.btnProntoScegliNick.configure(bg="red")
        self.verificaProntiScegliNick()

    def verificaProntiScegliNick(self):
        counterProntiNicks = 0
        #print("counter prima: ", counterProntiNicks)
        for i in range(len(self.plyrNicks)):
            if self.plyrNicks[i].getFlagPronto() == True:
                counterProntiNicks += 1
                #print("counter dentro if: ", counterProntiNicks)

        #print("counter dopo: ", counterProntiNicks)
        #print("Lunghezza plyrNicks: ", len(self.plyrNicks))

        if counterProntiNicks == len(self.plyrNicks):
            self.btnSalvaScegliNick.configure(state=tk.NORMAL, relief=tk.RAISED, bg=self.gioco_premi_titolo_fg_color)
            self.master.bind("<Return>", self.SalvaNicknames)
            self.master.bind("<Button-3>", self.SalvaNicknames)

    def SalvaNicknames(self, event=None):
        self.currentNick = 0
        for l in range(len(self.plyrNicks)):
            self.old_plyrNicks[l].setNome(self.plyrNicks[l].getNome())
            self.plyrNicks[l].setFlagPronto(False)
        self.btnSalvaScegliNick.configure(state=tk.DISABLED, bg=self.gioco_sfondo_bg_color, relief=tk.FLAT)
        self.checkIfSettedNicks()
        self.frameOpzioniGioc.grid(row=3, column=1)
        self.frameScegliNicks.grid_forget()


root = Tombolone()

root.mainloop()
