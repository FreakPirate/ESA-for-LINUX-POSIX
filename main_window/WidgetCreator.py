#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from subprocess import call

class WidgetCreator():
    def __init__(self, layout):
        self.layout = layout

    def widgetUserAdd(self):

        self.usernameLe = QLineEdit()

        self.passwordLe = QLineEdit()
        self.passwordLe.setEchoMode(QLineEdit.Password)

        self.commentLe = QLineEdit()

        self.homedirLe = QLineEdit()
        self.homedirLe.setPlaceholderText("Enter path after /home")

        self.uidLe = QLineEdit()
        self.uidLe.setPlaceholderText("Default taken")

        self.gidLe = QLineEdit()
        self.gidLe.setPlaceholderText("Default taken")

        fo = open('/etc/shells', 'r')
        tmp = fo.read()
        shells = tmp.split('\n')

        self.shellCB = QComboBox()

        for i in shells:
            if i != '':
                self.shellCB.addItem(i)

        self.warn_lbl = QLabel()
        self.warn_lbl.setText('(*) Required fields')

        self.layout.addRow("Username*", self.usernameLe)
        self.layout.addRow("Password*", self.passwordLe)
        self.layout.addRow("Shells", self.shellCB)
        self.layout.addRow("Comments", self.commentLe)
        self.layout.addRow("Home Directory", self.homedirLe)
        self.layout.addRow("Uid", self.uidLe)
        self.layout.addRow("Gid", self.gidLe)
        self.layout.addRow(self.warn_lbl)

        self.layout.setVerticalSpacing(5)

    def widgetUserModDet(self):

        user_log = '/tmp/user.log'
        script = "awk  -F':' '$3>999 {print $1}' /etc/passwd | grep -v nobody >%s" %user_log
        call(script, shell=True)

        fo = open(user_log, 'r')
        data = fo.read().split('\n')
        self.usernameCB = QComboBox()
        self.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.usernameCB.addItem(i)
        fo.close()

        self.newUserNameLe = QLineEdit()
        self.newUserNameLe.setPlaceholderText("Enter new Login Name")

        self.commentLe = QLineEdit()

        self.homedirLe = QLineEdit()
        self.homedirLe.setPlaceholderText("Enter path after /home")

        self.uidLe = QLineEdit()
        self.uidLe.setPlaceholderText("Default taken")

        self.gidLe = QLineEdit()
        self.gidLe.setPlaceholderText("Default taken")

        fo = open('/etc/shells', 'r')
        tmp = fo.read()
        shells = tmp.split('\n')

        self.shellCB = QComboBox()

        for i in shells:
            if i != '':
                self.shellCB.addItem(i)

        self.warn_lbl = QLabel()
        self.warn_lbl.setText('(*) Required fields')

        self.layout.addRow("Username*", self.usernameCB)
        self.layout.addRow("New UserName", self.newUserNameLe)
        self.layout.addRow("Shells", self.shellCB)
        self.layout.addRow("Comments", self.commentLe)
        self.layout.addRow("Home Directory", self.homedirLe)
        self.layout.addRow("Uid", self.uidLe)
        self.layout.addRow("Gid", self.gidLe)
        self.layout.addRow(self.warn_lbl)

        self.layout.setVerticalSpacing(7)

    def widgetUserModPass(self):

        user_log = '/tmp/user.log'
        script = "awk  -F':' '$3>999 {print $1}' /etc/passwd | grep -v nobody >%s" %user_log
        call(script, shell=True)

        fo = open(user_log, 'r')
        data = fo.read().split('\n')
        self.usernameCB = QComboBox()
        self.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.usernameCB.addItem(i)
        fo.close()

        self.oldPassLe = QLineEdit()
        self.oldPassLe.setEchoMode(QLineEdit.Password)

        self.newPassLe = QLineEdit()
        self.newPassLe.setEchoMode(QLineEdit.Password)

        self.confirmPassLe = QLineEdit()
        self.confirmPassLe.setEchoMode(QLineEdit.Password)

        self.warn_lbl = QLabel()
        self.warn_lbl.setText('(*) Required fields')

        self.layout.addRow("Username*", self.usernameCB)
        self.layout.addRow("Old Password*", self.oldPassLe)
        self.layout.addRow("New Password*", self.newPassLe)
        self.layout.addRow("Confirm New Password*", self.confirmPassLe)
        self.layout.addRow(self.warn_lbl)

        self.layout.setVerticalSpacing(10)

    def widgetUserDel(self):

        user_log = '/tmp/user.log'
        script = "awk  -F':' '$3>999 {print $1}' /etc/passwd | grep -v nobody >%s" %user_log
        call(script, shell=True)

        fo = open(user_log, 'r')
        data = fo.read().split('\n')
        self.usernameCB = QComboBox()
        self.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.usernameCB.addItem(i)
        fo.close()

        self.typeCB = QComboBox()
        self.typeCB.addItem('Recursive')
        self.typeCB.addItem('Normal')

        self.recur_lbl = QLabel()
        self.recur_lbl.setText('Recursive- Delete user along with its home directory')

        self.normal_lbl = QLabel()
        self.normal_lbl.setText('Normal- Deleting user while keeping the home directory')

        self.warn_lbl = QLabel()
        self.warn_lbl.setText('(*) Required fields')

        self.layout.addRow("Username*", self.usernameCB)
        self.layout.addRow("Type*", self.typeCB)
        self.layout.addRow(self.recur_lbl)
        self.layout.addRow(self.normal_lbl)
        self.layout.addRow(self.warn_lbl)

        self.layout.setVerticalSpacing(10)