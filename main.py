from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import randint


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Paint point example')
        self.point = None
    def mousePressEvent(self, event):
        self.point = event.pos()

        # Вызов перерисовки виджета
        self.update()

    def mouseReleaseEvent(self, event):
        self.point = None

    def paintEvent(self, event):
        super().paintEvent(event)

        # Если нет
        if not self.point:
            return

        # Рисовать будем на самом себе
        painter = QPainter(self)

        # Для рисования точки хватит setPen, но для других фигур (типо rect) понадобится setBrush
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(*[randint(0, 255) for i in range(3)]))
        painter.setPen(pen)
        # Рисование точки
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        painter.drawEllipse(x, y, w, w)


if __name__ == '__main__':
    app = QApplication([])
    w = Widget()
    w.show()
    app.exec()