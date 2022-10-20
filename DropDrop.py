import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from PyQt5.QtCore import Qt

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(1, 5)

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount )

    def _addColumn(self):
        checkBox = QCheckBox()
        comboBox = QComboBox()
        comboBox.addItems(['Мужчина', 'Женщина'])
        columnCount = self.columnCount()
        self.insertColumn(columnCount)
        self.setCellWidget(1, columnCount, checkBox)
        self.setCellWidget(3, columnCount, comboBox)
        try:
            print(self.tableWidget.item(4, 7).text())
        except:
            print('No data')



    def _removeRow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount()-1)
        self.getData()

class AppMain(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 600)

        mainLayout = QHBoxLayout()
        table = TableWidget()
        mainLayout.addWidget(table)
        buttonLayout = QVBoxLayout()

        button_new = QPushButton('New')
        button_new.clicked.connect(table._addRow)
        buttonLayout.addWidget(button_new)

        button_copy = QPushButton('AddColumn')
        button_copy.clicked.connect(table._addColumn)
        buttonLayout.addWidget(button_copy)

        button_save = QPushButton('Save')
        button_save.clicked.connect (self.save())
        buttonLayout.addWidget(button_save)

        button_remove = QPushButton('Remove')
        button_remove.clicked.connect(table._removeRow)
        buttonLayout.addWidget(button_remove, alignment=Qt.AlignTop)

        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)


    def save(self):
        rows = self.table.rowCount()
        cols = self.columnCount()
        print(rows)
        print(cols)
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.tableWidget.item(row, col).text())
                    print(self.tableWidget.item(row, col).text())
                except:
                    tmp.append('No data')
            data.append(tmp)
        print(data)

if __name__ == "__main__":
        app = QApplication(sys.argv)
        form = AppMain()
        form.show()
        sys.exit(app.exec_())