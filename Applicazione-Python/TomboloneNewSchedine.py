import tkinter as tk
from tkinter import messagebox
import random

"""
TODO
 ||
 \/    """
#TODO
# far visualizzare il nickname nel titolo del gioco
# compattare/pulire il codice                                 #########################################################
# giocatori con cpu,
# poter visualizzare le schedine dei bot con le freccette,
# provare pygame,                                             #########################################################
# migliorare grafica generale,                                #########################################################
# generare e settare le schedine con il nSchedine
# controlli a fine partita per verificare validita schedine                                          #
# evitare ridonzdanze nel random delle schedine
# fixare i controlli per il tabellone
# dire il numero a voce quando viene estratto                 #########################################################
# fare controllo per ambo, terna, quaterna, cinquina, decina, tombola e tombolino                    #
# usare sleep per aspettare a selezionare celle delle cpu,
# usare anche per la difficolta                               #########################################################
#

class Giocatore():
    def __init__(self, nome, schedine):
        self._nome=nome
        self._schedine=schedine
        self._punteggioCorrente=0
        self._classifica=[[],[]]
    
    def setNome(self, nome):
        self._nome=nome
    
    def setSchedine(self, schedine):
        self._schedine=schedine

    def setPunteggioCorrente(self, punteggio):
        self._punteggioCorrente = punteggio

    def getNome(self):
        return self._nome
    
    def getSchedine(self):
        return self._schedine

    def getPunteggioCorrente(self):
        return self._punteggioCorrente


class Tombolone(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Il Tombolone")
        self.grid()
        self.globals()
        self.colors()
        self.CreateWidgets()
        self.Menu(event=None)

    def colors(self):
        # Setto le variabili globali dei colori 
        # per gli sfondi e per le scritte
        """"""
        """------------------   VARIABILI   -------------------"""
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

        self.impostazioni_sfondo_bg_color = "black"
        self.impostazioni_titolo_bg_color = "black"
        self.impostazioni_titolo_fg_color = "black"
        self.impostazioni_labels_bg_color = "black"
        self.impostazioni_labels_fg_color = "black"
        self.impostazioni_options_bg_color = "black"
        self.impostazioni_options_fg_color = "black"
        self.impostazioni_rbtn_circle_bg_color = "black"
        
        
        
        """------------------   SCURO   -------------------"""
        self.menu_sfondo_dark_bg_color = "black"
        self.menu_titolo_dark_bg_color = "black"
        self.menu_titolo_dark_fg_color = "white"
        self.menu_buttons_dark_bg_color = "gray"
        self.menu_buttons_dark_fg_color = "white"

        self.gioco_sfondo_dark_bg_color = "black"
        self.gioco_titolo_dark_bg_color = "black"
        self.gioco_titolo_dark_fg_color = "white"
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

        self.impostazioni_sfondo_dark_bg_color = "black"
        self.impostazioni_titolo_dark_bg_color = "black"
        self.impostazioni_titolo_dark_fg_color = "white"
        self.impostazioni_labels_dark_bg_color = "black"
        self.impostazioni_labels_dark_fg_color = "white"
        self.impostazioni_options_dark_bg_color = "gray"
        self.impostazioni_options_dark_fg_color = "white"
        self.impostazioni_rbtn_circle_dark_bg_color = "black"
        
        
        
        """------------------   CHIARO   -------------------"""
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

        self.impostazioni_sfondo_ligth_bg_color = "#0040ff"
        self.impostazioni_titolo_ligth_bg_color = "#0040ff"
        self.impostazioni_titolo_ligth_fg_color = "black"
        self.impostazioni_labels_ligth_bg_color = "#0080ff"
        self.impostazioni_labels_ligth_fg_color = "black"
        self.impostazioni_options_ligth_bg_color = "#0080ff"
        self.impostazioni_options_ligth_fg_color = "black"
        self.impostazioni_rbtn_circle_ligth_bg_color = "white"
        
    def checkTema(self):
        # Verifica quale tema si ha selezionato
        self.frameGioco.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameMenu.grid_forget()
        if self.tema.get() == "Normale":
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

            self.impostazioni_sfondo_bg_color = self.impostazioni_sfondo_ligth_bg_color       
            self.impostazioni_titolo_bg_color = self.impostazioni_titolo_ligth_bg_color       
            self.impostazioni_titolo_fg_color = self.impostazioni_titolo_ligth_fg_color       
            self.impostazioni_labels_bg_color = self.impostazioni_labels_ligth_bg_color       
            self.impostazioni_labels_fg_color = self.impostazioni_labels_ligth_fg_color       
            self.impostazioni_options_bg_color = self.impostazioni_options_ligth_bg_color      
            self.impostazioni_options_fg_color = self.impostazioni_options_ligth_fg_color      
            self.impostazioni_rbtn_circle_bg_color = self.impostazioni_rbtn_circle_ligth_bg_color  

            self.CreateWidgets()
            self.frameGioco.grid_forget()
            self.frameImpostazioni.grid_forget()
            self.frameMenu.grid_forget()

        elif self.tema.get() == "Scuro":
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
                                          
            self.impostazioni_sfondo_bg_color = self.impostazioni_sfondo_dark_bg_color       
            self.impostazioni_titolo_bg_color = self.impostazioni_titolo_dark_bg_color       
            self.impostazioni_titolo_fg_color = self.impostazioni_titolo_dark_fg_color       
            self.impostazioni_labels_bg_color = self.impostazioni_labels_dark_bg_color       
            self.impostazioni_labels_fg_color = self.impostazioni_labels_dark_fg_color       
            self.impostazioni_options_bg_color = self.impostazioni_options_dark_bg_color      
            self.impostazioni_options_fg_color = self.impostazioni_options_dark_fg_color      
            self.impostazioni_rbtn_circle_bg_color = self.impostazioni_rbtn_circle_dark_bg_color  

            self.CreateWidgets()
            self.frameGioco.grid_forget()
            self.frameImpostazioni.grid_forget()
            self.frameMenu.grid_forget()

    def CreateWidgets(self):
#TODO*****************************************************************************************************************\
# *****************************************  MENU PRINCIPALE  ********************************************************\
# *********************************************************************************************************************

        self.frameMenu=tk.Frame(self, bg=self.menu_sfondo_bg_color)


        margineAltoSx=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, width="20").grid(row=0, column=0)
        margineAltoDx=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, width="20").grid(row=0, column=2)

        spazioTraTitoloETop=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 30)).grid(row=0, column=1)

        """self.btnClassificaPersonale=tk.Button(self.frameMenu, text="🏆", bg=self.menu_sfondo_bg_color, font=("Helvetica", 15, "bold"))
        self.btnClassificaPersonale.grid(row=0, column=0, sticky="s")"""

        self.lblTitoloMenu=tk.Label(self.frameMenu, text="Tombolone", bg=self.menu_titolo_bg_color, fg=self.menu_titolo_fg_color, font=('Helvetica', 50))
        self.lblTitoloMenu.grid(row=1, column=1, sticky="nesw")

        spazioTraTitoloEScelte=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 30)).grid(row=2, column=1)

        self.btnGioca=tk.Button(self.frameMenu, text="Gioca", command=lambda:self.Gioca(event=None), bg=self.menu_buttons_bg_color, fg=self.menu_buttons_fg_color, font=("Helvetica", 30))
        #self.btnGioca.bind("<Return>", (lambda event: self.Gioca()))
        self.btnGioca.grid(row=3, column=1, sticky="nesw")

        #self.btnGioca.bind("<Return>", self.Gioca)
        #self.frameMenu.bind("<Enter>", (lambda event: self.Gioca))

        spazioTraScelte=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 20)).grid(row=4, column=1)

        self.btnImpostazioni=tk.Button(self.frameMenu, text="Impostazioni", command=lambda:self.Impostazioni(event=None), font=("Helvetica", 30), fg=self.menu_buttons_fg_color, bg=self.menu_buttons_bg_color)
        self.btnImpostazioni.grid(row=5, column=1, sticky="nesw")

        spazioTraScelte1=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 20)).grid(row=6, column=1)

        self.btnEsci=tk.Button(self.frameMenu, text="Esci", command=lambda: self.Esci(event=None), fg=self.menu_buttons_fg_color, bg=self.menu_buttons_bg_color, font=("Helvetica", 30))
        self.btnEsci.grid(row=7, column=1)

        spazioTraScelteEBottom=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 30)).grid(row=8, column=1)

