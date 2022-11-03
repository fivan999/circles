from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setWindowTitle("Круги")
        self.paint_button.clicked.connect(self.paint)
        self.do_paint = False
        self.qp = QPainter()

    def paintEvent(self, event):
        if self.do_paint:
            self.qp.begin(self)
            self.make_circle()
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def make_circle(self):
        center_y = randint(50, 350)
        center_x = randint(50, 250)
        size = randint(50, 150)
        colors = [255, 237, 0]
        color = QColor(*colors)
        self.qp.setBrush(color)
        self.qp.drawEllipse(center_x - size // 2,
                            center_y - size // 2, size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    window = Window()
    window.show()
    sys.exit(app.exec())
