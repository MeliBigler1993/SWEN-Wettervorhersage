"""
This module defines and sets up the GUI
"""
import sys
from datetime import datetime
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QToolTip, QLabel, QLineEdit, QGridLayout, QComboBox, QTabWidget
from classes.meteo_scraper import MeteoScraper
from classes.speech_rec import Speaker

class Window(QWidget):
    """
    initiates a window application
    """
    def __init__(self):
        super().__init__()
        self.init_me()
        self.setWindowTitle("Wetterapplikation")
        self.setGeometry(50,50,200,200)
        self.show()

    def init_me(self):
        """
        sets the layout. mainly adds a tab widget
        """
        #Set Layout
        grid = QGridLayout()
        self.setLayout(grid)

        #Create Tabs & add to Layout
        tabs = TabWidget(self)
        grid.addWidget(tabs,1,1)

class TabWidget(QWidget):
    """
    initiates a Tabwidget with two tabs called "Text" and "Audio"
    """
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

        #Tab 1: Add Line Edit -PLZ/Location
        self.plz =QLineEdit(self)
        tab1_layout.addWidget(self.plz,2,1)

        #Tab 1: Day Options
        day = QLabel(self)
        day.setText("Wählen Sie den gewünschten Wochentag")
        tab1_layout.addWidget(day,4,1)
        day.adjustSize()
        self.set_day_options()
        tab1_layout.addWidget(self.options,5,1)

        #Tab 1: ToolTip und Send-Button
        QToolTip.setFont(QFont("Arial", 12))
        senden = QPushButton("Absenden", self)
        tab1_layout.addWidget(senden,6,1)
        senden.setToolTip("Drücken Sie hier, um die <b>Anfrage</b> zu versenden")
        senden.clicked.connect(lambda: self.pressed(self.plz.text(), self.options.currentIndex()))

        #Tab 1: Result Display
        self.resultat = QLabel()
        tab1_layout.addWidget(self.resultat,7,1)

        #Setup Tab2 "Audio"
        tab2_layout = QGridLayout()
        self.tab2.setLayout(tab2_layout)
        audio_label = QLabel()
        audio_label.setText("Starten Sie die Aufnahme")
        tab2_layout.addWidget(audio_label,1,1)

        #Tab2: Audio Recording
        rec_button = QPushButton("Audioaufnahme starten", self)
        tab2_layout.addWidget(rec_button,2,1)
        rec_button.clicked.connect(self.record)

        #Tab2: Display Recording
        self.aufnahme = QLabel()
        self.aufnahme.setText("Sie sagten: ")
        tab2_layout.addWidget(self.aufnahme,3,1)

        #Tab2: Listen to Answer
        voice_output = QPushButton("Audioantwort hören",self)
        tab2_layout.addWidget(voice_output,4,1)
        voice_output.clicked.connect(self.listen)

    def set_day_options(self):
        """
        Dynamically creates a dropdown filled with the possible days to select.
        """
        self.options = QComboBox(self)
        self.options.setObjectName("day")
        today = datetime.today()
        weekday = today.weekday()

        weekdays = {
                0: 'Montag',
                1: 'Dienstag',
                2: 'Mittwoch',
                3: 'Donnerstag',
                4: 'Freitag',
                5: 'Samstag',
                6: 'Sonntag',
            }

        for i in range(6):
            if i == 0:
                self.options.addItem("Heute")
            elif i == 1:
                self.options.addItem("Morgen")
            else:
                day = weekday+i
                if day > 6:
                    day = day - 7
                self.options.addItem(weekdays[day])

    def pressed(self, plz, day):
        """
        gets called by button "Absenden". Launches the Scraper and displays the weather for the given PLZ.
        """
        scrape = MeteoScraper()
        self.weather = scrape.find_weather(plz, day)
        self.resultat.setText(self.weather)


    def record(self):
        """
        gets called by button "Aufnehmen". Records what the user says and displays it in the window.
        """
        self.speaker = Speaker()
        self.plz = self.speaker.listen_for_input()
        self.aufnahme.setText("Sie sagten: "+self.plz)

    def listen(self):
        """
        gets called by button "Abhören". Speaks the sentence returned from the WebScraper.
        """
        scrape = MeteoScraper()
        self.weather = scrape.find_weather(self.plz)
        self.speaker.speak(self.weather)


app = QApplication (sys.argv)
w = Window()

#Exit App
sys.exit(app.exec_())
