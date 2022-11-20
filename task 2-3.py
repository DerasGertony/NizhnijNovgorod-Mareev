import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import randint as ri

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(00, 00, 300, 300)
        self.setWindowTitle('')
        self.make = False
        btn = QPushButton('Кнопка', self)
        btn.move(100, 0)
        btn.clicked.connect(self.do)
        self.circ = []

    def do(self):
        self.make = True
        self.repaint()

    def paintEvent(self, event):
        if self.make:
            qp = QPainter()
            qp.begin(self)
            self.draw_circ(qp)
            qp.end()
            self.make = False

    def draw_circ(self, qp):
        if self.circ:
            for i in self.circ:
                qp.setBrush(QColor(i[0][0], i[0][1], i[0][2]))
                qp.drawEllipse(i[1], i[2], i[3], i[3])
        r, g, b = ri(0, 255), ri(0, 255), ri(0, 255)
        a, b, r = ri(0, 300), ri(0, 300), ri(0, 100)
        self.circ.append([(r,g,b), a, b, r])
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(a, b, r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