#TODO*****************************************************************************************************************\
# ************************************************  GIOCO  ***********************************************************\
# *********************************************************************************************************************

        self.frameGioco = tk.Frame(self, bg=self.gioco_sfondo_bg_color)
        self.frameSchedine = tk.Frame(self.frameGioco, bg=self.gioco_sfondo_bg_color)

        #margineAltoDx=tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color, width=14).grid(row=0, column=0)

        tk.Label(self.frameGioco, text="", width=160, bg=self.gioco_sfondo_bg_color, font=("Helvetica", 11, "bold")).grid(row=0, column=0, columnspan=10, sticky="nesw")

        self.btnTornaAlMenuGioco=tk.Button(self.frameGioco, text="←", bg=self.gioco_sfondo_bg_color, fg=self.gioco_titolo_fg_color, highlightthickness=0, font=("Helvetica", 30), bd=0, command=lambda:self.Menu(event=None), relief="solid")
        self.btnTornaAlMenuGioco.grid(row=1, column=0)
        #self.update()
        #print("Altezza",btnTornaAlMenu.winfo_height())
        #print("larghezza", btnTornaAlMenu.winfo_width())
        fakebtnTornaAlMenu = tk.Button(self.frameGioco, bg=self.gioco_sfondo_bg_color, highlightthickness=0, state=tk.DISABLED, relief=tk.FLAT, height=4, width=17).grid(row=1, column=9)

        nick=str(self.nickname.get())
        self.lblTitoloGioco = tk.Label(self.frameGioco, width=20, text=nick, justify=tk.CENTER, fg=self.gioco_titolo_fg_color, bg=self.gioco_sfondo_bg_color, font=('Helvetica', 50))
        self.lblTitoloGioco.grid(row=1, column=4, columnspan=2, sticky="nesw")

        tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=2, column=0)


        frameNEstratto = tk.Frame(self.frameGioco, bg=self.gioco_sfondo_bg_color)

        self.lblNEstratto = tk.Button(frameNEstratto, text="Estrai", command= lambda: self.estrai(event=None), bg=self.gioco_label_nestratto_bg_color, font=("Helvetica", 20, "bold"),fg=self.gioco_label_nestratto_fg_color)
        self.lblNEstratto.grid(row=0)
        self.btnNEstratto = tk.Label(frameNEstratto, text="", fg=self.gioco_nestratto_fg_color, bg=self.gioco_nestratto_bg_color, height=2, font=('Helvetica', 15))
        self.btnNEstratto.grid(row=0, column=10, padx=20)

        frameNEstratto.grid(row=3, column=4,  columnspan=2)

        tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=4, column=0)

        # Tabellone
        #todo DA COMPATTARE
        frameTabellone=tk.Frame(self.frameGioco, highlightbackground="black", highlightthickness=1, bg=self.gioco_tabellone_unset_bg_color)
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
            lbl=tk.Label(frameTabellone, text=i+1, bg=self.gioco_tabellone_unset_bg_color, fg=self.gioco_tabellone_unset_fg_color)
            lbl.grid(row=row, column=column, sticky="nesw")
            tupla1 = (lbl, i+1)
            self.arrTabellone.append(lbl)
        frameTabellone.grid(row=0, rowspan=4, column=6, columnspan=3, sticky="e")
        #self.update()
        #print("larghezza: ", frameTabellone.winfo_width())
        #print("altezza: ", frameTabellone.winfo_height())
        faketabellone=tk.Frame(self.frameGioco, bg=self.gioco_sfondo_bg_color, height=191, width=182).grid(row=0, rowspan=4, column=1, columnspan=3)
        #frameTabellone.grid(row=0, column=0, sticky="ne", padx=50, pady=20)

        tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=6, column=0)

        #Schedine segnaposto                                          SCHEDINE
        self.arrSchedine = []
        h = 0
        for nSchedina in range(self.nSchedine.get() * 2):
            h += 1
            arrSchedina = []
            arrRow1 = []
            arrRow2 = []
            arrRow3 = []
            schedina = tk.Frame(self.frameSchedine, bg=self.gioco_sfondo_bg_color)
            if (nSchedina % 2) == 0:
                # Riga
                for riga in range(3):
                    # Colonna
                    for colonna in range(9):
                        cella = tk.Button(schedina, text="N", bg=self.gioco_schedine_unset_bg_color, disabledforeground=self.gioco_schedine_disabled_fg_color, font=("Helvetica", 17), width=2, bd=1, highlightcolor="black", relief=tk.SOLID)
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
                self.arrSchedine.append(arrSchedina)
            else:
                tk.Label(self.frameSchedine, text="  ", font=("Helvetica", 2), bg=self.gioco_sfondo_bg_color).grid(row=1, column=h)
            if nSchedina + 1 <= 6:
                schedina.grid(row=0, column=h)
                if nSchedina + 1 == 6:
                    h = 0
            elif nSchedina + 1 > 6 and nSchedina + 1 <= 12:
                schedina.grid(row=2, column=h)
                if nSchedina + 1 == 12:
                    h = 0

        #schedine
        for i in range(len(self.arrSchedine)):
            #righe
            for t in range(len(self.arrSchedine[i])):
                #celle
                for l in range(len(self.arrSchedine[i][t])):
                    #print(self.arrSchedine[i][t][l].cget("text"))
                    self.setCommandCelle(i, t, l)

        tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color, height=1).grid(row=12, column=9)

        self.btnPrevPlayer=tk.Button(self.frameGioco, text="<", highlightthickness=0, disabledforeground=self.gioco_sfondo_bg_color, state=tk.DISABLED, bg=self.gioco_label_nestratto_bg_color, fg=self.gioco_label_nestratto_fg_color, font=("Helvetica", 15, "bold"), command=lambda:self.switchPlayer("<"))
        self.btnPrevPlayer.grid(row=9, column=1, sticky="w")
        self.btnNextPlayer=tk.Button(self.frameGioco, text=">", highlightthickness=0, disabledforeground=self.gioco_sfondo_bg_color, bg=self.gioco_label_nestratto_bg_color, fg=self.gioco_label_nestratto_fg_color, font=("Helvetica", 15, "bold"), command=lambda:self.switchPlayer(">"))
        self.btnNextPlayer.grid(row=9, column=8, sticky="e")

        self.frameSchedine.grid(row=8, column=2, columnspan=6, rowspan=3)


