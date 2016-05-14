#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from WidgetCreator import WidgetCreator
from subprocess import call
import sqlite3
from utility_description import *
from utility_slots import Slots

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.cmd_useradmin_path = "/esa/scripts/user/useradmin"
        self.cmd_conn_limit_ftp = '/esa/scripts/firewall/rich_rules/connection_limit_ftp.sh'
        self.cmd_list_rich_rules = '/esa/scripts/firewall/rich_rules/list_rich_rules.sh'
        self.cmd_list_all_zones = '/esa/scripts/firewall/Zones/list_all_zones.sh'
        self.cmd_passwd = '/usr/bin/passwd'

        self.error_log = "/tmp/error.log"
        self.output_log = "/tmp/output.log"

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
        rich_rules = self.addParent(firewall, column, 'Rich Rules', 'Rich rule configuration')
        zone_rules = self.addParent(firewall, column, 'Zone Rules', 'Zonal setup')
        server = self.addParent(parent, column, 'Servers', 'confiure servers')

        self.addChild(user_administration, column, 'Add', 'Add a user')
        self.addChild(user_administration, column, 'Update Details', 'Update user details')
        self.addChild(user_administration, column, 'Update Password', 'Update user password')
        self.addChild(user_administration, column, 'Delete', 'Delete a user')

        self.addChild(firewall, column, 'Verify', 'Verify firewall installation')

        self.addChild(rich_rules, column, 'List', 'List all rich rules')
        self.addChild(rich_rules, column, 'Limit FTP connection', 'Limiting FTP connections')
        self.addChild(rich_rules, column, 'Port Forwading', 'forward port traffic')
        self.addChild(rich_rules, column, 'Reject source traffic', 'Limiting FTP connections')

        self.addChild(zone_rules, column, 'List all Zones', 'Add zone service')
        self.addChild(zone_rules, column, 'List specific Zone', 'Add zone service')
        self.addChild(zone_rules, column, 'Add Service', 'Add zone service')
        self.addChild(zone_rules, column, 'Remove Service', 'Add zone service')
        self.addChild(zone_rules, column, 'Add Source', 'Add zone service')
        self.addChild(zone_rules, column, 'Get Service', 'Add zone service')
        self.addChild(zone_rules, column, 'Remove Zone', 'Add zone service')
        self.addChild(zone_rules, column, 'Set default Zone', 'Add zone service')
        self.addChild(zone_rules, column, 'Get default Zone', 'Add zone service')

        self.addChild(server, column, 'Samba', 'configure samba server')
        self.addChild(server, column, 'Apache Web Server', 'configure APACHE web server')
        self.addChild(server, column, 'DNS', 'configure DNS server')
        self.addChild(server, column, 'SSH', 'configure SSH server')
        self.addChild(server, column, 'FTP', 'configure FTP server')
        self.addChild(server, column, 'TELNET', 'configure TELNET server')

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
        elif item.text(column) == 'List all Zones':
            self.retrieved = self.fetchDescription('LIST ALL ZONES')
            self.widgetListAllZones()
        elif item.text(column) == 'Limit FTP connection':
            self.retrieved = ['Limit FTP Connections', 'With this you can limit the number of requests to ftp server.']
            self.widgetLimitFtpConn()
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

        addDescription("DESCRIPTION", self.retrieved[1], self.vBoxBottom)

    def fetchDescription(self, cmd_title):
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
            sys.exit(1)
        finally:
            if conn:
                conn.close()
                return retrieved

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

        slots = Slots(self.widgetCollection, self.retrieved, self.vBoxBottom)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.accepted.connect(slots.slotUserAdd)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slots.slotResetUserAdd)

        # self.layout.addStretch(3)
        self.vBoxTop.addWidget(button_box)

    def widgetUserModDet(self):
        self.widgetCollection.widgetUserModDet()

        slots = Slots(self.widgetCollection, self.retrieved, self.vBoxBottom)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.accepted.connect(slots.slotUserModDet)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slots.slotResetUserModDet)

        self.vBoxTop.addWidget(button_box)

    def widgetUserModPass(self):
        self.widgetCollection.widgetUserModPass()

        slots = Slots(self.widgetCollection, self.retrieved, self.vBoxBottom)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.accepted.connect(slots.slotUserModPass)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slots.slotResetUserModPass)

        self.vBoxTop.addWidget(button_box)

    def widgetUserDel(self):
        self.widgetCollection.widgetUserDel()

        slots = Slots(self.widgetCollection, self.retrieved, self.vBoxBottom)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save)
        button_box.accepted.connect(slots.slotUserDel)

        self.vBoxTop.addWidget(button_box)

    def widgetListAllZones(self):
        self.widgetCollection.widgetListAllZones()


        script = "%s 2>%s >%s" %(self.cmd_list_all_zones, self.error_log, self.output_log)

        print script

        call(script, shell=True)

        if os.stat(self.error_log).st_size == 0:
            if os.stat(self.output_log).st_size == 0:
                self.widgetCollection.zoneLbl.setText("Error executing  command.")
            else:
                fo = open(self.output_log, 'r')
                self.widgetCollection.zoneLbl.setText(fo.read())
        else:
            fo = open(self.error_log, 'r')
            self.widgetCollection.zoneLbl.setText(fo.read())

        fo.close()

    def widgetLimitFtpConn(self):
        self.widgetCollection.widgetLimitFtpConn()

        slots = Slots(self.widgetCollection, self.retrieved, self.vBoxBottom)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.accepted.connect(slots.slotLimitFtpConn)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slots.slotResetLimitFtpConn)

        self.vBoxTop.addWidget(button_box)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
