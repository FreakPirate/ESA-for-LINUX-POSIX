from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.label = QtGui.QLabel("Login Successful")
        self.setCentralWidget(self.label)