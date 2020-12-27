'''
Author: geekli
Date: 2020-12-27 10:28:25
LastEditTime: 2020-12-27 10:30:57
LastEditors: your name
Description: 
FilePath: \pythonQT\ch01\HW_setText_html.py
'''
import sys
from PyQt5.QtWidgets import QApplication, QLabel


if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color="red">Hello</font> <h1>World</h1>')
    
    label.setText('<font color="red">Hello</font> <h1>World</h1>')
    label.show()
    sys.exit(app.exec_())

################################################################
#   label = QLabel()
#
#   label.setText('<font color="red">Hello</font> <h1>World</h1>')
################################################################