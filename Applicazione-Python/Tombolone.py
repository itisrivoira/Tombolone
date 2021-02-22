import tkinter as tk
import random

class Tombolone(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.globals()
        self.colors()
        self.CreateWidgets()
        self.estrai()
        self.frameMenu.grid()

    def colors(self):
        # Setto le variabili globali dei colori 
        # per gli sfondi e per le scritte
        self.menu_sfondo_bg_color="orange"
        self.gioco_sfondo_bg_color="red"
        self.impostazioni_sfondo_bg_color="#0040ff"

        self.menu_widget_bg_color="orange"
        self.gioco_widget_bg_color="yellow"
        self.impostazioni_widget_bg_color="#0080ff"

        self.menu_widget_fg_color="black"
        self.gioco_widget_fg_color="black"
        self.impostazioni_widget_fg_color="black"

    def CreateWidgets(self):
        #MENU PRINCIPALE **********************************************************************************************

        self.frameMenu=tk.Frame(self, bg=self.menu_sfondo_bg_color)


        margineAltoSx=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, width="20").grid(row=0, column=0)
        margineAltoDx=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, width="20").grid(row=0, column=2)

        spazioTraTitoloETop=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 30)).grid(row=0, column=1)

        self.lblTitoloMenu=tk.Label(self.frameMenu, text="Tombolone", bg=self.menu_sfondo_bg_color, fg=self.menu_widget_fg_color, font=('Helvetica', 50))
        self.lblTitoloMenu.grid(row=1, column=1, sticky="nesw")

        spazioTraTitoloEScelte=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 30)).grid(row=2, column=1)

        self.btnGioca=tk.Button(self.frameMenu, text="Gioca", command=lambda:self.Gioca(), bg=self.menu_widget_bg_color, fg=self.menu_widget_fg_color, font=("Helvetica", 30))
        self.btnGioca.grid(row=3, column=1, sticky="nesw")

        spazioTraScelte=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 20)).grid(row=4, column=1)

        self.btnImpostazioni=tk.Button(self.frameMenu, text="Impostazioni", command=lambda:self.Impostazioni(), font=("Helvetica", 30), fg=self.menu_widget_fg_color, bg=self.menu_widget_bg_color)
        self.btnImpostazioni.grid(row=5, column=1, sticky="nesw")

        spazioTraScelte1=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 20)).grid(row=6, column=1)

        self.btnEsci=tk.Button(self.frameMenu, text="Esci", command=lambda: self.quit(), fg=self.menu_widget_fg_color, bg=self.menu_widget_bg_color, font=("Helvetica", 30))
        self.btnEsci.grid(row=7, column=1)

        spazioTraScelteEBottom=tk.Label(self.frameMenu, bg=self.menu_sfondo_bg_color, font=("Helvetica", 30)).grid(row=8, column=1)
        
        

        #GIOCO *******************************************************************************************************

        self.frameGioco = tk.Frame(self, bg=self.gioco_sfondo_bg_color)
        self.frameSchedine = tk.Frame(self.frameGioco, bg=self.gioco_sfondo_bg_color)

        margineAltoDx=tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color, width=14).grid(row=0, column=0)
        btnTornaAlMenu=tk.Button(self.frameGioco, text="<--", bg=self.gioco_sfondo_bg_color, fg=self.gioco_widget_fg_color, font=("Helvetica", 30), bd=0, command=lambda:self.Menu(), relief="solid").grid(row=1, column=0, sticky="e")

        self.lblGiocatore = tk.Label(self.frameGioco, text="Giocatore " + str(self.currentPlayer), fg=self.gioco_widget_fg_color, bg=self.gioco_sfondo_bg_color, font=('Helvetica', 50))
        self.lblGiocatore.grid(row=1, column=2, columnspan=2, sticky="nesw")

        tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color).grid(row=2, column=0)

        self.lblNEstratto1=tk.Label(self.frameGioco, text="N Estratto: ", bg=self.gioco_sfondo_bg_color, fg=self.gioco_widget_fg_color)
        self.lblNEstratto1.grid(row=3, column=2, sticky="e")
        self.lblNEstratto2=tk.Label(self.frameGioco, text="", fg=self.gioco_widget_fg_color, bg=self.gioco_widget_bg_color, width=5, height=2, font=('Helvetica', 15))
        self.lblNEstratto2.grid(row=3, column=3, sticky="w")

        tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color, height=2).grid(row=4, column=0)

        # Tabellone
        frameTabellone=tk.Frame(self.frameGioco, bg=self.gioco_sfondo_bg_color)
        self.arrTabellone=[]
        row=0
        column=0
        for i in range(90):
            column=column+1
            if i+1 == 46:
                row=1
                column=0
            lbl=tk.Label(frameTabellone, text=i+1, bg=self.gioco_sfondo_bg_color, fg=self.gioco_widget_fg_color)
            lbl.grid(row=row, column=column, sticky="nesw")
            tupla1 = (lbl, i+1)
            self.arrTabellone.append(tupla1)
        frameTabellone.grid(row=4, column=1, columnspan=4)

        # Schedina
        self.arrSchedine=[]
        nSchedine=6
        h=0
        for y in range(nSchedine * 2):
            h=h+1
            if (y % 2) == 0:
                arrSchedina = []
                frameSchedina=tk.Frame(self.frameSchedine)
                l=0
                arrNEstrattiSchedina=[]
                for i in range(15):
                    l=l+1
                    randNSchedina=random.randint(1, 90)
                    while arrNEstrattiSchedina.count(randNSchedina) < 0:
                        randNSchedina=random.randint(1, 90)
                    arrNEstrattiSchedina.append(randNSchedina)
                    btn = tk.Button(frameSchedina, text=randNSchedina, fg=self.gioco_widget_fg_color, bg=self.gioco_widget_bg_color, font=('Helvetica', 25, 'bold'))
                    if i+1 <= 5:
                        btn.grid(row=0, column=l, sticky="nesw")
                        if i+1 == 5:
                            l=0
                    elif i+1 > 5 and i+1 <= 10:
                        btn.grid(row=1, column=l, sticky="nesw")
                        if i+1 == 10:
                            l=0
                    elif i+1 > 10 and i+1 <= 15:
                        btn.grid(row=2, column=l, sticky="nesw")
                        if i+1 == 15:
                            l=0
                    arrSchedina.append(btn)
                self.arrSchedine.append(arrSchedina)
            else:
                tk.Label(self.frameSchedine, text="  ", font=("Helvetica", 2), bg=self.gioco_sfondo_bg_color).grid(row=1, column=h+1)
            if y+1 <= 6:
                frameSchedina.grid(row=0, column=h)
                if y+1 == 6:
                    h=0
            elif y+1 > 6 and y+1 <=12:
                frameSchedina.grid(row=2, column=h)
                if y+1 == 12:
                    h=0

        self.arrSchedine[0][0].configure(command=lambda: self.click(0, 0))
        self.arrSchedine[1][0].configure(command=lambda: self.click(1, 0))
        self.arrSchedine[2][0].configure(command=lambda: self.click(2, 0))
        self.arrSchedine[3][0].configure(command=lambda: self.click(3, 0))
        self.arrSchedine[4][0].configure(command=lambda: self.click(4, 0))
        self.arrSchedine[5][0].configure(command=lambda: self.click(5, 0))
        self.arrSchedine[0][1].configure(command=lambda: self.click(0, 1))
        self.arrSchedine[1][1].configure(command=lambda: self.click(1, 1))
        self.arrSchedine[2][1].configure(command=lambda: self.click(2, 1))
        self.arrSchedine[3][1].configure(command=lambda: self.click(3, 1))
        self.arrSchedine[4][1].configure(command=lambda: self.click(4, 1))
        self.arrSchedine[5][1].configure(command=lambda: self.click(5, 1))
        self.arrSchedine[0][2].configure(command=lambda: self.click(0, 2))
        self.arrSchedine[1][2].configure(command=lambda: self.click(1, 2))
        self.arrSchedine[2][2].configure(command=lambda: self.click(2, 2))
        self.arrSchedine[3][2].configure(command=lambda: self.click(3, 2))
        self.arrSchedine[4][2].configure(command=lambda: self.click(4, 2))
        self.arrSchedine[5][2].configure(command=lambda: self.click(5, 2))
        self.arrSchedine[0][3].configure(command=lambda: self.click(0, 3))
        self.arrSchedine[1][3].configure(command=lambda: self.click(1, 3))
        self.arrSchedine[2][3].configure(command=lambda: self.click(2, 3))
        self.arrSchedine[3][3].configure(command=lambda: self.click(3, 3))
        self.arrSchedine[4][3].configure(command=lambda: self.click(4, 3))
        self.arrSchedine[5][3].configure(command=lambda: self.click(5, 3))
        self.arrSchedine[0][4].configure(command=lambda: self.click(0, 4))
        self.arrSchedine[1][4].configure(command=lambda: self.click(1, 4))
        self.arrSchedine[2][4].configure(command=lambda: self.click(2, 4))
        self.arrSchedine[3][4].configure(command=lambda: self.click(3, 4))
        self.arrSchedine[4][4].configure(command=lambda: self.click(4, 4))
        self.arrSchedine[5][4].configure(command=lambda: self.click(5, 4))
        self.arrSchedine[0][5].configure(command=lambda: self.click(0, 5))
        self.arrSchedine[1][5].configure(command=lambda: self.click(1, 5))
        self.arrSchedine[2][5].configure(command=lambda: self.click(2, 5))
        self.arrSchedine[3][5].configure(command=lambda: self.click(3, 5))
        self.arrSchedine[4][5].configure(command=lambda: self.click(4, 5))
        self.arrSchedine[5][5].configure(command=lambda: self.click(5, 5))
        self.arrSchedine[0][6].configure(command=lambda: self.click(0, 6))
        self.arrSchedine[1][6].configure(command=lambda: self.click(1, 6))
        self.arrSchedine[2][6].configure(command=lambda: self.click(2, 6))
        self.arrSchedine[3][6].configure(command=lambda: self.click(3, 6))
        self.arrSchedine[4][6].configure(command=lambda: self.click(4, 6))
        self.arrSchedine[5][6].configure(command=lambda: self.click(5, 6))
        self.arrSchedine[0][7].configure(command=lambda: self.click(0, 7))
        self.arrSchedine[1][7].configure(command=lambda: self.click(1, 7))
        self.arrSchedine[2][7].configure(command=lambda: self.click(2, 7))
        self.arrSchedine[3][7].configure(command=lambda: self.click(3, 7))
        self.arrSchedine[4][7].configure(command=lambda: self.click(4, 7))
        self.arrSchedine[5][7].configure(command=lambda: self.click(5, 7))
        self.arrSchedine[0][8].configure(command=lambda: self.click(0, 8))
        self.arrSchedine[1][8].configure(command=lambda: self.click(1, 8))
        self.arrSchedine[2][8].configure(command=lambda: self.click(2, 8))
        self.arrSchedine[3][8].configure(command=lambda: self.click(3, 8))
        self.arrSchedine[4][8].configure(command=lambda: self.click(4, 8))
        self.arrSchedine[5][8].configure(command=lambda: self.click(5, 8))
        self.arrSchedine[0][9].configure(command=lambda: self.click(0, 9))
        self.arrSchedine[1][9].configure(command=lambda: self.click(1, 9))
        self.arrSchedine[2][9].configure(command=lambda: self.click(2, 9))
        self.arrSchedine[3][9].configure(command=lambda: self.click(3, 9))
        self.arrSchedine[4][9].configure(command=lambda: self.click(4, 9))
        self.arrSchedine[5][9].configure(command=lambda: self.click(5, 9))
        self.arrSchedine[0][10].configure(command=lambda: self.click(0, 10))
        self.arrSchedine[1][10].configure(command=lambda: self.click(1, 10))
        self.arrSchedine[2][10].configure(command=lambda: self.click(2, 10))
        self.arrSchedine[3][10].configure(command=lambda: self.click(3, 10))
        self.arrSchedine[4][10].configure(command=lambda: self.click(4, 10))
        self.arrSchedine[5][10].configure(command=lambda: self.click(5, 10))
        self.arrSchedine[0][11].configure(command=lambda: self.click(0, 11))
        self.arrSchedine[1][11].configure(command=lambda: self.click(1, 11))
        self.arrSchedine[2][11].configure(command=lambda: self.click(2, 11))
        self.arrSchedine[3][11].configure(command=lambda: self.click(3, 11))
        self.arrSchedine[4][11].configure(command=lambda: self.click(4, 11))
        self.arrSchedine[5][11].configure(command=lambda: self.click(5, 11))
        self.arrSchedine[0][12].configure(command=lambda: self.click(0, 12))
        self.arrSchedine[1][12].configure(command=lambda: self.click(1, 12))
        self.arrSchedine[2][12].configure(command=lambda: self.click(2, 12))
        self.arrSchedine[3][12].configure(command=lambda: self.click(3, 12))
        self.arrSchedine[4][12].configure(command=lambda: self.click(4, 12))
        self.arrSchedine[5][12].configure(command=lambda: self.click(5, 12))
        self.arrSchedine[0][13].configure(command=lambda: self.click(0, 13))
        self.arrSchedine[1][13].configure(command=lambda: self.click(1, 13))
        self.arrSchedine[2][13].configure(command=lambda: self.click(2, 13))
        self.arrSchedine[3][13].configure(command=lambda: self.click(3, 13))
        self.arrSchedine[4][13].configure(command=lambda: self.click(4, 13))
        self.arrSchedine[5][13].configure(command=lambda: self.click(5, 13))
        self.arrSchedine[0][14].configure(command=lambda: self.click(0, 14))
        self.arrSchedine[1][14].configure(command=lambda: self.click(1, 14))
        self.arrSchedine[2][14].configure(command=lambda: self.click(2, 14))
        self.arrSchedine[3][14].configure(command=lambda: self.click(3, 14))
        self.arrSchedine[4][14].configure(command=lambda: self.click(4, 14))
        self.arrSchedine[5][14].configure(command=lambda: self.click(5, 14))


        tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color, height=2).grid(row=9, column=0)

        self.btnFinito=tk.Button(self.frameGioco, command=lambda:self.nextTurn(), text="Prossimo Giocatore", bg=self.gioco_widget_bg_color, fg=self.gioco_widget_fg_color)
        self.btnFinito.grid(row=10, column=2, columnspan=2, sticky="nesw")

        tk.Label(self.frameGioco, text="", bg=self.gioco_sfondo_bg_color, width=14, height=6).grid(row=11, column=6)

        self.frameSchedine.grid(row=6, column=1, columnspan=4, rowspan=3)



        #IMPOSTAZIONI *************************************************************************************************
        
        self.frameImpostazioni=tk.Frame(self, bg=self.impostazioni_sfondo_bg_color)

        margineAltoSx = tk.Label(self.frameImpostazioni, width="20", bg=self.impostazioni_sfondo_bg_color).grid(row=0, column=0)
        margineAltoDx = tk.Label(self.frameImpostazioni, width="20", bg=self.impostazioni_sfondo_bg_color).grid(row=0, column=4)

        spazioTraTitoloETop = tk.Label(self.frameImpostazioni, bg=self.impostazioni_sfondo_bg_color, font=("Helvetica", 30)).grid(row=0, column=2)

        btnTornaAlMenu=tk.Button(self.frameImpostazioni, text="<--", bg=self.impostazioni_sfondo_bg_color, fg=self.impostazioni_widget_fg_color, font=("Helvetica", 30), bd=0, command=lambda:self.indietro(), relief="solid").grid(row=1, column=0)

        self.lblTitoloImpostazioni = tk.Label(self.frameImpostazioni, text="Impostazioni", fg=self.impostazioni_widget_fg_color, bg=self.impostazioni_sfondo_bg_color, font=('Helvetica', 50))
        self.lblTitoloImpostazioni.grid(row=1, column=1, columnspan=3, sticky="nesw")

        spazioTraTitoloEScelte = tk.Label(self.frameImpostazioni, font=("Helvetica", 30), bg=self.impostazioni_sfondo_bg_color).grid(row=2, column=2)

        self.lblNGiocatori = tk.Label(self.frameImpostazioni, text="N Giocatori", fg=self.impostazioni_widget_fg_color, bg=self.impostazioni_sfondo_bg_color, font=("Helvetica", 30))
        self.lblNGiocatori.grid(row=3, column=1, columnspan=2, sticky="w")

        self.spnNGiocatori = tk.OptionMenu(self.frameImpostazioni, self.nGiocatori, "2","3","4","5","6","7","8","9","10")
        self.spnNGiocatori.configure(bg=self.impostazioni_widget_bg_color, fg=self.impostazioni_widget_fg_color, font=("Helvetica", 20), width=5)
        self.spnNGiocatori.grid(row=3, column=2, columnspan=2, sticky="e")

        spazioTraScelte1 = tk.Label(self.frameImpostazioni, font=("Helvetica", 20), bg=self.impostazioni_sfondo_bg_color).grid(row=4, column=2)

        self.lblNSchedine = tk.Label(self.frameImpostazioni, text="N Schedine", fg=self.impostazioni_widget_fg_color, bg=self.impostazioni_sfondo_bg_color, font=("Helvetica", 30))
        self.lblNSchedine.grid(row=5, column=1, columnspan=2, sticky="w")

        self.spnNSchedine = tk.OptionMenu(self.frameImpostazioni, self.nSchedine, "1", "2", "3", "4", "5", "6")
        self.spnNSchedine.configure(bg=self.impostazioni_widget_bg_color, fg=self.impostazioni_widget_fg_color, font=("Helvetica", 20), width=5)
        self.spnNSchedine.grid(row=5, column=2, columnspan=2, sticky="e")

        spazioTraScelte2 = tk.Label(self.frameImpostazioni, font=("Helvetica", 20), bg=self.impostazioni_sfondo_bg_color).grid(row=6, column=2)

        frameTema=tk.Frame(self.frameImpostazioni, bg=self.impostazioni_widget_bg_color)

        lblTema = tk.Label(frameTema, text="Tema", font=("Helvetica", 30), fg=self.impostazioni_widget_fg_color, bg=self.impostazioni_sfondo_bg_color).grid(row=0, column=0)

        spazioTraScelteTema=tk.Label(frameTema, text=" ", bg=self.impostazioni_sfondo_bg_color, width="15").grid(row=0, column=1, sticky="nesw")

        self.rbtnTema1 = tk.Radiobutton(frameTema, text="Colorato", variable=self.tema, fg=self.impostazioni_widget_fg_color, value="Normale", bg=self.impostazioni_widget_bg_color).grid(row=0, column=2)
        self.rbtnTema2 = tk.Radiobutton(frameTema, text="Scuro", variable=self.tema, fg=self.impostazioni_widget_fg_color, value="Scuro", bg=self.impostazioni_widget_bg_color).grid(row=0, column=3)

        frameTema.grid(row=7, column=1, columnspan=3, sticky="nesw")

        spazioTraScelte1 = tk.Label(self.frameImpostazioni, font=("Helvetica", 20), bg=self.impostazioni_sfondo_bg_color).grid(row=8, column=2)

        self.btnSalva = tk.Button(self.frameImpostazioni, text="Salva", command=lambda: self.Menu(), fg=self.impostazioni_widget_fg_color, bg=self.impostazioni_widget_bg_color, font=("Helvetica", 30))
        self.btnSalva.grid(row=9, column=1, columnspan=3)

        spazioTraScelteEBottom = tk.Label(self.frameImpostazioni, font=("Helvetica", 30), bg=self.impostazioni_sfondo_bg_color).grid(row=10, column=1)


    def estrai(self):
        #Estrae i numeri casuali della partita
        randN=random.randint(1, 91)
        if self.nEstratti == []:
            self.lblNEstratto2.configure(text=randN)
            self.nEstratti.append(randN)
            
            # Tabellone
            for i in range(len(self.arrTabellone)):
                if self.arrTabellone[i][1] == randN:
                    self.arrTabellone[i][0].configure(bg=self.gioco_widget_bg_color)
            print(randN)
        elif self.nEstratti.count(randN) > 0:
            self.estrai()
        else:
            self.lblNEstratto2.configure(text=randN)
            self.nEstratti.append(randN)
            
            # Tabellone
            for i in range(len(self.arrTabellone)):
                if self.arrTabellone[i][1] == randN:
                    self.arrTabellone[i][0].configure(bg=self.gioco_widget_bg_color)
            print(randN)

    def globals(self):
        # Setto le variabili "globali"
        self.nEstratti=[]
        self.currentPlayer=1
        self.nGiocatori=tk.IntVar(self, 2)
        self.nSchedine=tk.IntVar(self, 1)
        self.tema=tk.StringVar(self, "Normale")

    def Menu(self):
        # Verifica quale tema si ha selezionato\
        # e porta in primo piano il Menu 
        self.frameGioco.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameMenu.grid_forget()
        if self.tema.get() == "Scuro":
            self.menu_sfondo_bg_color="black"
            self.menu_widget_bg_color="gray"
            self.menu_widget_fg_color="white"

            self.gioco_sfondo_bg_color = "black"
            self.gioco_widget_bg_color = "gray"
            self.gioco_widget_fg_color = "white"

            self.impostazioni_sfondo_bg_color = "black"
            self.impostazioni_widget_bg_color = "gray"
            self.impostazioni_widget_fg_color = "white"
            self.CreateWidgets()
            self.frameGioco.grid_forget()
            self.frameImpostazioni.grid_forget()
            self.frameMenu.grid_forget()
        elif self.tema.get() == "Normale":
            self.menu_sfondo_bg_color = "orange"
            self.menu_widget_bg_color = "orange"
            self.menu_widget_fg_color = "black"

            self.gioco_sfondo_bg_color = "red"
            self.gioco_widget_bg_color = "yellow"
            self.gioco_widget_fg_color = "black"

            self.impostazioni_sfondo_bg_color = "#0040ff"
            self.impostazioni_widget_bg_color = "#0080ff"
            self.impostazioni_widget_fg_color = "black"
            self.CreateWidgets()
            self.frameGioco.grid_forget()
            self.frameImpostazioni.grid_forget()
            self.frameMenu.grid_forget()

        self.frameGioco.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameMenu.grid()

    def Gioca(self):
        # Porta in primo piano la schermata del gioco
        self.estrai()
        self.frameMenu.grid_forget()
        self.frameImpostazioni.grid_forget()
        self.frameGioco.grid()

    def nextTurn(self):
        # Cambia giocatore e cambia il turno
        curPlyr = self.currentPlayer + 1
        if curPlyr <= self.nGiocatori.get():
            self.currentPlayer = self.currentPlayer + 1
            self.lblGiocatore.configure(text="Giocatore "+str(self.currentPlayer))
            if curPlyr == self.nGiocatori.get():
                self.btnFinito.configure(text="Fine Turno")
            else:
                self.btnFinito.configure(text="Prossimo Giocatore")
        else:
            self.currentPlayer = 0
            self.estrai()
            self.nextTurn()

    def Impostazioni(self):
        # Porta in primo piano la schermata delle Impostazioni
        self.frameMenu.grid_forget()
        self.frameGioco.grid_forget()
        self.frameImpostazioni.grid()
        self.oldNGiocatori=self.nGiocatori.get()
        self.oldNSchedine=self.nSchedine.get()
        self.oldTema=self.tema.get()

    def indietro(self):
        # Se non si salvano le impostazioni selezionate 
        # non le aggiorna nelle variabili globali
        self.nGiocatori.set(self.oldNGiocatori)
        self.nSchedine.set(self.oldNSchedine)
        self.tema.set(self.oldTema)
        self.Menu()

    def click(self, nScheda, nCella):
        # Segna i numeri cliccati nelle schedine
        if self.arrSchedine[nScheda][nCella].cget("bg") == self.gioco_widget_bg_color:
            self.arrSchedine[nScheda][nCella].configure(bg=self.gioco_sfondo_bg_color)
            self.arrSchedine[nScheda][nCella].configure(fg=self.gioco_widget_fg_color)
        else:
            self.arrSchedine[nScheda][nCella].configure(bg=self.gioco_widget_bg_color)
            self.arrSchedine[nScheda][nCella].configure(fg=self.gioco_widget_fg_color)


root = Tombolone()

root.mainloop()
