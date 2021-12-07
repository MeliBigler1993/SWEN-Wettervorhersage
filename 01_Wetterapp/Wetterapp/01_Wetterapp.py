#Setting Up
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QToolTip, QLabel, QLineEdit, QGridLayout, QComboBox, QTabWidget


# w.setGeometry(50,50,1000,1000)



#Button erstellen (Objektorientiert)
class Fenster (QWidget):
    def __init__(self):
        super().__init__()
        self.init_me()
        self.setWindowTitle("Wetterapplikation")
        self.setWindowIcon(QIcon("./wetter.png"))#Icon funktioniert noch nicht
        self.setGeometry(50,50,200,200)
        self.show()

    def init_me(self):
        #Layout aufsetzen
        grid = QGridLayout()
        self.setLayout(grid)

        #Tabs erstellen und ins Layout einfügen
        tabs = TabWidget(self)
        grid.addWidget(tabs,1,1)

class TabWidget(QWidget):
    def __init__(self,parent):
        super(QWidget,self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1, "Text")
        self.tabs.addTab(self.tab2, "Audio")
        self.layout.addWidget(self.tabs)

        #Setup Tab1 "Text"
        tab1_layout = QGridLayout()
        self.tab1.setLayout(tab1_layout)
        self.plz_label = QLabel()
        self.plz_label.setText("Geben Sie die gewünschte PLZ oder Ort an")
        tab1_layout.addWidget(self.plz_label,1,1)

        #Tab 1: Line Edit -PLZ eingeben
        self.plz =QLineEdit(self)
        tab1_layout.addWidget(self.plz,2,1)

        #Tab 1: Einleitungssatz Wochentag wählen
        day = QLabel(self)
        day.setText("Wählen Sie den gewünschten Wochentag")
        tab1_layout.addWidget(day,4,1)
        day.adjustSize()
        self.options = QComboBox(self)
        self.options.setObjectName("day")
        self.options.addItem("Heute")
        self.options.addItem("Morgen")
        tab1_layout.addWidget(self.options,5,1)

        #Tab 1: ToolTip und Absende- Button erstellen
        QToolTip.setFont(QFont("Arial", 12))
        senden = QPushButton("Absenden", self)
        tab1_layout.addWidget(senden,6,1)
        senden.setToolTip("Drücken Sie hier, um die <b>Anfrage</b> zu versenden")
        senden.clicked.connect(self.gedrueckt)

        #Setup Tab2 "Audio"
        tab2_layout = QGridLayout()
        self.tab2.setLayout(tab2_layout)
        audio_label = QLabel()
        audio_label.setText("Starten Sie die Aufnahme")
        tab2_layout.addWidget(audio_label,1,1)

        #Tab2: Audioaufnahme
        rec_button = QPushButton("Audioaufnahme starten", self)
        tab2_layout.addWidget(rec_button,2,1)
        rec_button.pressed.connect(self.aufgenommen)
        rec_button.released.connect(self.abgeschickt)

        #Tab2: Display Aufnahme
        aufnahme = QLabel()
        aufnahme.setText("Sie sagten: ")
        tab2_layout.addWidget(aufnahme,3,1)

        #Tab2: Antwort hören
        voice_output = QPushButton("Audioantwort abhoeren",self)
        tab2_layout.addWidget(voice_output,4,1)
        voice_output.clicked.connect(self.abhoeren)

    def gedrueckt(self):
        print ("Button getätigt")

    def aufgenommen(self):
        print("Eine Audioaufnahme wurde hinzugefügt")

    def abgeschickt(self):
        print("Audioaufnahme übermittelt")

    def abhoeren(self):
        print("Audioantwort abhören")


app = QApplication (sys.argv)
w = Fenster()
#App beenden
sys.exit(app.exec_())

#Backlog
    #zurueck = QPushButton("Zurück", self)
    #zurueck.move(50,900)
    #zurueck.setToolTip("Drücken Sie hier, um <b>einen Schritt</b> zurück zu gehen")
    #zurueck.clicked.connect(self.gedrueckt)
