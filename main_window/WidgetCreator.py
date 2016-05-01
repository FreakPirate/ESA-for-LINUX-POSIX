#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *


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
        self.uidLe.setPlaceholderText("Default will be taken")

        self.gidLe = QLineEdit()
        self.gidLe.setPlaceholderText("Default will be taken")

        fo = open('/etc/shells', 'r')
        tmp = fo.read()
        shells = tmp.split('\n')

        self.shellCb = QComboBox()

        for i in shells:
            if i != '':
                self.shellCb.addItem(i)

        self.warn_lbl = QLabel()
        self.warn_lbl.setText('(*) Required fields')

        self.layout.addRow("Username*", self.usernameLe)
        self.layout.addRow("Password*", self.passwordLe)
        self.layout.addRow("Shells", self.shellCb)
        self.layout.addRow("Comments", self.commentLe)
        self.layout.addRow("Home Directory", self.homedirLe)
        self.layout.addRow("Uid", self.uidLe)
        self.layout.addRow("Gid", self.gidLe)
        self.layout.addRow(self.warn_lbl)

        self.layout.setVerticalSpacing(5)