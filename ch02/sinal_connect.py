'''
Author: geekli
Date: 2020-12-27 10:41:19
LastEditTime: 2020-12-27 10:41:20
LastEditors: your name
Description: 
FilePath: \pythonQT\ch02\sinal_connect.py
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.pressed.connect(self.button.released)  # 1
        self.button.released.connect(self.change_text)     # 2

    def change_text(self):
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())