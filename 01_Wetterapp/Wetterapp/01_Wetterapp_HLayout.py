#Setting Up
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon, QKeyEvent
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QToolTip
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
app = QApplication (sys.argv)

#Fenster bauen 
w = QWidget()
#Fenster anzeigen_TitelSetzen
w.show()
w.setGeometry(50,50,1000,1000)
w.setWindowTitle("Wetterapplikation")
w.setWindowIcon(QIcon("wetter.png"))#Icon funktioniert noch nicht

#Button erstellen (Objektorientiert)
class Fenster (QMainWindow): 
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        #Toolbar erstellen
        self.statusBar(). showMessage("Wir zeigen Ihnen das Wetter von Heute und der nächsten 7 Tage")

        #Menubar erstellen 
        menubar = self.menuBar()
        audio = menubar.addMenu("&Audioabfrage")
        text = menubar.addMenu("&Textsuche")

        #ToolTip erstellen 
        QToolTip.setFont(QFont("Arial", 8))
        #Boxlayout horizontal einstellen 
        h = QHBoxLayout()
        #Abstand einfügen, damit nicht der gesamte Platz gebraucht wird 
        h.addWidget(zurueck)
        h.addStretch(1)
        h.addWidget(senden)
        #Boxlaout vertikal einstellen 
        v= QVBoxLayout()
        v.addStretch(1)
        v.addLayout(h)
        senden = QPushButton("Anfrage absenden")
        senden.setToolTip("Drücken Sie hier, um die <b>Anfrage</b> zu versenden")
        senden.clicked.connect(self.gedrueckt)
        zurueck = QPushButton("Zurück")
        zurueck.setToolTip("Drücken Sie hier, um <b>einen Schritt</b> zurück zu gehen")
        zurueck.clicked.connect(self.gedrueckt)
        
        #Combobox
        self = QComboBox(self)
        self.move(80,50)
        self.addItem("Montag")
        self.addItem("Dienstag")
        self.addItem ("Mittwoch")
        self.toggeled.connect(self.gedrueckt)

        #Wochentage einfügen /funktioniert nicht! 
        w = QCheckBox ("Montag", self)
        w.move(60,50)
        w.stateChanged.connect(self.gedrueckt)


        #Fenster anzeigen_TitelSetzen
        self.setLayout (v)
        self.show()
        self.setGeometry(50,50,1000,1000)
        self.setWindowTitle("Wetterapplikation")
        self.setWindowIcon(QIcon("wetter.png"))#Icon funktioniert noch nicht

    def gedrueckt(self):
        print("Button getätigt")
    
    #Benutzerdefinierter Event erstellen - GUI beenden wenn w gedrückt wird. 
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_W:
            self.close()

#weiteres Fenster öffenen 






w= Fenster()
#App beenden
sys.exit(app.exec_())