import re


class FileReader(object):

    def __init__(self, pattern, negpat=None, item_visit=None):
        self.re = re.compile(pattern)
        if negpat:
            self.nre = re.compile(negpat)
        else:
            self.nre = None
        self.item_visit = None or item_visit

    def process_file(self, f):
        items = []
        count = 0
        for l in f:
            rem = self.re.search(l)
            line_ok = False
            if rem:
                line_ok = True
                if self.nre:
                    if self.nre.search(l):
                        line_ok = False
            if not line_ok:
                count += 1
                continue

            line_data = {'line': count, 'text': l.strip('\n').strip(),
                         'span': rem.span(), 'file': f.name}
            items.append(line_data)
            if self.item_visit:
                self.item_visit(line_data)
            count += 1

        return items
