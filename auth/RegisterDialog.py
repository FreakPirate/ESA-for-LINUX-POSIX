import sys
from PyQt4 import QtGui, QtCore
import Registrar


class RegisterDialog(QtGui.QDialog):
    def __init__(self, database_name, table_names, logo_path, parent=None):
        self.database_name = database_name
        self.table_names = table_names
        self.logo_path = logo_path
        super(RegisterDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.username = QtGui.QLineEdit()
        self.username.setPlaceholderText('Enter unique Username')

        self.email = QtGui.QLineEdit()
        self.email.setPlaceholderText('Enter valid E-mail')

        self.phone = QtGui.QLineEdit()
        self.phone.setPlaceholderText('Enter phone number')
        # self.phone.setValidator(QtGui.QIntValidator)

        self.password = QtGui.QLineEdit()
        self.password.setPlaceholderText('Enter Password')
        self.password.setEchoMode(QtGui.QLineEdit.Password)

        self.re_password = QtGui.QLineEdit()
        self.re_password.setPlaceholderText('Re-type Password')
        self.re_password.setEchoMode(QtGui.QLineEdit.Password)

        self.sec_ques = QtGui.QComboBox(self)
        self.sec_ques.addItem('What was your first pet name?')
        self.sec_ques.addItem('In which city were you born?')
        self.sec_ques.addItem('Who was your childhood hero?')
        self.sec_ques.addItem('What was the name of primary school?')
        self.sec_ques.addItem('What was your childhood nickname?')

        self.sec_ans = QtGui.QLineEdit()
        self.sec_ans.setPlaceholderText('Security Answer')
        self.sec_ans.setEchoMode(QtGui.QLineEdit.Password)

        self.q_check_box = QtGui.QCheckBox()
        self.q_check_box.stateChanged.connect(self.change_echo_mode)

        self.warn_lbl = QtGui.QLabel()
        self.warn_lbl.setText('(*) Required fields')

        hBox = QtGui.QHBoxLayout()
        hBox.addWidget(self.sec_ans)
        hBox.addWidget(self.q_check_box)

        registerLayout = QtGui.QFormLayout()
        registerLayout.addRow("Username*", self.username)
        registerLayout.addRow("E-Mail*", self.email)
        registerLayout.addRow("Phone No", self.phone)
        registerLayout.addRow("Password*", self.password)
        registerLayout.addRow("Re-Enter*", self.re_password)
        registerLayout.addRow("Security Question", self.sec_ques)
        registerLayout.addRow("Answer*", hBox)
        registerLayout.addRow(self.warn_lbl)

        registerLayout.setVerticalSpacing(10)

        button_box = QtGui.QDialogButtonBox()
        button_box.setStandardButtons(QtGui.QDialogButtonBox.Save | QtGui.QDialogButtonBox.Reset |
                                        QtGui.QDialogButtonBox.Cancel)

        button_box.accepted.connect(self.handle_registration)
        button_box.rejected.connect(self.reject)
        button_box.button(QtGui.QDialogButtonBox.Reset).clicked.connect(self.reset)

        vBox = QtGui.QVBoxLayout()
        vBox.addLayout(registerLayout)
        vBox.addStretch(3)
        vBox.addWidget(button_box)

        self.setWindowIcon(QtGui.QIcon(self.logo_path))
        self.setWindowTitle('Registration Dialog')
        self.resize(250, 300)

        self.setLayout(vBox)

    def change_echo_mode(self, state):
        if state == QtCore.Qt.Checked:
            self.sec_ans.setEchoMode(QtGui.QLineEdit.Normal)
        else:
            self.sec_ans.setEchoMode(QtGui.QLineEdit.Password)

    def handle_registration(self):
        username = str(self.username.text())
        email = str(self.email.text())
        phone = str(self.phone.text())
        password = str(self.password.text())
        re_password = str(self.re_password.text())
        sec_question = str(self.sec_ques.currentText())
        sec_ans = str(self.sec_ans.text())

        if username == '' or email == '' or password == '' or re_password == '' or sec_ans == '':
            self.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        if password != re_password:
            self.warn_lbl.setText("Passwords do not match")
            self.password.clear()
            self.re_password.clear()
            return

        register = Registrar.add(username, email, phone, password, sec_question, sec_ans,
            database_name, table_names)

        if register == "username":
            self.warn_lbl.setText('User already exist')
            self.username.clear()
            return

        if register == "email":
            self.warn_lbl.setText('Email-ID already exist')
            self.email.clear()
            return

        if register == "reject":
            self.reject()

        if register == "accept":
            self.accept()

    # def reject(self):
    #     QtGui.QApplication.quit()

    def reset(self):
        self.username.clear()
        self.password.clear()
        self.email.clear()
        self.phone.clear()
        self.sec_ans.clear()
        self.re_password.clear()
        self.setFocus()


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.label = QtGui.QLabel("Registration Successful")
        self.setCentralWidget(self.label)

    def setUsername(self, username):
        # do whatever you want with the username
        self.username = username
        self.label.setText("Username entered: %s" % self.username)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    register = RegisterDialog()
    if not register.exec_():
        sys.exit(-1)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
