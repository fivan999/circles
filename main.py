from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.paint_button = QtWidgets.QPushButton(Form)
        self.paint_button.setGeometry(QtCore.QRect(154, 270, 81, 23))
        self.paint_button.setObjectName("paint_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Круги"))
        self.paint_button.setText(_translate("Form", "Сделать круг"))


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        colors = [randint(0, 256), randint(0, 256), randint(0, 256)]
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
