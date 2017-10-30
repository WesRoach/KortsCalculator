#!/usr/bin/pythonw
# coding = utf-8

# CraftBar.py: Kort's Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates  <-- TODO: NEEDS UPDATING
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtCore import QDir, QResource
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication
from SCOptions import SCOptions
import SCWindow
import locale
import os
import os.path
import sys


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

        # THIS IS NO LONGER NEEDED SINCE WE HAVE STRIPPED SUPPORT FOR MACINTOSH
        # AND HAVE NO PLANS IN PORTING THIS TO ANY OTHER PLATFORMS.
        # if len(app.argv()) > 1:
        #   scw.openFile(app.argv()[1], True)

        scw.show()


if __name__ == '__main__':
    app = ScApplication()
    app.start()
    sys.exit(app.exec_())
