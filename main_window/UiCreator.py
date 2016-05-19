#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from subprocess import call

class UiCreator():
    def __init__(self, layout):
        self.layout = layout

        self.warn_lbl = QLabel()
        self.warn_lbl.setText('(*) Required fields')

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
        data = self.fetchNormalUsers()

        self.usernameCB = QComboBox()
        self.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.usernameCB.addItem(i)

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
        data = self.fetchNormalUsers()

        self.usernameCB = QComboBox()
        self.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.usernameCB.addItem(i)

        self.oldPassLe = QLineEdit()
        self.oldPassLe.setEchoMode(QLineEdit.Password)

        self.newPassLe = QLineEdit()
        self.newPassLe.setEchoMode(QLineEdit.Password)

        self.confirmPassLe = QLineEdit()
        self.confirmPassLe.setEchoMode(QLineEdit.Password)

        self.layout.addRow("Username*", self.usernameCB)
        self.layout.addRow("Old Password*", self.oldPassLe)
        self.layout.addRow("New Password*", self.newPassLe)
        self.layout.addRow("Confirm New Password*", self.confirmPassLe)
        self.layout.addRow(self.warn_lbl)

        self.layout.setVerticalSpacing(10)

    def widgetUserDel(self):

        data = self.fetchNormalUsers()

        self.usernameCB = QComboBox()
        self.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.usernameCB.addItem(i)

        self.typeCB = QComboBox()
        self.typeCB.addItem('Recursive')
        self.typeCB.addItem('Normal')

        self.recur_lbl = QLabel()
        self.recur_lbl.setText('Recursive- Delete user along with its home directory')

        self.normal_lbl = QLabel()
        self.normal_lbl.setText('Normal- Deleting user while keeping the home directory')

        self.layout.addRow("Username*", self.usernameCB)
        self.layout.addRow("Type*", self.typeCB)
        self.layout.addRow(self.recur_lbl)
        self.layout.addRow(self.normal_lbl)
        self.layout.addRow(self.warn_lbl)

        self.layout.setVerticalSpacing(10)

    def widgetListAllZones(self):
        self.zonesTitleLbl = QLabel()
        self.zonesTitleLbl.setText("ZONES:")

        self.zoneLbl = QLabel()

        self.layout.addRow(self.zonesTitleLbl)
        self.layout.addRow(self.zoneLbl)

    def widgetLimitFtpConn(self):
        self.connPerMinLe = QLineEdit()

        self.actionCB = QComboBox()
        self.actionCB.addItem('add')
        self.actionCB.addItem('remove')

        self.stateTypeCB = QComboBox()
        self.stateTypeCB.addItem('permanent')
        self.stateTypeCB.addItem('temporary')

        self.zoneNameLe = QLineEdit()

        self.layout.addRow('Number of connections per min*', self.connPerMinLe)
        self.layout.addRow('Action*', self.actionCB)
        self.layout.addRow('State*', self.stateTypeCB)
        self.layout.addRow('Zone Name (optional)', self.zoneNameLe)
        self.layout.addRow(self.warn_lbl)

    def widgetGetAcl(self):
        self.filenameLe = QLineEdit()
        self.filenameLe.setPlaceholderText('Enter valid file name/path')

        self.layout.addRow('File Name*', self.filenameLe)
        self.layout.addRow(self.warn_lbl)

    def widgetRemoveAcl(self):
        self.filenameLe = QLineEdit()
        self.filenameLe.setPlaceholderText('Enter valid file name/path')
        
        self.ownerTypeCB = QComboBox()
        self.ownerTypeCB.addItem('User')
        self.ownerTypeCB.addItem('Group')
        self.ownerTypeCB.addItem('Others')

        data = self.fetchNormalUsers()

        self.usernameCB = QComboBox()
        self.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.usernameCB.addItem(i)

        self.directoryCB = QComboBox()
        self.directoryCB.addItem('yes')
        self.directoryCB.addItem('no')

        self.layout.addRow('FileName*', self.filenameLe)
        self.layout.addRow('Owner Type', self.ownerTypeCB)
        self.layout.addRow('User Name', self.usernameCB)
        self.layout.addRow('Directory?', self.directoryCB)
        self.layout.addRow(self.warn_lbl)

    def widgetSetAcl(self):
        self.filenameLe = QLineEdit()
        self.filenameLe.setPlaceholderText('Enter valid file name/path')

        self.permissionLe = QLineEdit()
        self.permissionLe.setPlaceholderText('rwx, rw, wx, rx, r, w, x')

        self.ownerTypeCB = QComboBox()
        self.ownerTypeCB.addItem('User')
        self.ownerTypeCB.addItem('Group')
        self.ownerTypeCB.addItem('Others')

        data = self.fetchNormalUsers()

        self.usernameCB = QComboBox()
        self.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.usernameCB.addItem(i)

        self.directoryCB = QComboBox()
        self.directoryCB.addItem('yes')
        self.directoryCB.addItem('no')

        self.layout.addRow('FileName*', self.filenameLe)
        self.layout.addRow('Permissions', self.permissionLe)
        self.layout.addRow('Owner Type', self.ownerTypeCB)
        self.layout.addRow('User Name', self.usernameCB)
        self.layout.addRow('Directory?', self.directoryCB)
        self.layout.addRow(self.warn_lbl)

    def widgetSetDefaultDirAcl(self):
        self.filenameLe = QLineEdit()
        self.filenameLe.setPlaceholderText('Enter valid file name/path')

        self.permissionLe = QLineEdit()
        self.permissionLe.setPlaceholderText('rwx, rw, wx, rx, r, w, x')

        self.ownerTypeCB = QComboBox()
        self.ownerTypeCB.addItem('User')
        self.ownerTypeCB.addItem('Group')
        self.ownerTypeCB.addItem('Others')

        data = self.fetchNormalUsers()

        self.usernameCB = QComboBox()
        self.usernameCB.addItem('None')
        for i in reversed(data):
            if i != '':
                self.usernameCB.addItem(i)

        self.directoryCB = QComboBox()
        self.directoryCB.addItem('yes')
        self.directoryCB.addItem('no')

        self.layout.addRow('FileName*', self.filenameLe)
        self.layout.addRow('Permissions*', self.permissionLe)
        self.layout.addRow('Owner Type', self.ownerTypeCB)
        self.layout.addRow('User Name', self.usernameCB)
        self.layout.addRow('Directory?', self.directoryCB)
        self.layout.addRow(self.warn_lbl)

    def widgetSetFromExistingAcl(self):
        self.sourceFileLe = QLineEdit()
        self.sourceFileLe.setPlaceholderText('Source file name/path')

        self.targetFileLe = QLineEdit()
        self.targetFileLe.setPlaceholderText('Target file name/path')

        self.layout.addRow('Source File*', self.sourceFileLe)
        self.layout.addRow('Target File*', self.targetFileLe)
        self.layout.addRow(self.warn_lbl)


    def fetchNormalUsers(self):
        user_log = '/tmp/user.log'
        script = "awk  -F':' '$3>999 {print $1}' /etc/passwd | grep -v nobody >%s" %user_log
        call(script, shell=True)

        fo = open(user_log, 'r')
        data = fo.read().split('\n')
        fo.close()

        return data