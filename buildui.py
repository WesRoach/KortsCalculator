#!/usr/bin/python
import os
import sys

files = (
    ('ScWindow.ui', 'B_ScWindow.py'),
    ('CraftWindow.ui', 'B_CraftWindow.py'),
    ('DisplayWindow.ui', 'B_DisplayWindow.py'),
    ('ReportWindow.ui', 'B_ReportWindow.py'),
    ('ItemLevel.ui', 'B_ItemLevel.py'),
    ('CraftBar.ui', 'B_CraftBar.py'),
    ('Options.ui', 'B_Options.py'),
)

for ui, py in files:
    try:
        if os.stat(ui).st_mtime < os.stat(py).st_mtime:
            continue
    except:
        # We are happy to continue if a file is not found,
        # as we will error on a missing input file, and go
        # quietly on if the output file was missing
        pass
    # Add -d to the .system command if you want gory details
    os.system('%s -o %s %s' % (os.path.join(os.path.dirname(sys.executable),'pyuic4'), py, ui))

    # Make this Win32 text
    if os.name == 'nt':
        f = open(py, 'r')
        scstr = f.read()
        f.close()
        f = open(py, 'w')
        f.write(scstr)
        f.close()
        del scstr

    sys.stdout.write("Generated %s from %s\n" % (py, ui))

# a bit of magic, if a file changes in images/*, the dir's mtime bumps too:
if os.stat("SC.qrc").st_mtime >= os.stat("SC.rcc").st_mtime \
        or os.stat("images").st_mtime >= os.stat("SC.rcc").st_mtime:
    os.system('rcc -binary SC.qrc -o SC.rcc');
    sys.stdout.write("Generated SC.rcc from SC.qrc\n")
