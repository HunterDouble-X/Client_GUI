import sys

import PyQt5.Qt
from PyQt5 import *








def main():
    app = PyQt5.Qt.QApplication(sys.argv)
    window = PyQt5.Qt.QWidget()
    window.setWindowTitle('Chat App!')
    window.setGeometry(100,100,800,800)
    window.move(60,15)
    helloMsg = PyQt5.Qt.QLabel("<h1>Hello World</h1>", parent=window)
    helloMsg.move(60,15)
    window.show()
    sys.exit(app.exec())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
