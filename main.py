# main.py
import random
import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)

        k = random.randint(0, min(self.width(), self.height()))
        x = random.randint(0, self.width() - k)
        y = random.randint(0, self.width() - k)
        x1 = x + k
        y1 = y + k
        print(x, y, x1, y1)
        item = QGraphicsEllipseItem(x, y, k, k)
        item.setBrush(self.getRandomColor())
        scene.addItem(item)

    def getRandomColor(self):
        return QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())
