import os
from subprocess import  call

from PyQt4.QtGui import *

from Constants import *
from Utility import *


# this class adds buttonBox and slots to the vTopBox
# if a user clicks the button, signal is emitted and slot is executed
# inside each slot the output is shown in vBoxBottom

class WidgetCreator:
    def __init__(self, widgetCollection, vBoxTop, vBoxBottom):
        
        self.widgetCollection = widgetCollection
        self.vBoxTop = vBoxTop
        self.vBoxBottom = vBoxBottom

    # adds buttonBox and slots to UserAdd
    def widgetUserAdd(self, description):
        self.widgetCollection.widgetUserAdd()

        # instantiating slots in variables
        slotSave = lambda : self.slotUserAdd(description)
        slotReset = lambda : self.slotResetUserAdd()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        # self.layout.addStretch(3)
        self.vBoxTop.addWidget(button_box)

    def widgetUserModDet(self, description):
        self.widgetCollection.widgetUserModDet()

        slotSave = lambda : self.slotUserModDet(description)
        slotReset = lambda : self.slotResetUserModDet()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetUserModPass(self):
        self.widgetCollection.widgetUserModPass()

        slotSave = lambda : self.slotUserModPass()
        slotReset = lambda : self.slotResetUserModPass()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetUserDel(self, description):
        self.widgetCollection.widgetUserDel()

        slotSave = lambda : self.slotUserDel(description)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)

        self.vBoxTop.addWidget(button_box)

    def widgetListAllZones(self):
        self.widgetCollection.widgetListAllZones()


        script = "%s 2>%s >%s" %(cmd_zone_list_zones, error_log, output_log)

        print script

        call(script, shell=True)

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                self.widgetCollection.zoneLbl.setText("Error executing  command.")
            else:
                fo = open(output_log, 'r')
                self.widgetCollection.zoneLbl.setText(fo.read())
                fo.close()
        else:
            fo = open(error_log, 'r')
            self.widgetCollection.zoneLbl.setText(fo.read())
            fo.close()

    def widgetLimitFtpConn(self):
        self.widgetCollection.widgetLimitFtpConn()

        slotSave = lambda : self.slotLimitFtpConn()
        slotReset = lambda : self.slotResetLimitFtpConn()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetGetAcl(self):
        self.widgetCollection.widgetGetAcl()

        slotSave = lambda : self.slotGetAcl()
        slotReset = lambda : self.slotResetGetAcl()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetRemoveAcl(self):
        self.widgetCollection.widgetRemoveAcl()

        slotSave = lambda : self.slotRemoveAcl()
        slotReset = lambda : self.slotResetRemoveAcl()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetSetAcl(self):
        self.widgetCollection.widgetSetAcl()

        slotSave = lambda : self.slotSetAcl(cmd_set_acl)
        slotReset = lambda : self.slotResetSetAcl()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetSetDefaultDirAcl(self):
        self.widgetCollection.widgetRemoveAcl()

        slotSave = lambda : self.slotSetAcl(cmd_set_default_directory_acl)
        slotReset = lambda : self.slotResetSetAcl()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetSetFromExistingAcl(self):
        self.widgetCollection.widgetSetFromExistingAcl()

        slotSave = lambda : self.slotSetFromExistingAcl()
        slotReset = lambda : self.slotResetSetFromExistingAcl()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetZoneAddService(self):
        self.widgetCollection.widgetZoneAddService()

        slotSave = lambda : self.slotZoneAddService()
        slotReset = lambda : self.slotResetZoneAddService()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetZoneAddSource(self):
        self.widgetCollection.widgetZoneAddSource()

        slotSave = lambda : self.slotZoneAddSource()
        slotReset = lambda : self.slotResetZoneAddSource()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetZoneRemoveService(self):
        self.widgetCollection.widgetZoneRemoveService()

        slotSave = lambda : self.slotZoneRemoveService()
        slotReset = lambda : self.slotResetZoneRemoveService()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetZoneRemoveSource(self):
        self.widgetCollection.widgetZoneRemoveSource()

        slotSave = lambda : self.slotZoneRemoveSource()
        slotReset = lambda : self.slotResetZoneRemoveSource()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    def widgetZoneSetDefault(self):
        self.widgetCollection.widgetZoneSetDefault()

        slotSave = lambda : self.slotZoneSetDefault()
        slotReset = lambda : self.slotResetZoneSetDefault()

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Reset)
        button_box.button(QDialogButtonBox.Save).clicked.connect(slotSave)
        button_box.button(QDialogButtonBox.Reset).clicked.connect(slotReset)

        self.vBoxTop.addWidget(button_box)

    # slot to respond when SAVE is clicked inside UserAdd tree widget item
    # it adds a user to the linux with details such as username, password, uid, gid etc.
    def slotUserAdd(self, description):
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

        command = description[0]

        script = "%s %s -a %s %s %s %s %s %s %s -p %s -s %s %s %s 2>%s >%s" \
                 % (cmd_useradmin_path,command,username,switch_c,comment,switch_d,homedir,
                    switch_g,gid,password,shell,switch_u,uid,error_log,output_log)

        # print script
        call(script, shell=True)

        output = ''
        detail = ''

        fo = None
        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output = 'OUTPUT'
                detail = 'None'
            else:
                fo = open(output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
        else:
            fo = open(error_log, 'r')
            output = 'ERROR'
            detail = fo.read()

        addDescription(output, detail, self.vBoxBottom)

        fo.close()

    def slotUserModDet(self, description):
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

        command = description[0]

        script = "%s %s -a %s %s %s %s %s %s %s -s %s %s %s %s %s 2>%s >%s" \
                 % (cmd_useradmin_path,command,username,switch_c,comment,switch_d,homedir,
                    switch_g,gid,shell,switch_u,uid,switch_l,newusername,error_log,output_log)

        print script
        call(script, shell=True)

        output = ''
        detail = ''

        fo = None
        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output = 'OUTPUT'
                detail = 'None'
            else:
                fo = open(output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
        else:
            fo = open(error_log, 'r')
            output = 'ERROR'
            detail = fo.read()

        addDescription(output, detail, self.vBoxBottom)

        fo.close()

        refreshUserNameCB(self.widgetCollection)

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


        script = "echo -e \"%s\n%s\" | %s --stdin %s 2>%s >%s" %(newpass, newpass, cmd_passwd, username, error_log, output_log)
        print script
        call(script, shell=True)

        fo = None
        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output = 'OUTPUT'
                detail = 'None'
            else:
                fo = open(output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
        else:
            fo = open(error_log, 'r')
            output = 'ERROR'
            detail = fo.read()

        addDescription(output, detail, self.vBoxBottom)

        fo.close()

        refreshUserNameCB(self.widgetCollection)

    def slotUserDel(self, description):
        username = str(self.widgetCollection.usernameCB.currentText())
        type = str(self.widgetCollection.typeCB.currentText())

        if username == '' or username == 'None':
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        switch_r = ''

        if type == 'Recursive':
            switch_r = '-r'
        elif type == 'Normal':
            switch_r = ''
        else:
            print "Error with 'typeCB'"

        command = description[0]

        script = "%s %s %s -a %s 2>%s >%s" \
                 %(cmd_useradmin_path, command, switch_r, username, error_log, output_log)

        print script
        call(script, shell=True)

        fo = None
        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output = 'OUTPUT'
                detail = 'None'
            else:
                fo = open(output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
        else:
            fo = open(error_log, 'r')
            output = 'ERROR'
            detail = fo.read()

        addDescription(output, detail, self.vBoxBottom)

        fo.close()

        refreshUserNameCB(self.widgetCollection)

    def slotLimitFtpConn(self):
        conn_per_min = str(self.widgetCollection.connPerMinLe.text())
        action = str(self.widgetCollection.actionCB.currentText())
        state = str(self.widgetCollection.stateTypeCB.currentText())
        zone_name = str(self.widgetCollection.zoneNameLe.text())

        if conn_per_min == '':
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        script = "%s %s %s %s %s 2>%s >%s" \
                 %(cmd_rich_limit_ftp, conn_per_min, action, state, zone_name, error_log, output_log)

        # print script
        call(script, shell=True)

        output = ''
        fo = None
        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                addDescription("OUTPUT", "No output", self.widgetCollection)
                return
            else:
                fo = open(output_log, 'r')
                output = fo.read()
                # print output
        else:
            fo = open(error_log, 'r')
            addDescription("ERROR", fo.read(), self.widgetCollection)
            return

        fo.close()

        script = "%s 2>%s >%s" %(cmd_rich_list, error_log, output_log)
        # print script
        call(script, shell=True)

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output = output + '\n\n' + 'RICH RULE ZONES:\n' + 'None'
            else:
                fo = open(output_log, 'r')
                output = output + '\n\n' + 'RICH RULE ZONES:\n' + fo.read()
        else:
            fo = open(error_log, 'r')
            output = output + '\n\n' + 'ERROR:\n' + fo.read()

        addDescription("OUTPUT", output, self.widgetCollection)
        fo.close()

    def slotGetAcl(self):
        filename = str(self.widgetCollection.filenameLe.text())

        if filename == '' or filename == None:
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        script = '%s %s 2>%s >%s' %(cmd_get_acl, filename, error_log, output_log)
        call(script, shell=True)

        output = ''
        detail = ''

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
            output = 'ERROR'
            e = fo.read()
            fo = open(output_log, 'r')
            o = fo.read()
            fo.close()

            detail = e + '\n\n' + o

        addDescription(output, detail, self.vBoxBottom)

    def slotRemoveAcl(self):
        filename = str(self.widgetCollection.filenameLe.text())
        username = str(self.widgetCollection.usernameCB.currentText())
        ownertype = str(self.widgetCollection.ownerTypeCB.currentText())
        directory = str(self.widgetCollection.directoryCB.currentText())

        if filename == '' or filename == None:
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        if ownertype == 'User':
            ownertype = 'u'
        elif ownertype == 'Group':
            ownertype = 'g'
        elif ownertype == 'Others':
            ownertype = 'o'

        script = '%s %s %s %s %s 2>%s >%s' %(cmd_remove_acl, ownertype, username, filename, directory, error_log, output_log)
        print script
        call(script, shell=True)

        output = ''
        detail = ''

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output, detail = getAcl(filename)
            else:
                fo = open(output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
                fo.close()
        else:
            fo = open(error_log, 'r')
            output = 'ERROR'
            e = fo.read()
            fo = open(output_log, 'r')
            o = fo.read()
            fo.close()
            detail = e + '\n\n' + o

        addDescription(output, detail, self.vBoxBottom)

    def slotSetAcl(self, command):
        filename = str(self.widgetCollection.filenameLe.text())
        username = str(self.widgetCollection.usernameCB.currentText())
        ownertype = str(self.widgetCollection.ownerTypeCB.currentText())
        directory = str(self.widgetCollection.directoryCB.currentText())
        permission = str(self.widgetCollection.permissionLe.text())

        if filename == '' or filename == None:
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        if ownertype == 'User':
            ownertype = 'u'
        elif ownertype == 'Group':
            ownertype = 'g'
        elif ownertype == 'Others':
            ownertype = 'o'

        script = '%s %s %s %s %s %s 2>%s >%s' %(command, ownertype, username, permission, filename, directory, error_log, output_log)
        print script
        call(script, shell=True)

        output = ''
        detail = ''

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output, detail = getAcl(filename)
            else:
                fo = open(output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
                fo.close()
        else:
            fo = open(error_log, 'r')
            output = 'ERROR'
            e = fo.read()
            fo = open(output_log, 'r')
            o = fo.read()
            fo.close()

            detail = e + '\n\n' + o

        addDescription(output, detail, self.vBoxBottom)

    def slotSetFromExistingAcl(self):
        sourcefile = str(self.widgetCollection.sourceFileLe.text())
        targetfile = str(self.widgetCollection.targetFileLe.text())

        if sourcefile == '' or sourcefile == None or targetfile == '' or targetfile == None:
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        script = '%s %s %s 2>%s >%s' %(cmd_set_from_existing_file, sourcefile, targetfile, error_log, output_log)
        print script
        call(script, shell=True)

        output = ''
        detail = ''

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output, detail = getAcl(targetfile)
            else:
                fo = open(output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
                fo.close()
        else:
            fo = open(error_log, 'r')
            output = 'ERROR'
            e = fo.read()
            fo = open(output_log, 'r')
            o = fo.read()
            fo.close()

            detail = e + '\n\n' + o

        addDescription(output, detail, self.vBoxBottom)

    def slotZoneAddService(self):
        zone = str(self.widgetCollection.zoneLe.text())
        service = str(self.widgetCollection.serviceCB.currentText())

        if zone == '' or zone == None:
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        script = "%s %s %s 2>%s >%s" %(cmd_zone_add_service, service, zone, error_log, output_log)
        call(script, shell=True)

        output = ''
        detail = ''

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output='OUTPUT'
                detail = 'None'
            else:
                fo = open(output_log, 'r')
                detail = fo.read()
                fo.close()
                detail = detail +'\n' + getZones()
        else:
            fo = open(error_log, 'r')
            detail = fo.read()
            fo.close()

        addDescription(output, detail, self.vBoxBottom)

    def slotZoneAddSource(self):
        zone = str(self.widgetCollection.zoneLe.text())
        source = str(self.widgetCollection.sourceLe.text())

        if zone == '' or zone == None:
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        script = "%s %s %s 2>%s >%s" %(cmd_zone_add_source, source, zone, error_log, output_log)
        call(script, shell=True)

        output = ''
        detail = ''

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output='OUTPUT'
                detail = 'None'
            else:
                fo = open(output_log, 'r')
                detail = fo.read()
                fo.close()
                detail = detail +'\n' + getZones()
        else:
            fo = open(error_log, 'r')
            detail = fo.read()
            fo.close()

        addDescription(output, detail, self.vBoxBottom)

    def slotZoneRemoveService(self):
        zone = str(self.widgetCollection.zoneLe.text())
        service = str(self.widgetCollection.serviceLe.text())

        if zone == '' or zone == None:
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        script = "%s %s %s 2>%s >%s" %(cmd_zone_remove_service, service, zone, error_log, output_log)
        call(script, shell=True)

        output = ''
        detail = ''

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output='OUTPUT'
                detail = 'None'
            else:
                fo = open(output_log, 'r')
                detail = fo.read()
                fo.close()
                detail = detail +'\n' + getZones()
        else:
            fo = open(error_log, 'r')
            detail = fo.read()
            fo.close()

        addDescription(output, detail, self.vBoxBottom)

    def slotZoneRemoveSource(self):
        zone = str(self.widgetCollection.zoneLe.text())
        service = str(self.widgetCollection.sourceLe.text())

        if zone == '' or zone == None:
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        script = "%s %s %s 2>%s >%s" %(cmd_zone_remove_source, service, zone, error_log, output_log)
        call(script, shell=True)

        output = ''
        detail = ''

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output='OUTPUT'
                detail = 'None'
            else:
                fo = open(output_log, 'r')
                detail = fo.read()
                fo.close()
                detail = detail +'\n' + getZones()
        else:
            fo = open(error_log, 'r')
            detail = fo.read()
            fo.close()

        addDescription(output, detail, self.vBoxBottom)

    def slotZoneSetDefault(self):
        zone = str(self.widgetCollection.zoneLe.text())

        if zone == '' or zone == None:
            self.widgetCollection.warn_lbl.setText("(*) marked fields are mandatory.")
            return

        script = "%s %s 2>%s >%s" %(cmd_zone_remove_source, zone, error_log, output_log)
        call(script, shell=True)

        output = ''
        detail = ''

        if os.stat(error_log).st_size == 0:
            if os.stat(output_log).st_size == 0:
                output='OUTPUT'
                detail = 'None'
            else:
                fo = open(output_log, 'r')
                detail = fo.read()
                fo.close()
                detail = detail +'\n' + getZones()
        else:
            fo = open(error_log, 'r')
            detail = fo.read()
            fo.close()

        addDescription(output, detail, self.vBoxBottom)

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
        refreshUserNameCB(self.widgetCollection)
        self.widgetCollection.newPassLe.clear()
        self.widgetCollection.confirmPassLe.clear()

    def slotResetLimitFtpConn(self):
        self.widgetCollection.connPerMinLe.clear()
        self.widgetCollection.zoneNameLe.clear()

    def slotResetGetAcl(self):
        self.widgetCollection.filenameLe.clear()

    def slotResetRemoveAcl(self):
        self.widgetCollection.filenameLe.clear()

    def slotResetSetAcl(self):
        self.widgetCollection.filenameLe.clear()
        self.widgetCollection.permissionLe.clear()

    def slotResetSetFromExistingAcl(self):
        self.widgetCollection.sourceFileLe.clear()
        self.widgetCollection.targetFileLe.clear()

    def slotResetZoneAddService(self):
        self.widgetCollection.zoneLe.clear()

    def slotResetZoneAddSource(self):
        self.widgetCollection.zoneLe.clear()
        self.widgetCollection.sourceLe.clear()

    def slotResetZoneRemoveService(self):
        self.widgetCollection.zoneLe.clear()
        self.widgetCollection.serviceLe.clear()

    def slotResetZoneRemoveSource(self):
        self.widgetCollection.zoneLe.clear()
        self.widgetCollection.sourceLe.clear()

    def slotResetZoneSetDefault(self):
        self.widgetCollection.zoneLe.clear()