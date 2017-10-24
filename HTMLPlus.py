#
# Copyright 2006 by Ehrayn <ehrayn@sourceforge.net>
# Granted 2006 by Ehrayn to the public domain
#

"Proper handling of line breaks, newer entity defs and indentation"

import string
import formatter
import htmllib
import sys


class DimWriter(formatter.DumbWriter):
    def __init__(self, file=None, maxcol=72, indent=8):
        self.margin = 0
        self.indent = indent
        formatter.DumbWriter.__init__(self, file, maxcol)

    def send_paragraph(self, blankline):
        self.file.write('\n'*(blankline + 1))
        self.col = 0
        self.atbreak = 0

    def new_margin(self, margin, depth):
        self.margin = depth * self.indent

    def send_literal_data(self, data):
        if self.margin > 0:
            col = self.col
            for line in data.splitlines(True):
                if (col < self.margin):
                    self.file.write(' '*(self.margin - col))
                    col = self.margin
                self.file.write(line)
                if line[-1] == "\n":
                    col = 0
                else:
                    line.expandtabs()
                    col += len(line)
            self.atbreak = 0
            self.col = col
        else:
            formatter.DumbWriter.send_literal_data(self, data)

    def send_column_break(self):
        self.send_literal_data('  ')

    def send_flowing_data(self, data, label = 0):
        if data:
            data = data.replace('\xa0', '')
        if not data: return
        atbreak = self.atbreak or data[0].isspace()
        col = self.col
        maxcol = self.maxcol
        write = self.file.write
        for word in data.split():
            if atbreak:
                if col + len(word) >= maxcol:
                    write('\n')
                    atbreak = 0
                    col = 0
            if col < self.margin:
                if label:
                    indent = max(self.margin - len(data) - 1, 0)
                else:
                    indent = self.margin - col
                write(' '*(indent))
                col += indent
                label = 0
                atbreak = 0
            if atbreak:
                write(' ')
                col = col + 1
            write(word)
            col = col + len(word)
            atbreak = 1
        self.col = col
        self.atbreak = data[-1].isspace()

    def send_label_data(self, data):
        self.send_flowing_data(data, 1)
        self.atbreak = 1

    def send_hor_rule(self, *args, **kw):
        col = self.col
        if col < self.margin:
            self.file.write(' '*(self.margin - col))
            col = self.margin
        self.file.write('-'*(self.maxcol - col))
        self.send_line_break()

    def new_alignment(self, align):
        pass


class ObtuseFormatter(formatter.AbstractFormatter):

    def add_column_break(self, attr):
        self.softspace = 0
        self.nospace = 1
        self.writer.send_column_break()

    def add_line_break(self):
        # <br /> is absolute
        self.writer.send_line_break()
        self.have_label = 0
        self.hard_break = self.nospace = 1
        self.have_label = self.softspace = self.parskip = self.para_end = 0

    def add_hor_rule(self, *args, **kw):
        # <hr /> looks funky, collapse surrounding line breaks
        if not self.hard_break:
            self.writer.send_line_break()
        self.writer.send_hor_rule(*args, **kw)
        self.hard_break = self.nospace = self.parskip = 1
        self.have_label = self.softspace = self.para_end = 0
    

class HTMLPlusParser(htmllib.HTMLParser):
    """This is extends the basic HTML parser class.
    """

    def __init__(self, formatter, verbose=None):
        if verbose and not hasattr(verbose, "write"):
            verbose = sys.stderr
        htmllib.HTMLParser.__init__(self, formatter, verbose)
        # consists of [tables][rows][cols]
        # where reparsestack[-1] is the deepest replayable elt
        self.reparsestack = []
        # the current dt element somewhere in tablestack
        self.tdelt = []


    # Manage a replay buffer, with self.tdelt being our current hdr/data block

    def handle_data(self, data):
        if len(self.reparsestack):
            self.reparsestack[-1].append((getattr(self, 'handle_data'), data,))
        htmllib.HTMLParser.handle_data(self, data)

    def handle_starttag(self, tag, method, attrs):
        if self.reparsestack:
            self.reparsestack[-1].append((method, attrs,))
        htmllib.HTMLParser.handle_starttag(self, tag, method, attrs)

    def handle_endtag(self, tag, method):
        if self.tdelt:
            self.tdelt[-1].append((method,))
        htmllib.HTMLParser.handle_endtag(self, tag, method)


    def do_p(self, attr):
        self.formatter.end_paragraph(1)

    def end_p(self):
        self.formatter.end_paragraph(1)

    def start_div(self, attr):
        self.formatter.end_paragraph(0)

    def end_div(self):
        self.formatter.end_paragraph(0)

    def start_center(self, attr):
        self.formatter.end_paragraph(0)

    def end_center(self):
        self.formatter.end_paragraph(0)

    def add_label_data(self, format, counter, blankline=None):
        self.formatter.add_flowing_data()

    def do_dd(self, attrs):
        self.ddpop()
        self.formatter.push_margin('dd')
        self.list_stack.append(['dd', '', 0])

    def end_dd(self):
        self.ddpop()

    def end_dt(self):
        self.ddpop()

    def end_li(self):
        self.formatter.end_paragraph(0)

    def start_table(self, attr):
        self.formatter.end_paragraph(0)

    def end_table(self):
        self.formatter.end_paragraph(0)

    def start_tr(self, attr):
        self.formatter.end_paragraph(0)

    def end_tr(self):
        self.formatter.end_paragraph(0)

    def start_tr(self, attr):
        self.formatter.end_paragraph(0)

    def end_tr(self):
        self.formatter.end_paragraph(0)

    def do_th(self, attr):
        self.formatter.add_column_break(attr)

    def end_th(self):
        self.atbreak = 1

    def do_td(self, attr):
        self.formatter.add_column_break(attr)

    def end_td(self):
        self.atbreak = 1


    def unknown_starttag(self, tag, attrs):
        if self.verbose:
            self.verbose.write('\n*** Stack:' + '\n'.join(self.stack))
            self.verbose.write('\n*** Unrecognized <' + tag + '>\n')

    def unknown_endtag(self, tag):
        if self.verbose:
            self.verbose.write('\n*** Stack:' + '\n'.join(self.stack))
            self.verbose.write('\n*** Unrecognized </' + tag + '>\n')

    def report_unbalanced(self, tag):
        if self.verbose:
            self.verbose.write('\n*** Stack:' + '\n'.join(self.stack))
            self.verbose.write('\n*** Unbalanced </' + tag + '>\n')



if __name__ == '__main__':
    verbose = False
    fi = sys.stdin
    fo = sys.stdout
    args = sys.argv[1:]
    if '-v' in args:
        verbose = True
        del args[args.index('-v')]
    if len(args):
        fi = open(args[0], 'r')
        del args[0]
    if len(args):
        fo = open(args[0], 'w')
        del args[0]
    w = DimWriter(fo, 36)
    s = ObtuseFormatter(w)
    p = HTMLPlusParser(s, verbose)
    t = fi.read()
    p.feed(t)
    p.close()
    w.flush()
