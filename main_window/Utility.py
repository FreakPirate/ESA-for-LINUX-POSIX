import sqlite3
from subprocess import call
from PyQt4.QtGui import *
import sys

def refreshUserNameCB(widgetCollection):
    widgetCollection.usernameCB.clear()

    # Another way to clear QComboBox

    # item_count = self.widgetCollection.usernameCB.count()
    # for i in range(item_count):
    #     self.widgetCollection.usernameCB.removeItem(i)

    user_log = '/tmp/user.log'
    script = "awk  -F':' '$3>999 {print $1}' /etc/passwd | grep -v nobody >%s" %user_log
    call(script, shell=True)

    fo = open(user_log, 'r')
    data = fo.read().split('\n')
    widgetCollection.usernameCB.addItem('None')
    for i in reversed(data):
        if i != '':
            widgetCollection.usernameCB.addItem(i)
    fo.close()

def addDescription(title, content, vBoxBottom):
    removeDescription(vBoxBottom)
    lbl_title = QLabel()
    lbl_title.setText(title.upper())
    lbl_title.setWordWrap(True)

    lbl_content = QLabel()
    lbl_content.setText(content)
    lbl_content.setWordWrap(True)

    vBoxBottom.addWidget(lbl_title)
    vBoxBottom.addWidget(lbl_content)

    # print self.vBoxBottom

def removeDescription(vBoxBottom):
    for cnt in reversed(range(vBoxBottom.count())):
        # takeAt does both the jobs of itemAt and removeWidget
        # namely it removes an item and returns it
        widget = vBoxBottom.takeAt(cnt).widget()

        if widget is not None:
            # widget will be None if the item is a layout
            widget.deleteLater()

def fetchDescription(cmd_title):
    retrieved = None

    try:
        conn = sqlite3.connect('/esa/database/esa.db')
        cur = conn.cursor()

        query = 'SELECT CMD_NAME_RPM, DESCRIPTION FROM command_list WHERE CMD_TITLE = "%s"' %cmd_title
        print query
        cur.execute(query)

        retrieved = cur.fetchone()

    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        return "Error %s:" % e.args[0]
    finally:
        if conn:
            conn.close()
        return retrieved

def removeWidgetTopRight(vBoxTop):
    for cnt in reversed(range(vBoxTop.count())):
        # takeAt does both the jobs of itemAt and removeWidget
        # namely it removes an item and returns it
        widget = vBoxTop.takeAt(cnt).widget()

        if widget is not None:
            # widget will be None if the item is a layout
            widget.deleteLater()