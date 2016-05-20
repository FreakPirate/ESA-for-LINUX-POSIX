
"""
Controller module:
Controls the functioning of rest of the modules
"""

import sys
import os.path
import SplashScreen
from auth import LoginDialog, RegisterDialog
from widgets import MainWindow
from PyQt4 import QtGui
import sqlite3 as sqlite


def main():
    # Database parameters
    database_name = "./database/user.sqlite"
    table_names = ["passwd", "shadow"]
    conn = None

    # Controller parameters
    splash_path = "images/splashscreen.jpg"
    logo_path = "images/logo.jpg"

    ### SPLASHSCREEN CALL ###
    SplashScreen.show(splash_path)

    app = QtGui.QApplication(sys.argv)

    ### SETTING DATABASE CONNECTION ###
    try:
        conn = sqlite.connect(database_name)
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwd'")
        table_check = cur.fetchone()[0]

        if table_check == 0:
            register = RegisterDialog.RegisterDialog(database_name, table_names, logo_path)
            if not register.exec_():
                sys.exit(-1)

            cur.execute("DROP TABLE IF EXISTS " + table_names[0])
            cur.execute("DROP TABLE IF EXISTS " + table_names[1])

            passwd_schema = '''CREATE TABLE %s
                (Id     INT     PRIMARY KEY     AUTOINCREMENT   NOT NULL,
                Name    TEXT    NOT NULL,
                Password    VARCHAR(100)    NOT NULL,
                Privilege   TEXT    NOT NULL
                )''' %table_names[0]

            shadow_schema = '''CREATE TABLE %s
                (Id     INT     AUTOINCREMENT   NOT NULL,
                EmailId VARCHAR(20)     NOT NULL,
                Phone   VARCHAR(20),
                Question    VARCHAR(40) NOT NULL,
                Answer  VARCHAR(100)    NOT NULL,
                FOREIGN KEY(PasswdId) REFERENCES passwd(Id)
                )''' %table_names[1]

            cur.execute(passwd_schema)
            cur.execute(shadow_schema)
    except sqlite.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if conn:
            conn.close()

    ### START: GUI MANAGEMENT ###

    login = LoginDialog.LoginDialog(lock_files, logo_path)
    if not login.exec_():
        sys.exit(-1)

    main_window = MainWindow.MainWindow()
    main_window.show()
    # GUI END

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
