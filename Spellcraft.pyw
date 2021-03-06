#!/usr/bin/pythonw
# coding = utf-8

# CraftBar.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from PyQt5.QtCore import QDir, QResource
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication
import SCWindow
import locale
import sys


locale.setlocale(locale.LC_ALL, '')  # TODO: ADD SUPPORT FOR ADDITIONAL LANGUAGES

# THIS MIGHT NOT BE NEEDED
QApplication.setDesktopSettingsAware(True)


class SpellCraftingCalculator(QApplication):

    def __init__(self):
        args = sys.argv
        self.curPath = QDir.cleanPath(QDir.currentPath())

        if args[0]:
            args[0] = str(QDir(self.curPath).absoluteFilePath(args[0]))

        else:
            args[0] = str(QDir(self.curPath).absoluteFilePath(__file__))

        self.appPath = str(QDir.cleanPath(QDir(args[0]).absoluteFilePath("..")))
        QApplication.__init__(self, args)

    def start(self):
        font = QFont(self.font())
        font.setPointSize(8)
        font.setFamily("Trebuchet MS")
        self.setFont(font)

        scc = SCWindow.SCWindow()
        self.setWindowIcon(QIcon(r"images/SCWindow.png"))
        app.setActiveWindow(scc)

        scc.show()


if __name__ == '__main__':
    app = SpellCraftingCalculator()
    app.start()
    sys.exit(app.exec_())
