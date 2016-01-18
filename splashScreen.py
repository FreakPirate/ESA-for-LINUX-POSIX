from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import sys

def show(img_path='images/splashscreen.jpg'):
    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap(img_path)

    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)

    # adding progress bar
    progressBar = QProgressBar(splash)
    progressBar.setGeometry(splash.width()/10, 8*splash.height()/10, 8*splash.width()/10, splash.height()/20)

    splash.setMask(splash_pix.mask())

    splash.show()
    for i in range(0, 100):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.03:
           app.processEvents()

    # Simulate something that takes time
    # time.sleep(2)

    # app.exec_()
    return

if __name__ == '__main__':
    show()