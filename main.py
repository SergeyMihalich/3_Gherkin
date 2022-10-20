from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

'' 'Pyqt5 динамически добавляет и удаляет элементы управления' ''


class DynAddObject(QDialog):
    i = 1
    def __init__(self, parent=None):
        super(DynAddObject, self).__init__(parent)
        self.widgetList = []
        addButton = QPushButton(u"Добавить контрол")
        delAllBUtton = QPushButton(u"Снять все")
        delOneBUtton = QPushButton(u"Снять один")
        self.layout = QGridLayout()
        self.layout.addWidget(addButton, 1, 0)
        self.layout.addWidget(delAllBUtton, 2, 0)
        self.layout.addWidget(delOneBUtton, 3, 0)
        self.setLayout(self.layout)
        addButton.clicked.connect(self.add)
        delAllBUtton.clicked.connect(self.deleteAll)
        delOneBUtton.clicked.connect(self.deleteOne)

    def add(self):
        self.combo = QComboBox(self)
        self.combo.addItems(["Ubuntu", "Mandriva",
                        "Fedora", "Arch", "Gentoo"])
        btncont = self.layout.count()
        widget = QPushButton(str(btncont - 1), self)
        self.layout.addWidget(self.combo)

    def deleteOne(self):
        i = self.layout.count()-1
        if(i>2):self.layout.itemAt(i).widget().deleteLater()
        self.tim()

    def deleteAll(self):
        for i in range(self.layout.count())[3:]:
            self.layout.itemAt(i).widget().deleteLater()
            self.tim()

    def tim(self):
        # Здесь устанавливается таймер
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.resize(self.sizeHint()))
        self.timer.start(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DynAddObject()
    form.show()
    app.exec_()