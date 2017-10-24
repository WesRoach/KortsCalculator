import StringIO
import string
import htmlentitydefs, re
import codecs

entity_map = {}
for i in range(256):
    entity_map[chr(i)] = "&%d;" % i
for entity, char in htmlentitydefs.entitydefs.items():
    if entity_map.has_key(char):
        entity_map[char] = "&%s;" % entity

def escape_entity(m):
    get = entity_map.get
    l1 = codecs.getencoder('latin-1')
    return string.join(map(get, l1(m.group())[0]), "")

def unicodeEscape(string):
    pattern = re.compile(r"[&<>\"\x80-\xff]+")
    return pattern.sub(escape_entity, string)

def unicodeHtmlEscape(string):
    pattern = re.compile(r"[&\"\x80-\xff]+")
    return pattern.sub(escape_entity, string)

class UnicodeStringIO(StringIO.StringIO):
    def __init__(self):
        StringIO.StringIO.__init__(self)

    def write(self, string, escape=False):
        StringIO.StringIO.write(self, string.encode('UTF-8'))
        return 
#        pattern = re.compile(r"[&<>\"\x80-\xff]+")
#        if escape:
#            StringIO.StringIO.write(self, pattern.sub(escape_entity, string))
#        else:
#            StringIO.StringIO.write(self, string)





# this pattern matches substrings of reserved and non-ASCII characters

# create character map





