# coding = utf-8

# GroupFrame.py: Kort's Spellcrafting Calculator
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license

# TODO: CONSIDER DROPPING SUPPORT FOR WINDOWS XP


from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QFrame, QStyle, QStyleOptionFrame, QStyleOptionTabWidgetFrame


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
            styleoptions = QStyleOptionFrame()
            frame = QStyle.PE_FrameGroupBox

        styleoptions.initFrom(self)
        self.style().drawPrimitive(frame, styleoptions, painter, self)
