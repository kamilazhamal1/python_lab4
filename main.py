#!/usr/bin/env python3
# coding=utf-8
import random
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа с визуальными табличными данными в Python')

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):

        row = 0
        col = 0

        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = random.randrange(-20, 21, 1)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

        list_information_max_num = finder(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены неправильные данные!')
        else:
            self.label_max.setText(
                'Максимальный элемент второй строки: ' + str(list_information_max_num[0]))

    def solve(self):
        list_information_max_num = finder(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены некорректные данные!')
            return
        else:
            self.label_max.setText(
                'Максимальный элемент второй строки: ' + str(list_information_max_num[0]))

        max_num = list_information_max_num[0]
        col_max_number = list_information_max_num[1]

        if max_num <= int(self.tableWidget.item(2, 0).text()):
            self.label_answer.setText(
                "Максимальный элемент второй строки (%d) не больше\n"
                "первого элемента третьей строки %d.\n"
                "Задание не будет выполнено." % (max_num, int(self.tableWidget.item(2, 0).text()))
            )
        else:
            self.label_answer.setText(
                "Максимальный элемент второй строки (%d) больше\n"
                "первого элемента третьей строки %d.\n"
                "Элементы поменялись местами." % (max_num, int(self.tableWidget.item(2, 0).text()))
            )
            self.tableWidget.setItem(1, list_information_max_num[1],
                                     QTableWidgetItem(self.tableWidget.item(2, 0).text()))
            self.tableWidget.setItem(2, 0,
                                     QTableWidgetItem(str(max_num)))

        self.label_error.setText('')


def finder(table_widget):

    col_max_number = 0
    max_num = int(table_widget.item(1, col_max_number).text())

    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if row == 1:
                    if number > max_num:
                        max_num = number
                        col_max_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, col_max_number]
    except Exception:
        return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
