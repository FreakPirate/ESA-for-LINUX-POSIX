"""
Core functional and management module for the whole project
"""

import sys
import os.path
import SplashScreen
from auth import LoginDialog, RegisterDialog
from widgets import MainWindow
from PyQt4 import QtGui

def main(args='passwd.lck'):
    lock_file = 'esa.lck'

    pix_path = "images/splash_screen_01.jpg"
    SplashScreen.show(pix_path)

    # GUI MANAGEMENT BEGIN
    app = QtGui.QApplication(sys.argv)

    if not os.path.isfile(lock_file):
        file_conn = open(lock_file, 'w')
        file_conn.close()
        register = RegisterDialog.RegisterDialog()
        if not register.exec_():
            sys.exit(-1)

    login = LoginDialog.LoginDialog()
    if not login.exec_():
        sys.exit(-1)

    main_window = MainWindow.MainWindow()
    main_window.show()
    # GUI END

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
