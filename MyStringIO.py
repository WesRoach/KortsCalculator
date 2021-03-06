# coding = utf-8

# MyStringIO.py: Kort's Spellcrafting Calculator (main Window)
#
# See http://www.github.com/artomason/KortsCalculator/ for updates
#
# See NOTICE.txt for copyrights and grant of license


import codecs
import html.entities
import io
import re
import string

entity_map = {}

for i in range(256):
    entity_map[chr(i)] = "&%d;" % i

for entity, char in list(html.entities.entitydefs.items()):

    if char in entity_map:
        entity_map[char] = "&%s;" % entity


def escape_entity(m):
    get = entity_map.get
    l1 = codecs.getencoder('latin-1')
    return str.join(list(map(get, l1(m.group())[0])), "")


def unicodeEscape(string):
    pattern = re.compile(r"[&<>\"\x80-\xff]+")
    return pattern.sub(escape_entity, string)


def unicodeHtmlEscape(string):
    pattern = re.compile(r"[&\"\x80-\xff]+")
    return pattern.sub(escape_entity, string)


class UnicodeStringIO(io.StringIO):  # THIS IS PROBABLY NOT NECESSARY SINCE UNICODE IS STR DEFAULT
    def __init__(self):
        io.StringIO.__init__(self)

    def write(self, strval, escape=False):
        io.StringIO.write(self, strval)
        return
