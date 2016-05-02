#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from WidgetCreator import WidgetCreator
from subprocess import call
import sqlite3

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        frameCentre = QFrame(self)
        hBox = QHBoxLayout()

        self.treeWidget = QTreeWidget()
        self.treeWidget.setHeaderHidden(True)

        self.connect(self.treeWidget, SIGNAL("itemClicked(QTreeWidgetItem*, int)"), self.onItemClicked)
        self.addItems(self.treeWidget.invisibleRootItem())

        self.topright = QFrame()
        self.topright.setFrameShape(QFrame.StyledPanel)

        self.vBoxTop = QFormLayout()
        self.topright.setLayout(self.vBoxTop)

        self.bottomright = QFrame()
        self.bottomright.setFrameShape(QFrame.StyledPanel)

        self.vBoxBottom = QVBoxLayout()
        self.bottomright.setLayout(self.vBoxBottom)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(self.topright)
        splitter1.addWidget(self.bottomright)
        splitter1.setSizes([200, 100])

        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(self.treeWidget)
        splitter2.addWidget(splitter1)
        splitter2.setSizes([50, 200])

        hBox.addWidget(splitter2)

        frameCentre.setLayout(hBox)

        self.setCentralWidget(frameCentre)

        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(100, 100, 1200, 600)
        self.setWindowTitle('Enhanced Security Agent')
        self.show()

    def addItems(self, parent):
        column = 0
        clients_item = self.addParent(parent, column, 'User Administration', 'user admin')
        vendors_item = self.addParent(parent, column, 'Firewall Rules', 'setup firewall')
        time_period_item = self.addParent(parent, column, 'Servers', 'confiure servers')

        self.addChild(clients_item, column, 'Add', 'Add a user')
        self.addChild(clients_item, column, 'Update Details', 'Update user details')
        self.addChild(clients_item, column, 'Update Password', 'Update user password')
        self.addChild(clients_item, column, 'Delete', 'Delete a user')

        self.addChild(vendors_item, column, 'Append', 'append a rule in firewall')
        self.addChild(vendors_item, column, 'List', 'list all rules in firewall')
        self.addChild(vendors_item, column, 'Drop', 'drop rules')

        self.addChild(time_period_item, column, 'Samba', 'configure samba server')
        self.addChild(time_period_item, column, 'Apache Web Server', 'configure APACHE web server')
        self.addChild(time_period_item, column, 'DNS', 'configure DNS server')
        self.addChild(time_period_item, column, 'SSH', 'configure SSH server')
        self.addChild(time_period_item, column, 'FTP', 'configure FTP server')
        self.addChild(time_period_item, column, 'TELNET', 'configure TELNET server')

    def addParent(self, parent, column, title, data):
        item = QTreeWidgetItem(parent, [title])
        item.setData(column, Qt.UserRole, data)
        item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        return item

    def addChild(self, parent, column, title, data):
        item = QTreeWidgetItem(parent, [title])
        item.setData(column, Qt.UserRole, data)
        # item.setCheckState(column, Qt.Unchecked)
        return item

    def onItemClicked(self, item, column):
        self.widgetCollection = None
        self.widgetCollection = WidgetCreator(self.vBoxTop)

        self.removeWidgetTopRight()

        if item.text(column) == 'Add':
            self.retrieved = self.fetchDescription('ADDING NEW USER')
            self.widgetUserAdd()
        elif item.text(column) == 'Update Details':
            self.retrieved = self.fetchDescription('MODIFYING EXISTING USER')
            self.widgetUserModDet()
        elif item.text(column) == 'Update Password':
            self.retrieved = self.fetchDescription('MODIFYING EXISTING USER')
            self.widgetUserModPass()
        elif item.text(column) == 'Delete':
            self.retrieved = self.fetchDescription('DELETING EXISTING USER')
            self.widgetUserDel()
        elif item.text(column) == 'Append':
            pass
        elif item.text(column) == 'List':
            pass
        elif item.text(column) == 'Drop':
            pass
        elif item.text(column) == 'Samba':
            pass
        elif item.text(column) == 'Apache Web Server':
            pass
        elif item.text(column) == 'DNS':
            pass
        elif item.text(column) == 'SSH':
            pass
        elif item.text(column) == 'FTP':
            pass
        elif item.text(column) == 'TELNET':
            pass
        elif item.text(column) == 'User Administration':
            pass
        elif item.text(column) == 'Firewall Rules':
            pass
        elif item.text(column) == 'Servers':
            pass
        else:
            print "None", item.text(column)
            pass

        self.addDescription("DESCRIPTION", self.retrieved[1])

    def fetchDescription(self, cmd_title):
        retrieved = None

        try:
            conn = sqlite3.connect('/root/esa/database/esa.db')
            cur = conn.cursor()

            query = 'SELECT CMD_NAME_RPM, DESCRIPTION FROM command_list WHERE CMD_TITLE = "%s"' %cmd_title
            print query
            cur.execute(query)

            retrieved = cur.fetchone()

        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if conn:
                conn.close()
                return retrieved

    def addDescription(self, title, content):
        self.removeDescription()
        lbl_title = QLabel()
        lbl_title.setText(title.upper())
        lbl_title.setWordWrap(True)

        lbl_content = QLabel()
        lbl_content.setText(content)
        lbl_content.setWordWrap(True)

        self.vBoxBottom.addWidget(lbl_title)
        self.vBoxBottom.addWidget(lbl_content)

        # print self.vBoxBottom

    def removeDescription(self):
        for cnt in reversed(range(self.vBoxBottom.count())):
            # takeAt does both the jobs of itemAt and removeWidget
            # namely it removes an item and returns it
            widget = self.vBoxBottom.takeAt(cnt).widget()

            if widget is not None:
                # widget will be None if the item is a layout
                widget.deleteLater()

    def removeWidgetTopRight(self):
        for cnt in reversed(range(self.vBoxTop.count())):
            # takeAt does both the jobs of itemAt and removeWidget
            # namely it removes an item and returns it
            widget = self.vBoxTop.takeAt(cnt).widget()

            if widget is not None:
                # widget will be None if the item is a layout
                widget.deleteLater()

    def widgetUserAdd(self):
        self.widgetCollection.widgetUserAdd()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.accepted.connect(self.slotUserAdd)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(self.slotResetUserAdd)

        # self.layout.addStretch(3)
        self.vBoxTop.addWidget(button_box)

    def widgetUserModDet(self):
        self.widgetCollection.widgetUserModDet()
        
        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.accepted.connect(self.slotUserModDet)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(self.slotResetUserModDet)

        self.vBoxTop.addWidget(button_box)

    def widgetUserModPass(self):
        self.widgetCollection.widgetUserModPass()
        
        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.accepted.connect(self.slotUserModPass)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(self.slotResetUserModPass)

        self.vBoxTop.addWidget(button_box)

    def widgetUserDel(self):
        self.widgetCollection.widgetUserDel()
        
        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save)
        button_box.accepted.connect(self.slotUserDel)

        self.vBoxTop.addWidget(button_box)
    
    def slotUserAdd(self):
        username = str(self.widgetCollection.usernameLe.text())
        password = str(self.widgetCollection.passwordLe.text())
        comment = str(self.widgetCollection.commentLe.text())
        uid = str(self.widgetCollection.uidLe.text())
        gid = str(self.widgetCollection.gidLe.text())
        homedir = str(self.widgetCollection.homedirLe.text())
        shell = str(self.widgetCollection.shellCB.currentText())

        if username == '' or password == '':
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        command_path = "/root/esa/scripts/shell/useradmin"

        switch_c = ''
        switch_d = ''
        switch_g = ''
        switch_u = ''

        if comment != '':
            switch_c = '-c'
        if homedir != '':
            switch_d = '-d'
            homedir = '/home/' + homedir
        if gid != '':
            switch_g = '-g'
        if uid != '':
            switch_u = '-u'

        error_log = "/tmp/error.log"
        output_log = "/tmp/output.log"
        command = self.retrieved[0]

        script = "%s %s -a %s %s %s %s %s %s %s -p %s -s %s %s %s 2>%s >%s" \
                 % (command_path,command,username,switch_c,comment,switch_d,homedir,
                    switch_g,gid,password,shell,switch_u,uid,error_log,output_log)

        print script
        call(script, shell=True)
        
        fo = None
        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                self.addDescription("OUTPUT", "No output")
            else:
                fo = open(output_log, 'r')
                self.addDescription("OUTPUT", fo.read())
        else:
            fo = open(error_log, 'r')
            self.addDescription("ERROR", fo.read())

        fo.close()
        
    def slotUserModDet(self):
        username = str(self.widgetCollection.usernameCB.currentText())
        newusername = str(self.widgetCollection.newUserNameLe.text())
        comment = str(self.widgetCollection.commentLe.text())
        uid = str(self.widgetCollection.uidLe.text())
        gid = str(self.widgetCollection.gidLe.text())
        homedir = str(self.widgetCollection.homedirLe.text())
        shell = str(self.widgetCollection.shellCB.currentText())

        if username == '' or username == 'None':
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        command_path = "/root/esa/scripts/shell/useradmin"

        switch_c = ''
        switch_d = ''
        switch_g = ''
        switch_u = ''
        switch_l = ''

        if comment != '':
            switch_c = '-c'
        if homedir != '':
            switch_d = '-d'
            homedir = '/home/' + homedir
        if gid != '':
            switch_g = '-g'
        if uid != '':
            switch_u = '-u'
        if newusername != '':
            switch_l = '-l'

        error_log = "/tmp/error.log"
        output_log = "/tmp/output.log"
        command = self.retrieved[0]

        script = "%s %s -a %s %s %s %s %s %s %s -s %s %s %s %s %s 2>%s >%s" \
                 % (command_path,command,username,switch_c,comment,switch_d,homedir,
                    switch_g,gid,shell,switch_u,uid,switch_l,newusername,error_log,output_log)

        print script
        call(script, shell=True)
        
        fo = None
        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                self.addDescription("OUTPUT", "No output")
            else:
                fo = open(output_log, 'r')
                self.addDescription("OUTPUT", fo.read())
        else:
            fo = open(error_log, 'r')
            self.addDescription("ERROR", fo.read())

        fo.close()

        self.refreshUserNameCB()
        
    def slotUserModPass(self):
        username = str(self.widgetCollection.usernameCB.currentText())
        oldpass = str(self.widgetCollection.oldPassLe.text())
        newpass = str(self.widgetCollection.newPassLe.text())
        confirmpass = str(self.widgetCollection.confirmPassLe.text())

        if username == '' or username == 'None' or oldpass == '' or newpass == '' or confirmpass == '':
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        if newpass != confirmpass:
            self.widgetCollection.warn_lbl.setText('Passwords does not match.')
            self.slotResetUserModPass()
            return

        command_path = "/usr/bin/passwd"

        error_log = "/tmp/error.log"
        output_log = "/tmp/output.log"

        script = "echo -e \"%s\n%s\" | %s --stdin %s 2>%s >%s" %(newpass, newpass, command_path, username, error_log, output_log)
        print script
        call(script, shell=True)
        
        fo = None
        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                self.addDescription("OUTPUT", "No output")
            else:
                fo = open(output_log, 'r')
                self.addDescription("OUTPUT", fo.read())
        else:
            fo = open(error_log, 'r')
            self.addDescription("ERROR", fo.read())

        fo.close()

        self.refreshUserNameCB()
        
    def slotUserDel(self):
        username = str(self.widgetCollection.usernameCB.currentText())
        type = str(self.widgetCollection.typeCB.currentText())

        if username == '' or username == 'None':
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        command_path = "/root/esa/scripts/shell/useradmin"

        switch_r = ''

        if type == 'Recursive':
            switch_r = '-r'
        elif type == 'Normal':
            switch_r = ''
        else:
            print "Error with 'typeCB'"

        error_log = "/tmp/error.log"
        output_log = "/tmp/output.log"
        command = self.retrieved[0]

        script = "%s %s %s -a %s 2>%s >%s" \
                 %(command_path, command, switch_r, username, error_log, output_log)

        print script
        call(script, shell=True)
        
        fo = None
        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                self.addDescription("OUTPUT", "No output")
            else:
                fo = open(output_log, 'r')
                self.addDescription("OUTPUT", fo.read())
        else:
            fo = open(error_log, 'r')
            self.addDescription("ERROR", fo.read())

        fo.close()

        self.refreshUserNameCB()

    def refreshUserNameCB(self):
        self.widgetCollection.usernameCB.clear()
        item_count = self.widgetCollection.usernameCB.count()
        for i in range(item_count):
            self.widgetCollection.usernameCB.removeItem(i)

        user_log = '/tmp/user.log'
        script = "awk  -F':' '$3>999 {print $1}' /etc/passwd | grep -v nobody >%s" %user_log
        call(script, shell=True)

        fo = open(user_log, 'r')
        data = fo.read().split('\n')
        self.widgetCollection.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.widgetCollection.usernameCB.addItem(i)
        fo.close()

    def slotResetUserAdd(self):
        self.widgetCollection.usernameLe.clear()
        self.widgetCollection.passwordLe.clear()
        self.widgetCollection.commentLe.clear()
        self.widgetCollection.homedirLe.clear()
        self.widgetCollection.uidLe.clear()
        self.widgetCollection.gidLe.clear()

    def slotResetUserModDet(self):
        self.widgetCollection.newUserNameLe.clear()
        self.widgetCollection.commentLe.clear()
        self.widgetCollection.homedirLe.clear()
        self.widgetCollection.uidLe.clear()
        self.widgetCollection.gidLe.clear()

    def slotResetUserModPass(self):
        self.widgetCollection.oldPassLe.clear()
        self.widgetCollection.newPassLe.clear()
        self.widgetCollection.confirmPassLe.clear()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
