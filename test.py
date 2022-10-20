from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox, QComboBox, QListWidget, QHBoxLayout, QListWidgetItem, QTableWidgetItem
from PyQt5 import QtWidgets, uic
import sys
from PyQt5 import QtCore
import const

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mydesign.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.button.clicked.connect(self.createTable)
        self.button2 = self.findChild(QtWidgets.QPushButton, 'deleteOne')
        self.button2.clicked.connect(self.deleteOneCol)

        self.tableWidget.setRowCount(4)

        #self.tableWidget.setColumnCount(7)

        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)
        self.myListWidget2.setDefaultDropAction(Qt.MoveAction)
        self.myListWidget2.installEventFilter(self)

        for i in const.STEP:
            self.myListWidget1.insertItem(1, QListWidgetItem(i))

        self.show()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.ContextMenu and source is self.myListWidget2:
            menu = QtWidgets.QMenu()
            menu.addAction('Delete')
            if menu.exec_(event.globalPos()):
                item = source.indexAt(event.pos()).row()
                removed = self.myListWidget2.takeItem(item)
                print(removed)
            return True
        return super(Ui, self).eventFilter(source, event)

    def createTable(self):
        comboBox = QComboBox()
        comboBox.addItems(const.VARIABLE_TYPES)
        columnCount = self.tableWidget.columnCount()
        self.tableWidget.insertColumn(columnCount)
        self.tableWidget.setCellWidget(0, columnCount, QCheckBox())
        self.tableWidget.setItem(1, columnCount, QTableWidgetItem("column_"+str(columnCount+1)))
        self.tableWidget.setCellWidget(2, columnCount, comboBox)
        self.tableWidget.setCellWidget(3, columnCount, QCheckBox())
        self.save()

    def deleteOneCol(self):
        i = self.tableWidget.columnCount()-1
        if(i>0):self.tableWidget.removeColumn(i)
        print(i)

    def save(self):
        data = []
        for row in range(self.tableWidget.rowCount()):
            rowdata = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                widget = self.tableWidget.cellWidget(row, column)
                if item is not None: rowdata.append(item.text())
                elif isinstance(widget, QCheckBox): rowdata.append(widget.isChecked())
                elif isinstance(widget, QComboBox): rowdata.append(widget.currentText())
                else: rowdata.append("")
            data.append(rowdata)
        all_items = [str(self.myListWidget2.item(i).text()) for i in range(self.myListWidget2.count())]
        print(all_items)
        print(data)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
