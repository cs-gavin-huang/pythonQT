'''
Author: geekli
Date: 2020-12-27 10:25:44
LastEditTime: 2020-12-27 10:26:18
LastEditors: your name
Description: 
FilePath: \pythonQT\ch01\qt1.py
'''
import sys
from PyQt5.QtWidgets import QApplication, QLabel
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 1
    label = QLabel('Hello World') # 2
    label.show() # 3
    sys.exit(app.exec_())# 4