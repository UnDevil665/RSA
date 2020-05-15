from RSA import keys
from PyQt5 import QtWidgets, QtCore
from Form1 import Ui_MainWindow
import sys

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.generate_Button.clicked.connect(self.generate_Btn_Clicked)
        self.ui.send_ok_Button.clicked.connect(self.send_ok_Btn_Clicked)
        self.ui.r_LineEdit.textChanged.connect(self.r_Edited)
        self.ui.send_r_Button.clicked.connect(self.send_r_Btn_Clicked)
        self.ui.decrypt_Button.clicked.connect(self.decrypt_Btn_Clicked)

    def generate_Btn_Clicked(self):
        self.ui.send_r_Button.setEnabled(False)
        self.e, self.n, self.d = keys(64)
        self.ui.e_LineEdit.setEnabled(True)
        self.ui.n_LineEdit.setEnabled(True)
        self.ui.d_LineEdit.setEnabled(True)

        self.ui.e_LineEdit.setText(str(self.e))
        self.ui.n_LineEdit.setText(str(self.n))
        self.ui.d_LineEdit.setText(str(self.d))

        self.ui.send_ok_Button.setEnabled(True)

    def send_ok_Btn_Clicked(self):
        self.ui.generate_Button.setEnabled(False)
        self.ui.send_ok_Button.setEnabled(False)
        self.ui.e_LineEdit2.setEnabled(True)
        self.ui.n_LineEdit2.setEnabled(True)
        self.ui.r_LineEdit.setEnabled(True)

        self.ui.e_LineEdit2.setText(str(self.e))
        self.ui.n_LineEdit2.setText(str(self.n))

    def r_Edited(self):
        self.ui.send_r_Button.setEnabled(True)

    def send_r_Btn_Clicked(self):
        self.ui.help_LineEdit.hide()
        if int(self.ui.r_LineEdit.text()) < self.n:
            self.ui.send_r_Button.setEnabled(False)
            self.ui.decrypt_Button.setEnabled(True)
            self.ui.cipher_LineEdit.setEnabled(True)

            self.ui.cipher_LineEdit.setText(str(pow(int(self.ui.r_LineEdit.text()), self.e, self.n)))
        else:
            self.ui.help_LineEdit.show()

    def decrypt_Btn_Clicked(self):
        self.ui.send_r_Button.setEnabled(True)
        self.ui.decrypt_Button.setEnabled(False)
        self.ui.r_LineEdit2.setEnabled(True)
        self.ui.generate_Button.setEnabled(True)

        self.ui.r_LineEdit2.setText(str(pow(int(self.ui.cipher_LineEdit.text()), self.d, self.n)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = MyWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()