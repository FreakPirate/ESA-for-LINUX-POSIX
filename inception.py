"""
Core functional and management module for the whole project
"""

import sys
import os.path
import SplashScreen
from auth import LoginDialog, RegisterDialog
from widgets import MainWindow
from PyQt4 import QtGui


def main():
    lock_files = ['lock/passwd.lck', 'lock/shadow.lck']
    esa_lock = 'lock/esa.lck'
    splash_path = "images/splashscreen.jpg"
    logo_path = "images/logo.jpg"
    SplashScreen.show(splash_path)

    # GUI MANAGEMENT BEGIN
    app = QtGui.QApplication(sys.argv)

    if not os.path.isfile(esa_lock):
        register = RegisterDialog.RegisterDialog(lock_files, logo_path)
        if not register.exec_():
            sys.exit(-1)
        file_conn = open(esa_lock, 'w')
        file_conn.close()

    login = LoginDialog.LoginDialog(lock_files, logo_path)
    if not login.exec_():
        sys.exit(-1)

    main_window = MainWindow.MainWindow()
    main_window.show()
    # GUI END

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
