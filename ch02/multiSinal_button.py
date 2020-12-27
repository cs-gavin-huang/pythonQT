'''
Author: geekli
Date: 2020-12-27 10:38:46
LastEditTime: 2020-12-27 10:40:44
LastEditors: your name
Description: 
FilePath: \pythonQT\ch02\multiSinal_button.py
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.pressed.connect(self.change_text)     # 1
        self.button.released.connect(self.change_text)    # 2

    #插槽
    def change_text(self):
        if self.button.text() == 'Start':                 # 3
            self.button.setText('Stop')
        else:
            self.button.setText('Start')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())