"""
Core functional and management module for the whole project
"""

import sys
import os.path
import SplashScreen
from Constants import splashscreen_path, esa_lock
from auth import LoginDialog, RegisterDialog
from widget import MainWindow
from PyQt4 import QtGui


def main():

    SplashScreen.show(splashscreen_path)

    # GUI MANAGEMENT BEGIN
    app = QtGui.QApplication(sys.argv)

    if not os.path.isfile(esa_lock):
        register = RegisterDialog.RegisterDialog()
        if not register.exec_():
            sys.exit(-1)
        file_conn = open(esa_lock, 'w')
        file_conn.close()
        print "EOF if not"

    login = LoginDialog.LoginDialog()
    if not login.exec_():
        sys.exit(-1)

    main_window = MainWindow.main()
    main_window.show()
    # GUI END

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
