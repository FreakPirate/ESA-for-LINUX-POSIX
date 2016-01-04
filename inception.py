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
    lock_files = ['lock/passwd.lck', 'lock/shadow.lck']
    esa_lock = 'lock/esa.lck'
    pix_path = "images/splash_screen_01.jpg"
    SplashScreen.show(pix_path)

    # GUI MANAGEMENT BEGIN
    app = QtGui.QApplication(sys.argv)

    if not os.path.isfile(esa_lock):
        file_conn = open(esa_lock, 'w')
        file_conn.close()
        register = RegisterDialog.RegisterDialog(lock_files)
        if not register.exec_():
            sys.exit(-1)

    login = LoginDialog.LoginDialog(lock_files)
    if not login.exec_():
        sys.exit(-1)

    main_window = MainWindow.MainWindow()
    main_window.show()
    # GUI END

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
