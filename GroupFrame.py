# GroupFrame.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates  <-- TODO: NEEDS UPDATING
#
# See NOTICE.txt for copyrights and grant of license


from PyQt4.QtGui import QFrame, QPainter, QStyle, QPalette
from PyQt4.QtGui import QStyleOptionTabWidgetFrame, QStyleOptionFrameV2
import sys


class GroupFrame(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        ltrb = self.getContentsMargins()

        if str(self.style().objectName()).lower() == "windowsxp":
            self.setContentsMargins(ltrb[0] + 1, ltrb[1], ltrb[2] + 2, ltrb[3] + 1)
        else:
            self.setContentsMargins(ltrb[0] + 1, ltrb[1], ltrb[2] + 1, ltrb[3])

    def paintEvent(self, pevent):
        painter = QPainter(self)

        if str(self.style().objectName()).lower() == "windowsxp":
            # WINDOWS XP IN CLASIC VIEW DISPLAYS NO GROUPFRAME
            styleoptions = QStyleOptionTabWidgetFrame()
            frame = QStyle.PE_FrameTabWidget
        else:
            styleoptions = QStyleOptionFrameV2()
            frame = QStyle.PE_FrameGroupBox
        styleoptions.initFrom(self)
        self.style().drawPrimitive(frame, styleoptions, painter, self)
