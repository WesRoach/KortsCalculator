#!/usr/bin/pythonw
# CraftBar.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates  <-- TODO: NEEDS UPDATING
#
# See NOTICE.txt for copyrights and grant of license


import SCWindow
import sys
import locale
from PyQt4.QtCore import *
from PyQt4.QtGui import *


locale.setlocale(locale.LC_ALL, '')  # TODO: ADD SUPPORT FOR ADDITIONAL LANGUAGES


class ScApplication(QApplication):

    def __init__(self):
        args = sys.argv
        self.curPath = QDir.cleanPath(QDir.currentPath())

        if args[0]:
            args[0] = str(QDir(self.curPath).absoluteFilePath(args[0]))

        else:

            args[0] = str(QDir(self.curPath).absoluteFilePath(__file__))
        self.appPath = str(QDir.cleanPath(QDir(args[0]).absoluteFilePath("..")))

        if len(args) > 1:
            args[1] = str(QDir.cleanPath(QDir(self.curPath).absoluteFilePath(args[1])))

        QResource.registerResource(QDir(self.appPath).absoluteFilePath("SC.rcc"))
        QApplication.__init__(self, args)

    def start(self):
        font = QFont(self.font())
        font.setPointSize(8);
        font.setFamily("Trebuchet MS")
        self.setFont(font)

        scw = SCWindow.SCWindow()
        app.setActiveWindow(scw)
        scw.setWindowIcon(QIcon(":/images/ScWindow.png"))

        if len(app.argv()) > 1:
            scw.openFile(app.argv()[1], True)

        scw.show()


if __name__ == '__main__':
    app = ScApplication()
    app.start()
    sys.exit(app.exec_())
