# Import PyQT5 -https://www.youtube.com/watch?v=Vde5SH8e1OQ
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


#Definition of the Application (Fenster einstellen, erste Texte schreiben) 
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Wetterapp")

#Erstes Label integrieren 
    label = QtWidgets.QLabel(win)
    label.setText("My Fist Label")
    label.move(20,50) 


    win.show()
    sys.exit(app.exec_())

window()