#TODO*****************************************************************************************************************\
# ********************************************  IMPOSTAZIONI  ********************************************************\
# *********************************************************************************************************************

        self.frameImpostazioni=tk.Frame(self, bg=self.impostazioni_sfondo_bg_color)

        margineAltoSx = tk.Label(self.frameImpostazioni, width="20", bg=self.impostazioni_sfondo_bg_color).grid(row=0, column=0)
        margineAltoDx = tk.Label(self.frameImpostazioni, width="20", bg=self.impostazioni_sfondo_bg_color).grid(row=0, column=4)

        spazioTraTitoloETop = tk.Label(self.frameImpostazioni, bg=self.impostazioni_sfondo_bg_color, font=("Helvetica", 30)).grid(row=0, column=2)

        self.btnTornaAlMenuImpostazioni = tk.Button(self.frameImpostazioni, text="←", bg=self.impostazioni_sfondo_bg_color, fg=self.impostazioni_titolo_fg_color, font=("Helvetica", 30), bd=0, command=lambda:self.indietro(event=None), relief=tk.FLAT)
        self.btnTornaAlMenuImpostazioni.grid(row=1, column=0)

        self.lblTitoloImpostazioni = tk.Label(self.frameImpostazioni, text="Impostazioni", fg=self.impostazioni_titolo_fg_color, bg=self.impostazioni_titolo_bg_color, font=('Helvetica', 50))
        self.lblTitoloImpostazioni.grid(row=1, column=1, columnspan=3, sticky="nesw")

        spazioTraTitoloEScelte = tk.Label(self.frameImpostazioni, font=("Helvetica", 30), bg=self.impostazioni_sfondo_bg_color).grid(row=2, column=2)

        self.lblNickGiocatore=tk.Label(self.frameImpostazioni, text="Nickname", font=("Helvetica", 30), bg=self.impostazioni_labels_bg_color, fg=self.impostazioni_labels_fg_color)
        self.lblNickGiocatore.grid(row=3, column=1, columnspan=2, sticky="w")

        self.enNickGiocatori=tk.Entry(self.frameImpostazioni, textvariable=self.nickname, width=15, font=("Helvetica", 15), bg=self.impostazioni_options_bg_color, fg=self.impostazioni_options_fg_color)
        self.enNickGiocatori.grid(row=3, column=2, columnspan=2, sticky="e")

        spazioTraScelte = tk.Label(self.frameImpostazioni, font=("Helvetica", 20), bg=self.impostazioni_sfondo_bg_color).grid(row=4, column=2)

        self.lblNGiocatori = tk.Label(self.frameImpostazioni, text="N Giocatori", fg=self.impostazioni_labels_fg_color, bg=self.impostazioni_labels_bg_color, font=("Helvetica", 30))
        self.lblNGiocatori.grid(row=5, column=1, columnspan=2, sticky="w")

        self.spnNGiocatori = tk.OptionMenu(self.frameImpostazioni, self.nGiocatori, "2","3","4","5","6","7","8","9","10")
        self.spnNGiocatori.configure(highlightthickness=0, bg=self.impostazioni_options_bg_color, fg=self.impostazioni_options_fg_color, font=("Helvetica", 20), width=5)
        self.spnNGiocatori.grid(row=5, column=2, columnspan=2, sticky="e")

        spazioTraScelte1 = tk.Label(self.frameImpostazioni, font=("Helvetica", 20), bg=self.impostazioni_sfondo_bg_color).grid(row=6, column=2)

        self.lblNSchedine = tk.Label(self.frameImpostazioni, text="N Schedine", fg=self.impostazioni_labels_fg_color, bg=self.impostazioni_labels_bg_color, font=("Helvetica", 30))
        self.lblNSchedine.grid(row=7, column=1, columnspan=2, sticky="w")

        self.spnNSchedine = tk.OptionMenu(self.frameImpostazioni, self.nSchedine, "1", "2", "3", "4", "5", "6")
        self.spnNSchedine.configure(highlightthickness=0, bg=self.impostazioni_options_bg_color, fg=self.impostazioni_options_fg_color, font=("Helvetica", 20), width=5)
        self.spnNSchedine.grid(row=7, column=2, columnspan=2, sticky="e")

        spazioTraScelte2 = tk.Label(self.frameImpostazioni, font=("Helvetica", 20), bg=self.impostazioni_sfondo_bg_color).grid(row=8, column=2)


        frameTema=tk.Frame(self.frameImpostazioni, bg=self.impostazioni_options_bg_color)

        lblTema = tk.Label(frameTema, text="Tema", font=("Helvetica", 30), fg=self.impostazioni_labels_fg_color, bg=self.impostazioni_labels_bg_color).grid(row=0, column=0)

        spazioTraScelteTema=tk.Label(frameTema, text=" ", bg=self.impostazioni_sfondo_bg_color, width="28").grid(row=0, column=1, sticky="nesw")

        self.rbtnTema1 = tk.Radiobutton(frameTema, text="Colorato", variable=self.tema, selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Normale", bg=self.impostazioni_options_bg_color).grid(row=0, column=2)
        self.rbtnTema2 = tk.Radiobutton(frameTema, text="Scuro", variable=self.tema, selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Scuro", bg=self.impostazioni_options_bg_color).grid(row=0, column=3)

        frameTema.grid(row=9, column=1, columnspan=2, sticky="nesw")


        spazioTraScelte1 = tk.Label(self.frameImpostazioni, font=("Helvetica", 20), bg=self.impostazioni_sfondo_bg_color).grid(row=10, column=2)


        frameTipoSchedine=tk.Frame(self.frameImpostazioni, bg=self.impostazioni_options_bg_color)

        lblTipoSched = tk.Label(frameTipoSchedine, text="Schedina", font=("Helvetica", 30), fg="gray", bg=self.impostazioni_labels_bg_color).grid(row=0, column=0)

        spazioTraScelteTema=tk.Label(frameTipoSchedine, text=" ", bg=self.impostazioni_sfondo_bg_color, width="15").grid(row=0, column=1, sticky="nesw")

        self.rbtnTpoSched1 = tk.Radiobutton(frameTipoSchedine, state=tk.DISABLED, text="Tombolone", variable=self.tipoSched, selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Tombolone", bg=self.impostazioni_options_bg_color).grid(row=0, column=2)
        self.rbtnTpoSched2 = tk.Radiobutton(frameTipoSchedine, state=tk.DISABLED, text="Classic", variable=self.tipoSched, selectcolor=self.impostazioni_rbtn_circle_bg_color, highlightthickness=0, fg=self.impostazioni_options_fg_color, value="Classic", bg=self.impostazioni_options_bg_color).grid(row=0, column=3)

        frameTipoSchedine.grid(row=11, column=1, columnspan=3, sticky="nesw")


        spazioTraScelte2 = tk.Label(self.frameImpostazioni, font=("Helvetica", 20), bg=self.impostazioni_sfondo_bg_color).grid(row=12, column=2)

        self.btnSalva = tk.Button(self.frameImpostazioni, text="Salva", command=lambda: self.Menu(event=None), fg=self.impostazioni_options_fg_color, bg=self.impostazioni_options_bg_color, font=("Helvetica", 30))
        self.btnSalva.grid(row=13, column=1, columnspan=3)

        spazioTraScelteEBottom = tk.Label(self.frameImpostazioni, font=("Helvetica", 30), bg=self.impostazioni_sfondo_bg_color).grid(row=14, column=1)

    def creaSchedineGiocatori(self, plyr):
        # Creo una pseudo-schedina con una tupla
        # contenente il numero e lo stato (set o unset)

        arrSchedine = []
        h = 0
        for nSchedina in range(self.nSchedine.get() * 2):
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

    def assegnaSchedineGiocatori(self):
        # Per ogni nGiocatore creo una pseudoschedina
        # contenente solo un numero e lo stato(set o unset)

        giocatore = Giocatore("boh", [])

        # Giocatori
        for t in range(self.nGiocatori.get()):
            arrSchedine = self.creaSchedineGiocatori(t)
            if self.giocatore.getSchedine() == []:
                self.giocatore.setSchedine(arrSchedine)
                giocatore = self.giocatore
            else:
                giocatore = Giocatore("CPU " + str(t), arrSchedine)
            self.giocatoriCpu.append(giocatore)

        # STAMPO COSSEH

        """"#DEBUG
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
                    print()"""

    def setCommandCelle(self, nScheda, nRiga, nCella):
        self.arrSchedine[nScheda][nRiga][nCella].configure(command=lambda: self.click(0, nScheda, nRiga, nCella, "plyr"))

    def estrai(self, event):
        #Estrae i numeri casuali della partita

        randN=random.randint(1, 90)
        if self.nEstratti == []:
            self.btnNEstratto.configure(text=randN)
            self.nEstratti.append(randN)

            # Tabellone
            for i in range(len(self.arrTabellone)):
                if int(self.arrTabellone[i].cget("text")) == randN:
                    self.arrTabellone[i].configure(bg=self.gioco_tabellone_set_bg_color)
            #DEBUG  print("N Estratto: ", randN)

        elif self.nEstratti.count(randN) != 0:
            self.estrai(event=None)
        else:
            self.btnNEstratto.configure(text=randN)
            self.nEstratti.append(randN)

            # Tabellone
            for i in range(len(self.arrTabellone)):
                if int(self.arrTabellone[i].cget("text")) == randN:
                    self.arrTabellone[i].configure(bg=self.gioco_tabellone_set_bg_color)

        #Le CPU aspettano un tot prima di selezionare le celle e dichiarare i premi
        if self.nSchedine.get() == 1 or self.nSchedine.get() == 2:
            sec = random.randint(2000, 5000)
        elif self.nSchedine.get() == 3 or self.nSchedine.get() == 4:
            sec = random.randint(3000, 7000)
        elif self.nSchedine.get() == 5 or self.nSchedine.get() == 6:
            sec = random.randint(4000, 10000)
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
                                        self.arrSchedine[l][y][t].configure(bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color)
                                        self.click(i, l, y, self.giocatoriCpu[i].getSchedine()[l][y][t][0], "cpu")
                                    else:
                                        self.click(i, l, y, self.giocatoriCpu[i].getSchedine()[l][y][t][0], "cpu")

    def globals(self):
        # Setto le variabili "globali"
        self.nickname=tk.StringVar(self, "Default Nick")
        self.nEstratti=[]
        self.currentPlayer=0
        self.giocatore=Giocatore(self.nickname.get(), [])
        self.giocatoriCpu=[]
        self.nGiocatori=tk.IntVar(self, 2)
        self.nSchedine=tk.IntVar(self, 1)
        self.tema=tk.StringVar(self, "Normale")
        self.tipoSched=tk.StringVar(self, "Classic")
        self.ambo = False
        self.terna = False
        self.quaterna = False
        self.cinquina = False
        self.decina = False
        self.tombola = False
        self.tombolino = False

    def Esci(self, event):
        self.master.quit()

    def Menu(self, event):
        # Porta in primo piano il Menu

        self.master.bind('<Return>', self.Gioca)
        self.master.bind('<Button-3>', self.Gioca)
        self.master.bind('<Escape>', self.Esci)

        self.checkTema()

        self.frameGioco.grid_forget()
        self.frameImpostazioni.grid_forget()
        #self.master.bind('<Enter>', lambda event: self.Gioca)
        self.frameMenu.grid(row=0, column=0)

    def Gioca(self, event):

        self.master.bind('<Return>', None)
        self.master.bind('<Button-3>', self.estrai)
        self.master.bind('<Escape>', self.Menu)

        # Porta in primo piano la schermata del gioco
        self.currentPlayer=0
        self.nickname.set(self.enNickGiocatori.get())
        self.giocatore=Giocatore(self.nickname.get(), [])
        self.giocatoriCpu=[]
        self.assegnaSchedineGiocatori()
        self.switchPlayer("")
        self.nEstratti=[]
        self.estrai(event)
        self.ambo = False
        self.terna = False
        self.quaterna = False
        self.cinquina = False
        self.decina = False
        self.tombola = False
        self.tombolino = False
        self.frameMenu.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameGioco.grid(row=0, column=0)

    def switchPlayer(self, direction):
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
            self.btnPrevPlayer.configure(state=tk.DISABLED)
            self.btnNextPlayer.configure(state=tk.NORMAL)
            self.btnPrevPlayer.configure(bg=self.gioco_sfondo_bg_color, relief=tk.FLAT)
            self.btnNextPlayer.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            #self.btnPrevPlayer.grid_forget()
            #self.btnNextPlayer.grid(row=11, column=4)

        elif self.currentPlayer == len(self.giocatoriCpu)-1:
            self.btnPrevPlayer.configure(state=tk.NORMAL)
            self.btnNextPlayer.configure(state=tk.DISABLED)
            self.btnPrevPlayer.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            self.btnNextPlayer.configure(bg=self.gioco_sfondo_bg_color, relief=tk.FLAT)
            #self.btnPrevPlayer.grid(row=11, column=1)
            #self.btnNextPlayer.grid_forget()

        else:
            self.btnPrevPlayer.configure(state=tk.NORMAL)
            self.btnNextPlayer.configure(state=tk.NORMAL)
            self.btnPrevPlayer.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            self.btnNextPlayer.configure(bg=self.gioco_label_nestratto_bg_color, relief=tk.RAISED)
            #self.btnPrevPlayer.grid(row=11, column=1)
            #self.btnNextPlayer.grid(row=11, column=4)

        """"#DEBUG
        print("CurrentPlayer: ", self.currentPlayer)
        print("nGiocatori: ", self.nGiocatori.get())
        print("nGiocatori-1: ", self.nGiocatori.get()-1)
        print("Len: ", len(self.giocatoriCpu))
        for h in range(len(self.giocatoriCpu)):
            print("\t"+self.giocatoriCpu[h].getNome())"""

        self.lblTitoloGioco.configure(text=self.giocatoriCpu[self.currentPlayer].getNome())

        # Schedine
        for i in range(len(self.arrSchedine)):
            # Righe
            for l in range(len(self.arrSchedine[i])):
                # Celle
                for k in range(len(self.arrSchedine[i][l])):

                    if self.giocatoriCpu[self.currentPlayer].getNome() == self.nickname.get():
                        if self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][0] != " ":
                            self.arrSchedine[i][l][k].configure(state=tk.NORMAL)
                        else:
                            self.arrSchedine[i][l][k].configure(state=tk.DISABLED)
                    else:
                        self.arrSchedine[i][l][k].configure(state=tk.DISABLED)
                    self.arrSchedine[i][l][k].configure(text=self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][0])
                    if self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][1] == "unset":
                        self.arrSchedine[i][l][k].configure(bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color)
                    elif self.giocatoriCpu[self.currentPlayer].getSchedine()[i][l][k][1] == "set":
                        self.arrSchedine[i][l][k].configure(bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color)

    def Impostazioni(self, event):
        # Porta in primo piano la schermata delle Impostazioni

        self.master.bind('<Return>', self.Menu)
        self.master.bind('<Escape>', self.indietro)

        self.frameMenu.grid_forget()
        self.frameGioco.grid_forget()
        self.frameImpostazioni.grid(row=0, column=0)
        
        self.oldNGiocatori=self.nGiocatori.get()
        self.oldNSchedine=self.nSchedine.get()
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
        self.old_impostazioni_sfondo_bg_color=self.impostazioni_sfondo_bg_color
        self.old_impostazioni_titolo_bg_color=self.impostazioni_titolo_bg_color
        self.old_impostazioni_titolo_fg_color=self.impostazioni_titolo_fg_color
        self.old_impostazioni_labels_bg_color=self.impostazioni_labels_bg_color
        self.old_impostazioni_labels_fg_color=self.impostazioni_labels_fg_color
        self.old_impostazioni_options_bg_color=self.impostazioni_options_bg_color
        self.old_impostazioni_options_fg_color=self.impostazioni_options_fg_color
        self.old_impostazioni_rbtn_circle_bg_color=self.impostazioni_rbtn_circle_bg_color

    def indietro(self, event):
        # Se non si salvano le impostazioni selezionate 
        # non le aggiorna nelle variabili globali
        self.nGiocatori.set(self.oldNGiocatori)
        self.nSchedine.set(self.oldNSchedine)
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
        self.impostazioni_sfondo_bg_color=self.old_impostazioni_sfondo_bg_color
        self.impostazioni_titolo_bg_color=self.old_impostazioni_titolo_bg_color
        self.impostazioni_titolo_fg_color=self.old_impostazioni_titolo_fg_color
        self.impostazioni_labels_bg_color=self.old_impostazioni_labels_bg_color
        self.impostazioni_labels_fg_color=self.old_impostazioni_labels_fg_color
        self.impostazioni_options_bg_color=self.old_impostazioni_options_bg_color
        self.impostazioni_options_fg_color=self.old_impostazioni_options_fg_color
        self.impostazioni_rbtn_circle_bg_color=self.old_impostazioni_rbtn_circle_bg_color
        
        self.Menu(event=None)

    def click(self, giocatore, nScheda, nRiga, nCella, flag):
        # colora la cella selezionata quando la si
        # clicca nella grid(vale solo per il giocatore)

        if flag != "cpu":
            # Segna i numeri cliccati nelle schedine
            if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][nCella][0] != " ":
                if self.arrSchedine[nScheda][nRiga][nCella].cget("bg") == self.gioco_schedine_unset_bg_color:
                    self.arrSchedine[nScheda][nRiga][nCella].configure(bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color)
                    arr = self.giocatoriCpu[self.currentPlayer].getSchedine()
                    num = self.giocatoriCpu[self.currentPlayer].getSchedine()[nScheda][nRiga][nCella][0]
                    commnd = "set"
                    tupla = [num, commnd]
                    arr[nScheda][nRiga][nCella] = tupla
                    self.giocatoriCpu[self.currentPlayer].setSchedine(arr)
                else:
                    self.arrSchedine[nScheda][nRiga][nCella].configure(bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color)
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

        counter=0
        # celle
        for y in range(len(self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga])):
            if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][y][1] == "set":
                for i in range(len(self.arrTabellone)):
                    if self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][y][0] != " ":
                        if self.arrTabellone[i].cget("bg") == self.gioco_tabellone_set_bg_color  and  int(self.arrTabellone[i].cget("text")) == int(self.giocatoriCpu[giocatore].getSchedine()[nScheda][nRiga][y][0]):
                            counter+=1

        #Giocatore
        if self.giocatoriCpu[giocatore].getNome() == self.nickname.get():
            if counter==2 and self.ambo is False:
                self.ambo=True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+2)
                print("Hai fatto AMBO sulla scheda N." + str(nScheda+1) , " e hai gudagnato 2 punti")
                messagebox.showinfo("CONGRATULAZIONI "+self.giocatoriCpu[giocatore].getNome()+"!!", "Hai fatto AMBO sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 2 punti")
            elif counter==3 and self.terna is False:
                self.terna = True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+3)
                print("Hai fatto TERNA sulla scheda N.", nScheda+1 , " e hai gudagnato 3 punti")
                messagebox.showinfo("CONGRATULAZIONI "+self.giocatoriCpu[giocatore].getNome()+"!!", "Hai fatto TERNA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 3 punti")
            elif counter==4 and self.quaterna is False:
                self.quaterna = True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+4)
                print("Hai fatto QUATERNA sulla scheda N.", nScheda+1 , " e hai gudagnato 4 punti")
                messagebox.showinfo("CONGRATULAZIONI "+self.giocatoriCpu[giocatore].getNome()+"!!", "Hai fatto QUATERNA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 4 punti")
            elif counter==5 and self.cinquina is False:
                self.cinquina = True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+5)
                print("Hai fatto CINQUINA sulla scheda N.", nScheda+1 , " e hai gudagnato 5 punti")
                messagebox.showinfo("CONGRATULAZIONI "+self.giocatoriCpu[giocatore].getNome()+"!!", "Hai fatto CINQUINA sulla scheda N." + str(nScheda + 1) + "\n   Hai gudagnato 5 punti")
        #CPU
        else:
            if counter==2 and self.ambo is False:
                self.ambo=True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+2)
                print(self.giocatoriCpu[giocatore].getNome() + " ha fatto AMBO sulla scheda N." + str(nScheda+1))
                messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Ambo sulla scheda N." + str(nScheda + 1))
            elif counter==3 and self.terna is False:
                self.terna = True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+3)
                print(self.giocatoriCpu[giocatore].getNome() + " ha fatto TERNA sulla scheda N.", nScheda+1)
                messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Terna sulla scheda N." + str(nScheda + 1))
            elif counter==4 and self.quaterna is False:
                self.quaterna = True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+4)
                print(self.giocatoriCpu[giocatore].getNome() + " ha fatto QUATERNA sulla scheda N.", nScheda+1)
                messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Quaterna sulla scheda N." + str(nScheda + 1))
            elif counter==5 and self.cinquina is False:
                self.cinquina = True
                self.giocatoriCpu[giocatore].setPunteggioCorrente(self.giocatoriCpu[giocatore].getPunteggioCorrente()+5)
                print(self.giocatoriCpu[giocatore].getNome() + " ha fatto CINQUINA sulla scheda N.", nScheda+1)
                messagebox.showwarning("ATTENZIONE!!", self.giocatoriCpu[giocatore].getNome() + " ha fatto Cinquina sulla scheda N." + str(nScheda + 1))

        counterWin1 = 0
        self.previousWinner = ""
        for y in range(len(self.giocatoriCpu[giocatore].getSchedine()[nScheda])):
            for h in range(len(self.giocatoriCpu[giocatore].getSchedine()[nScheda][y])):
                if self.giocatoriCpu[giocatore].getSchedine()[nScheda][y][h][1] == "set":
                    counterWin1 += 1

        if counterWin1 == 15 and self.tombola is False:
            self.tombola = True
            if self.giocatoriCpu[giocatore].getNome() == self.nickname.get():
                if self.verificaValiditaPremi(giocatore) == True:
                    print("HAI VINTOOOOOOOOO!!! Con ",self.giocatoriCpu[giocatore].getPunteggioCorrente(), " punti!")
                    messagebox.showinfo("GRANDE!!   HAI VINTO!!!", "HAI FATTO TOMBOLA sulla scheda N."+ str(nScheda+1) +" \n con punteggio di "+str(self.giocatoriCpu[giocatore].getPunteggioCorrente())+"!!!")
                    self.previousWinner = self.giocatoriCpu[giocatore].getNome()
                    self.showClassifica()
                elif self.verificaValiditaPremi(giocatore) == False:
                    self.tombola = False
                    print("Non hai vinto perche' hai barato!")
                    messagebox.showerror("Non si puo fare >:(", "LA SCHEDINA N. " + str(nScheda+1) + " NON E' VALIDA!!!")
            else:
                print("Mi dispiace, hai perso...")
                messagebox.showwarning("CHE PECCATO!! Hai perso...  Ma c'e' ancora Tombolino :)", self.giocatoriCpu[giocatore].getNome()+" ha fatto TOMBOLA sulla scheda N." + str(nScheda + 1) + "...")
                self.previousWinner=self.giocatoriCpu[giocatore].getNome()
                self.showClassifica()

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

        if counterCroupier == 90:
            loseByCroupier += 1
            if loseByCroupier == 1:
                self.after(10000, lambda:self.faVincereIlCroupier())

    """def faVincereIlCroupier(self):
        print("Ha vinto il croupier!")
        messagebox.showwarning("Che Peccato!  Hai perso...", "Ha vinto il Croupier per mancanza di numeri da estrarre")
        for y in range(len(self.arrTabellone)):
            self.arrTabellone[y].configure(bg=self.gioco_tabellone_unset_bg_color)
        self.Menu(event=None)"""

    """def checkByColor(self, nScheda, nRiga):
        # E' come controllavo prima i premi(ovvero con
        # i bg dei buttons ora diventati segnaposto)
        counterRow=0
        for i in range(len(self.arrSchedine[nScheda][nRiga])):
            if self.arrSchedine[nScheda][nRiga][i].cget("bg") == self.gioco_schedine_set_bg_color:
                counterRow+=1

        if counterRow==2 and self.ambo is False:
            self.ambo=True
            print(self.giocatoriCpu[self.currentPlayer].getNome() + " ha fatto Ambo sulla scheda N.", nScheda+1)
            messagebox.showinfo("CONGRATULAZIONI!!", self.giocatoriCpu[self.currentPlayer].getNome() + " ha fatto Ambo sulla scheda N." + str(nScheda + 1))
        elif counterRow==3 and self.terna is False:
            self.terna = True
            print(self.giocatoriCpu[self.currentPlayer].getNome() + " ha fatto Terna sulla scheda N.", nScheda+1)
            messagebox.showinfo("CONGRATULAZIONI!!", self.giocatoriCpu[self.currentPlayer].getNome() + " ha fatto Terna sulla scheda N." + str(nScheda + 1))
        elif counterRow==4 and self.quaterna is False:
            self.quaterna = True
            print(self.giocatoriCpu[self.currentPlayer].getNome() + " ha fatto Quaterna sulla scheda N.", nScheda+1)
            messagebox.showinfo("CONGRATULAZIONI!!", self.giocatoriCpu[self.currentPlayer].getNome() + " ha fatto Quaterna sulla scheda N." + str(nScheda + 1))
        elif counterRow==5 and self.cinquina is False:
            self.cinquina = True
            print(self.giocatoriCpu[self.currentPlayer].getNome() + " ha fatto Cinquina sulla scheda N.", nScheda+1)
            messagebox.showinfo("CONGRATULAZIONI!!", self.giocatoriCpu[self.currentPlayer].getNome() + " ha fatto Cinquina sulla scheda N." + str(nScheda + 1))

        counterWin1=0
        for y in range(len(self.arrSchedine[nScheda])):
            for h in range(len(self.arrSchedine[nScheda][y])):
                if self.arrSchedine[nScheda][y][h].cget("bg") == self.gioco_schedine_set_bg_color:
                    counterWin1+=1

        if counterWin1 == 15:
            print("HAI VINTOOOOOOOOO!!!")
            messagebox.showinfo("GRANDE!!   HAI VINTO!!!", "HAI FATTO TOMBOLA sulla scheda N."+ str(nScheda+1) +"!!!")"""

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
        #Giocatori
        for i in range(len(self.giocatoriCpu)):
            if self.previousWinner == self.giocatoriCpu[i].getNome():
                lblNome=tk.Button(frameInfo, disabledforeground=self.gioco_schedine_unset_fg_color, state=tk.DISABLED, font=("Helvetica", 30), text=self.giocatoriCpu[i].getNome(), command=lambda:self.goToPlayerClassifica(self.giocatoriCpu[i].getNome()), relief=tk.SOLID, bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color).grid(row=i+1, column=0, sticky="nesw")
                lblPunt=tk.Button(frameInfo, disabledforeground=self.gioco_schedine_unset_fg_color, state=tk.DISABLED, font=("Helvetica", 30), text=self.giocatoriCpu[i].getPunteggioCorrente(), command=lambda:self.goToPlayerClassifica(self.giocatoriCpu[i].getNome()), relief=tk.SOLID, bg=self.gioco_schedine_unset_bg_color, fg=self.gioco_schedine_unset_fg_color).grid(row=i+1, column=1, sticky="nesw")
            else:
                lblNome = tk.Button(frameInfo, disabledforeground=self.gioco_schedine_set_fg_color, state=tk.DISABLED, font=("Helvetica", 30), text=self.giocatoriCpu[i].getNome(), command=lambda:self.goToPlayerClassifica(self.giocatoriCpu[i].getNome()), relief=tk.SOLID, bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color).grid( row=i + 1, column=0, sticky="nesw")
                lblPunt = tk.Button(frameInfo, disabledforeground=self.gioco_schedine_set_fg_color, state=tk.DISABLED, font=("Helvetica", 30), text=self.giocatoriCpu[i].getPunteggioCorrente(), command=lambda:self.goToPlayerClassifica(self.giocatoriCpu[i].getNome()), relief=tk.SOLID, bg=self.gioco_schedine_set_bg_color, fg=self.gioco_schedine_set_fg_color).grid(row=i + 1, column=1, sticky="nesw")
        frameInfo.grid(row=1, rowspan=10, column=0, columnspan=3, padx=20)
        btnVaialMenu=tk.Button(frameClassifica, font=("Helvetica", 30), text="Rigioca", command=lambda:self.replayClassifica(), bg=self.gioco_sfondo_bg_color, fg=self.gioco_titolo_fg_color).grid(row=11, column=0, columnspan=2, sticky="nsw")
        btnEsci=tk.Button(frameClassifica, font=("Helvetica", 30), text="Menu", command=lambda:self.goToMenuClassifica(), bg=self.gioco_sfondo_bg_color, fg=self.gioco_titolo_fg_color).grid(row=11, column=1, columnspan=2, sticky="nes")
        frameClassifica.grid()

    """def goToPlayerClassifica(self, clickedPlyr):
        #self.Classifica.withdraw()
        for i in range(len(self.giocatoriCpu)):
            print("giocatore: ", i )
            print("CurPlayer: ", self.currentPlayer)
            print("Giocatore Lista: "+ self.giocatoriCpu[i].getNome())
            if clickedPlyr == self.giocatoriCpu[i].getNome():
                print("sono nella if")
                self.switchPlayer(int(i))
            print("--------------------------------------------------------")"""

    def replayClassifica(self):
        self.Menu(event=None)
        self.Gioca(event=None)
        self.Classifica.destroy()

    def goToMenuClassifica(self):
        self.Menu(event=None)
        self.Classifica.destroy()


root = Tombolone()

root.mainloop()
