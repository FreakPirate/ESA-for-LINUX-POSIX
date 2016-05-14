# List and content all slots
import os
from subprocess import call
from utility_description import *

class Slots():
    def __init__(self, widgetCollection, retrievedDesc, vBoxBottom):
        self.widgetCollection = widgetCollection
        self.retrieved = retrievedDesc
        self.vBoxBottom = vBoxBottom

        self.cmd_useradmin_path = "/esa/scripts/user/useradmin"
        self.cmd_conn_limit_ftp = '/esa/scripts/firewall/rich_rules/connection_limit_ftp.sh'
        self.cmd_list_rich_rules = '/esa/scripts/firewall/rich_rules/list_rich_rules.sh'
        self.cmd_list_all_zones = '/esa/scripts/firewall/Zones/list_all_zones.sh'
        self.cmd_passwd = '/usr/bin/passwd'

        self.error_log = "/tmp/error.log"
        self.output_log = "/tmp/output.log"

        pass

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

        command = self.retrieved[0]

        script = "%s %s -a %s %s %s %s %s %s %s -p %s -s %s %s %s 2>%s >%s" \
                 % (self.cmd_useradmin_path,command,username,switch_c,comment,switch_d,homedir,
                    switch_g,gid,password,shell,switch_u,uid,self.error_log,self.output_log)

        print script
        call(script, shell=True)

        output = ''
        detail = ''

        fo = None
        if os.stat(self.error_log).st_size == 0:
            if os.stat(self.output_log).st_size == 0:
                output = 'OUTPUT'
                detail = 'None'
            else:
                fo = open(self.output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
        else:
            fo = open(self.error_log, 'r')
            output = 'ERROR'
            detail = fo.read()

        addDescription(output, detail, self.vBoxBottom)

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

        command = self.retrieved[0]

        script = "%s %s -a %s %s %s %s %s %s %s -s %s %s %s %s %s 2>%s >%s" \
                 % (self.cmd_useradmin_path,command,username,switch_c,comment,switch_d,homedir,
                    switch_g,gid,shell,switch_u,uid,switch_l,newusername,self.error_log,self.output_log)

        print script
        call(script, shell=True)

        output = ''
        detail = ''

        fo = None
        if os.stat(self.error_log).st_size == 0:
            if os.stat(self.output_log).st_size == 0:
                output = 'OUTPUT'
                detail = 'None'
            else:
                fo = open(self.output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
        else:
            fo = open(self.error_log, 'r')
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


        script = "echo -e \"%s\n%s\" | %s --stdin %s 2>%s >%s" %(newpass, newpass, self.cmd_passwd, username, self.error_log, self.output_log)
        print script
        call(script, shell=True)

        fo = None
        if os.stat(self.error_log).st_size == 0:
            if os.stat(self.output_log).st_size == 0:
                output = 'OUTPUT'
                detail = 'None'
            else:
                fo = open(self.output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
        else:
            fo = open(self.error_log, 'r')
            output = 'ERROR'
            detail = fo.read()

        addDescription(output, detail, self.vBoxBottom)

        fo.close()

        refreshUserNameCB(self.widgetCollection)

    def slotUserDel(self):
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

        command = self.retrieved[0]

        script = "%s %s %s -a %s 2>%s >%s" \
                 %(self.cmd_useradmin_path, command, switch_r, username, self.error_log, self.output_log)

        print script
        call(script, shell=True)

        fo = None
        if os.stat(self.error_log).st_size == 0:
            if os.stat(self.output_log).st_size == 0:
                output = 'OUTPUT'
                detail = 'None'
            else:
                fo = open(self.output_log, 'r')
                output = 'OUTPUT'
                detail = fo.read()
        else:
            fo = open(self.error_log, 'r')
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
                 %(self.cmd_conn_limit_ftp, conn_per_min, action, state, zone_name, self.error_log, self.output_log)

        # print script
        call(script, shell=True)

        output = ''
        fo = None
        if os.stat(self.error_log).st_size == 0:
            if os.stat(self.output_log).st_size == 0:
                addDescription("OUTPUT", "No output", self.widgetCollection)
                return
            else:
                fo = open(self.output_log, 'r')
                output = fo.read()
                # print output
        else:
            fo = open(self.error_log, 'r')
            addDescription("ERROR", fo.read(), self.widgetCollection)
            return

        fo.close()

        script = "%s 2>%s >%s" %(self.cmd_list_rich_rules, self.error_log, self.output_log)
        # print script
        call(script, shell=True)

        if os.stat(self.error_log).st_size == 0:
            if os.stat(self.output_log).st_size == 0:
                output = output + '\n\n' + 'RICH RULE ZONES:\n' + 'None'
            else:
                fo = open(self.output_log, 'r')
                output = output + '\n\n' + 'RICH RULE ZONES:\n' + fo.read()
        else:
            fo = open(self.error_log, 'r')
            output = output + '\n\n' + 'ERROR:\n' + fo.read()

        addDescription("OUTPUT", output, self.widgetCollection)
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

    def slotResetLimitFtpConn(self):
        self.widgetCollection.connPerMinLe.clear()
        self.widgetCollection.zoneNameLe.clear()