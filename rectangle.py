from PyQt6.QtCore import QRect, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow , QWidget 
from PyQt6.QtGui import QColor, QPainter, QPen

import sys

class Rectangle(QWidget):
    def __init__(self , parent):
        super().__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.fillRect(10 , 10 , 500 , 100 , QColor("#2E3440"))

        super().paintEvent(event)

class Window(QMainWindow):

    def __init__(self):

        super().__init__()


        self.InitWindow()

    def InitWindow(self):

        shape = Rectangle(self)

        shape.setGeometry(QRect(0 , 0 , 500 , 500))

        self.show()

App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())


