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
        #Label (Text) erstellen 
        w = QLabel(self)
        w.setText("<b>TEXT</b>")
        w.move(50,100)
        w = QLabel(self)
        w.setText("Geben Sie Ihre PLZ an")
        w.move (50,150)
        #Line Edit -PLZ eingeben
        self.w =QLineEdit(self)
        self.w.move(50,200)

        #Einleitungssatz Wochentag wählen
        w = QLabel(self)
        w.setText("Wählen Sie den gewünschten Wochentag")
        w.move (50,250)
        #Wochentage aufzählen und auswählen Button 
        Montag = QPushButton("Montag", self)
        Montag.move(50,300)
        Montag.clicked.connect(self.gedrueckt)
        Dienstag = QPushButton("Dienstag", self)
        Dienstag.move(150,300)
        Dienstag.clicked.connect(self.gedrueckt)
        Mittwoch = QPushButton("Mittwoch", self)
        Mittwoch.move(250,300)
        Mittwoch.clicked.connect(self.gedrueckt)
        Donnerstag = QPushButton("Donnerstag", self)
        Donnerstag.move(350,300)
        Donnerstag.clicked.connect(self.gedrueckt)
        Freitag = QPushButton("Freitag", self)
        Freitag.move(450,300)
        Freitag.clicked.connect(self.gedrueckt)
        Samstag = QPushButton("Samstag", self)
        Samstag.move(550,300)
        Samstag.clicked.connect(self.gedrueckt)
        Sonntag = QPushButton("Sonntag", self)
        Sonntag.move(650,300)
        Sonntag.clicked.connect(self.gedrueckt)

        #ToolTip und Absende- Button erstellen 
        QToolTip.setFont(QFont("Arial", 8))
        senden = QPushButton("Absenden", self)
        senden.move(50,380)
        senden.setToolTip("Drücken Sie hier, um die <b>Anfrage</b> zu versenden")
        senden.clicked.connect(self.gedrueckt)

        #Einleitungstext Audioaufnahme
        w = QLabel(self)
        w.setText("<b>AUDIO</b>")
        w.move(50,650)
        w = QLabel(self)
        w.setText("Starten Sie die Aufnahme")
        w.move (50,700)

        #Audioaufnahme 
        Audiobutton = QPushButton("Audioaufnahme starten", self)
        Audiobutton.move(50,750)
        Audiobutton.pressed.connect(self.aufgenommen)
        Audiobutton.released.connect(self.abgeschickt)

        Wetter = QPushButton("Audioantwort abhoeren",self)
        Wetter.move(200,750)
        Wetter.clicked.connect(self.abhoeren)

        #Toolbar erstellen
        self.statusBar(). showMessage("Wir zeigen Ihnen das Wetter von Heute und der nächsten 7 Tage")

        #Menubar erstellen 
        menubar = self.menuBar()
        audio = menubar.addMenu("&Audioabfrage")
        text = menubar.addMenu("&Textsuche")

        #Fenster anzeigen_TitelSetzen
        self.show()
        self.setGeometry(50,50,1000,1000)
        self.setWindowTitle("Wetterapplikation")
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


w= Fenster()
#App beenden
sys.exit(app.exec_())

Backlog
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