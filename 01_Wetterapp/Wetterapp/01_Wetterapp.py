#Setting Up
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon, QKeyEvent
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QToolTip, QLabel, QLineEdit, QGridLayout, QComboBox


# w.setGeometry(50,50,1000,1000)



#Button erstellen (Objektorientiert)
class Fenster (QWidget): 
    def __init__(self):
        super().__init__()
        self.initMe()
        self.setWindowTitle("Wetterapplikation")
        self.setWindowIcon(QIcon("wetter.png"))#Icon funktioniert noch nicht
        self.show()

    def initMe(self):
        #Layout aufsetzen
        grid = QGridLayout()
        self.setLayout(grid)

        #Label (Text) erstellen 
        text = QLabel(self)
        text.setText("<b>TEXT</b>")
        grid.addWidget(text,1,1)
        plz_label = QLabel(self)
        plz_label.setText("Geben Sie die gewünschte PLZ oder Ort an")
        grid.addWidget(plz_label,2,1)
        #Line Edit -PLZ eingeben
        self.plz =QLineEdit(self)
        grid.addWidget(self.plz,3,1)
        # self.plz.adjustSize() # nötig, damit das gesamte Label angezeigt wird
        
        #Einleitungssatz Wochentag wählen
        day = QLabel(self)
        day.setText("Wählen Sie den gewünschten Wochentag")
        grid.addWidget(day,4,1)
        day.adjustSize()
        self.options = QComboBox(self)
        self.options.setObjectName("day")
        self.options.addItem("Heute")
        self.options.addItem("Morgen")
        grid.addWidget(self.options,5,1)

        #ToolTip und Absende- Button erstellen 
        QToolTip.setFont(QFont("Arial", 8))
        senden = QPushButton("Absenden", self)

        grid.addWidget(senden,6,1)
        senden.setToolTip("Drücken Sie hier, um die <b>Anfrage</b> zu versenden")
        senden.clicked.connect(self.gedrueckt)
        senden.adjustSize()

        #Einleitungstext Audioaufnahme
        label = QLabel(self)
        label.setText("<b>AUDIO</b>")
        grid.addWidget(label,1,2)
        label_start = QLabel(self)
        label_start.setText("Starten Sie die Aufnahme")
        grid.addWidget(label_start,2,2)

        #Audioaufnahme 
        Audiobutton = QPushButton("Audioaufnahme starten", self)
        grid.addWidget(Audiobutton,3,2)
        Audiobutton.pressed.connect(self.aufgenommen)
        Audiobutton.released.connect(self.abgeschickt)

        wetter = QPushButton("Audioantwort abhoeren",self)
        grid.addWidget(wetter,4,2)
        wetter.clicked.connect(self.abhoeren)

    #Brauchen wir nicht, da wir Tabs und Labels nutzen weden (GridLayout funktioniert nicht in Window sondern in Widget)
        # #Toolbar erstellen
        # self.statusBar(). showMessage("Wir zeigen Ihnen das Wetter von Heute und der nächsten 7 Tage")

        # #Menubar erstellen 
        # menubar = self.menuBar()
        # audio = menubar.addMenu("&Audioabfrage")
        # text = menubar.addMenu("&Textsuche")

        #Fenster anzeigen_TitelSetzen
        # self.show()
        self.setGeometry(50,50,200,200)
        # self.setWindowTitle("Wetterapplikation")
        self.setWindowIcon(QIcon("wetter.png"))#Icon funktioniert noch nicht

    def gedrueckt(self, text):
        print ("Button getätigt")
    
    def aufgenommen(self):
        print("Eine Audioaufnahme wurde hinzugefügt")
    
    def abgeschickt(self):
        print("Audioaufnahme übermittelt")

    def abhoeren(self):
        print("Audioantwort abhören")


    #Benutzerdefinierter Event erstellen - GUI beenden wenn w gedrückt wird. 
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_W:
            self.close()


app = QApplication (sys.argv)
w = Fenster()
#App beenden
sys.exit(app.exec_())

#Backlog
#VERSUCH -Combobox Wochentag auswählen 
        #w = QComboBox(self)
        #w.move(80,50)
        #w.addItem("Montag")
        #w.self.addItem("Dienstag")
        #self.addItem ("Mittwoch")

        #zurueck = QPushButton("Zurück", self)
        #zurueck.move(50,900)
        #zurueck.setToolTip("Drücken Sie hier, um <b>einen Schritt</b> zurück zu gehen")
        #zurueck.clicked.connect(self.gedrueckt)