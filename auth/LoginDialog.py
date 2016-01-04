import sys
from PyQt4 import QtGui, QtCore
import Authenticator

class LoginDialog(QtGui.QDialog):
    def __init__(self, lock_files, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.lock_files = lock_files
        self.show()

    def show(self):
        self.username = QtGui.QLineEdit()
        self.username.setPlaceholderText("Username")

        self.password = QtGui.QLineEdit()
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setPlaceholderText("Password")

        loginLayout = QtGui.QFormLayout()
        loginLayout.addRow("Username", self.username)
        loginLayout.addRow("Password", self.password)
        loginLayout.setVerticalSpacing(15)

        self.btn_recover = QtGui.QPushButton("Forgot Password")
        hBox = QtGui.QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(self.btn_recover)

        self.label = QtGui.QLabel()

        self.buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.handle_login)
        self.buttons.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(loginLayout)
        layout.addLayout(hBox)
        layout.addWidget(self.label)
        layout.addWidget(self.buttons)

        self.resize(250,150)
        self.setWindowTitle("Authentication")
        self.setWindowIcon(QtGui.QIcon("../logo/final.jpg"))
        self.setLayout(layout)

    def handle_login(self):
        username = str(self.username.text())
        password = str(self.password.text())

        loginCheckTrue = Authenticator.check(username, password, self.lock_files[0])

        if loginCheckTrue: # do actual login check
            self.accept()
        else:
            # self.pop_dialog = MyPopupDialog()
            # self.pop_dialog.exec_()

            self.username.clear()
            self.password.clear()
            self.username.setFocus()
            self.label.setText("Invalid username or password. Try again?")


    # def reject(self):
    #     #todo: implement exit check dialog
    #     pass


    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class MyPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyPopupDialog, self).__init__()
        self.check()

    def check(self):
        retry = QtGui.QMessageBox.critical(self, 'Login Failed',
            "Do you want to retry", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)

        if retry == QtGui.QMessageBox.Yes:
            pass
        else:
            QtGui.QApplication.quit()


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.label = QtGui.QLabel("Login Successful")
        self.setCentralWidget(self.label)

    def setUsername(self, username):
        # do whatever you want with the username
        self.username = username
        self.label.setText("Username entered: %s" % self.username)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    login = LoginDialog()
    if not login.exec_(): # 'reject': user pressed 'Cancel', so quit
        sys.exit(-1)

    # 'accept': continue
    main = MainWindow()
    # main.setUsername(login.username.text()) # get the username, and supply it to main window
    main.show()

    sys.exit(app.exec_())