import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

import untitled


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mn = QMainWindow()
    ui = untitled.Ui_Form()
    ui.setupUi(mn)
    mn.show()
    sys.exit(app.exec_())
