import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.need_draw = False

    def run(self):
        self.need_draw = True
        self.size = randint(10, 40)
        self.x = randint(5, 70)
        self.repaint()

    def paintEvent(self, event):
        if self.need_draw:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(self.x, self.x, self.x + self.size, self.x + self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())