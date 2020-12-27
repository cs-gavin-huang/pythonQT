'''
Author: geekli
Date: 2020-12-27 10:33:59
LastEditTime: 2020-12-27 10:36:52
LastEditors: your name
Description: 
FilePath: \pythonQT\ch02\button_setText.py
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):                                            # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)                # 2
        self.button.clicked.connect(self.change_text)           # 3

    def change_text(self):
        print('change text')
        self.button.setText('Stop')                             # 4
        # disconnect
        self.button.clicked.disconnect(self.change_text)        # 5


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()                                               # 6
    demo.show()                                                 # 7
    sys.exit(app.exec_())