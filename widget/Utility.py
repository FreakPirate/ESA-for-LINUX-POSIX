# Helper File Functions

import os
import sqlite3
from subprocess import call

from PyQt4.QtGui import *

from Constants import *


# Refreshes the UserName combobox when either a  user is added or removed
def refreshUserNameCB(widgetCollection):
    widgetCollection.usernameCB.clear()

    # Another way to clear QComboBox

    # item_count = self.widgetCollection.usernameCB.count()
    # for i in range(item_count):
    #     self.widgetCollection.usernameCB.removeItem(i)

    user_log = '/tmp/user.log'
    # script to be executed
    script = "awk  -F':' '$3>999 {print $1}' /etc/passwd | grep -v nobody >%s" %user_log
    # this is how a script is exected and output is recorded inside /tmp/output.log
    call(script, shell=True)

    fo = open(user_log, 'r')
    data = fo.read().split('\n')
    widgetCollection.usernameCB.addItem('None')
    for i in reversed(data):
        if i != '':
            widgetCollection.usernameCB.addItem(i)
    fo.close()

# returns a stream of services available on the system
def getAcl(filename):

    script = "%s %s 2>%s >%s" %(cmd_get_acl, filename, error_log, output_log)
    call(script, shell=True)

    detail = ''
    output = ''

    if os.stat(error_log).st_size == 0:
        if os.stat(output_log).st_size == 0:
            output = 'OUTPUT'
            detail = 'None'
        else:
            fo = open(output_log, 'r')
            output = 'OUTPUT'
            detail = fo.read()
            fo.close()
    else:
        fo = open(error_log, 'r')
        output = 'OUTPUT'
        e = fo.read()
        fo = open(output_log, 'r')
        o = fo.read()
        detail = e + '\n' + o

    return output, detail

def getZones():
    script = "%s 2>%s >%s" %(cmd_zone_list_zones, error_log, output_log)
    call(script, shell=True)

    if os.stat(error_log).st_size == 0:
        if os.stat(output_log).st_size == 0:
            detail = 'None'
        else:
            fo = open(output_log, 'r')
            detail = fo.read()
            fo.close()
    else:
        fo = open(error_log, 'r')
        detail = fo.read()

    return detail

# adds content provided to the vBoxBottom
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

# Removes any previously set description inside vBoxBottom
def removeDescription(vBoxBottom):
    for cnt in reversed(range(vBoxBottom.count())):
        # takeAt does both the jobs of itemAt and removeWidget
        # namely it removes an item and returns it
        widget = vBoxBottom.takeAt(cnt).widget()

        if widget is not None:
            # widget will be None if the item is a layout
            widget.deleteLater()

# instantiate connection to the database and queries for description
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