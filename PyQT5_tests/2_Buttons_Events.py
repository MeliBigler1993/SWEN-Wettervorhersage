#Buttons and Events https://www.youtube.com/watch?v=-2uyzAqefyE
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from tests import Test
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My Fist Label")
        self.label.move(20,50) 

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Clickme")
        self.b1.clicked.connect(clicked)

    def clicked (self):
        self.label.setText("you pressed the button")


def clicked():
    print("clicked")
    test = Test()
    zahl = test.add()
    print(zahl)


#Definition of the Application (Fenster einstellen, erste Texte schreiben) 
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 200, 300, 300)
    win.setWindowTitle("Wetterapp")

#Erstes Label integrieren 
    label = QtWidgets.QLabel(win)
    label.setText("My Fist Label")
    label.move(20,50) 

    #integrate Button without funktion (nicht klickbar)
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Clickme")

    #add an event - wir sagen, was passieren soll (hier wird "clicked" in der Console angezeigt)
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()















































































