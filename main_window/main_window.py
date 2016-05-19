#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UiCreator import *
from subprocess import call
import sqlite3
from Utility import *
from WidgetCreator import *
from Constants import *

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.description = None

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

        top_scroll = QScrollArea()
        top_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        top_scroll.setWidgetResizable(True)
        top_scroll.setWidget(self.topright)

        self.bottomright = QFrame()
        self.bottomright.setFrameShape(QFrame.StyledPanel)

        self.vBoxBottom = QVBoxLayout()
        self.bottomright.setLayout(self.vBoxBottom)

        #Scroll Area Properties
        bottom_scroll = QScrollArea()
        # scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        bottom_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        bottom_scroll.setWidgetResizable(True)
        bottom_scroll.setWidget(self.bottomright)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(top_scroll)
        splitter1.addWidget(bottom_scroll)
        splitter1.setSizes([200, 100])

        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(self.treeWidget)
        splitter2.addWidget(splitter1)
        splitter2.setSizes([50, 200])

        hBox.addWidget(splitter2)

        frameCentre.setLayout(hBox)

        self.setCentralWidget(frameCentre)

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
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
        user_administration = self.addParent(parent, column, 'User Administration', 'user admin')
        firewall = self.addParent(parent, column, 'Firewall', 'setup firewall')
        rich_rules = self.addParent(firewall, column, title_rich_rules, title_rich_rules)
        zone_rules = self.addParent(firewall, column, title_zone_rules, title_zone_rules)
        acl = self.addParent(parent, column, title_acl, title_acl)
        server = self.addParent(parent, column, 'Servers', 'confiure servers')

        self.addChild(user_administration, column, 'Add', 'Add a user')
        self.addChild(user_administration, column, 'Update Details', 'Update user details')
        self.addChild(user_administration, column, 'Update Password', 'Update user password')
        self.addChild(user_administration, column, 'Delete', 'Delete a user')

        self.addChild(firewall, column, 'Verify', 'Verify firewall installation')

        self.addChild(rich_rules, column, title_rich_limit_ftp, title_rich_limit_ftp)
        self.addChild(rich_rules, column, title_rich_list, title_rich_limit_ftp)
        self.addChild(rich_rules, column, title_rich_masquerade, title_rich_masquerade)
        self.addChild(rich_rules, column, title_rich_port_forwading, title_rich_port_forwading)
        self.addChild(rich_rules, column, title_rich_port_range, title_rich_port_range)
        self.addChild(rich_rules, column, title_rich_reject_traffic, title_rich_reject_traffic)

        self.addChild(zone_rules, column, title_zone_add_service, title_zone_add_service)
        self.addChild(zone_rules, column, title_zone_add_source, title_zone_add_source)
        self.addChild(zone_rules, column, title_zone_get_default_zone, title_zone_get_default_zone)
        self.addChild(zone_rules, column, title_zone_get_services, title_zone_get_services)
        self.addChild(zone_rules, column, title_zone_list_all, title_zone_list_all)
        self.addChild(zone_rules, column, title_zone_list_zones, title_zone_list_zones)
        self.addChild(zone_rules, column, title_zone_remove_service, title_zone_remove_service)
        self.addChild(zone_rules, column, title_zone_remove_source, title_zone_remove_source)
        self.addChild(zone_rules, column, title_zone_set_default_zone, title_zone_set_default_zone)

        self.addChild(acl, column, title_get_acl, title_get_acl)
        self.addChild(acl, column, title_remove_acl, title_remove_acl)
        self.addChild(acl, column, title_set_acl, title_set_acl)
        self.addChild(acl, column, title_set_default_dir_acl, title_set_default_dir_acl)
        self.addChild(acl, column, title_set_from_existing_file, title_set_from_existing_file)

        self.addChild(server, column, 'Samba', 'configure samba server')
        self.addChild(server, column, 'Apache Web Server', 'configure APACHE web server')
        self.addChild(server, column, 'DNS', 'configure DNS server')
        self.addChild(server, column, 'SSH', 'configure SSH server')
        self.addChild(server, column, 'FTP', 'configure FTP server')
        self.addChild(server, column, 'TELNET', 'configure TELNET server')

    def addParent(self, parent, column, title, data=''):
        item = QTreeWidgetItem(parent, [title])
        item.setData(column, Qt.UserRole, data)
        item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        return item

    def addChild(self, parent, column, title, data=''):
        item = QTreeWidgetItem(parent, [title])
        item.setData(column, Qt.UserRole, data)
        # item.setCheckState(column, Qt.Unchecked)
        return item

    def onItemClicked(self, item, column):
        self.widgetCollection = None
        self.widgetCollection = UiCreator(self.vBoxTop)

        self.description = None
        removeWidgetTopRight(self.vBoxTop)
        
        widgetCreator = WidgetCreator(self.widgetCollection, self.vBoxTop, self.vBoxBottom)

        if item.text(column) == 'Add':
            self.description = fetchDescription('ADDING NEW USER')
            widgetCreator.widgetUserAdd(self.description)
        elif item.text(column) == 'Update Details':
            self.description = fetchDescription('MODIFYING EXISTING USER')
            widgetCreator.widgetUserModDet(self.description)
        elif item.text(column) == 'Update Password':
            self.description = fetchDescription('MODIFYING EXISTING USER')
            widgetCreator.widgetUserModPass()
        elif item.text(column) == 'Delete':
            self.description = fetchDescription('DELETING EXISTING USER')
            widgetCreator.widgetUserDel(self.description)
        elif item.text(column) == 'List all Zones':
            self.description = fetchDescription('LIST ALL ZONES')
            widgetCreator.widgetListAllZones()
        elif item.text(column) == 'Limit FTP connection':
            self.description = ['Limit FTP Connections', 'With this you can limit the number of requests to ftp server.']
            widgetCreator.widgetLimitFtpConn()
        elif item.text(column) == title_get_acl:
            self.description = ['', 'This script shows the already present Access Control List of the given file.']
            widgetCreator.widgetGetAcl()
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

        if self.description != None:
            # print "In description if", self.description
            addDescription("DESCRIPTION", self.description[1], self.vBoxBottom)
        else:
            # print "In description  else"
            removeDescription(self.vBoxBottom)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
