import os
import os.path
import stat
import sys
import re

class FileFinder(object):
    def __init__(self, file_re=None, file_nre=None, visit=None):
        self.file_re = None
        self.file_nre = None
        self.visit = None or visit
        if file_re:
            self.file_re = re.compile(file_re)
        if file_nre:
            self.file_nre = re.compile(file_nre)

    def _isdir(self, f):
        try:
            statv = os.stat(f)
            mode = statv[stat.ST_MODE]
        except OSError:
            return False
        return stat.S_ISDIR(mode)

    def read_directory(self, files, recurse=True):
        all_files = []
        #print files
        for f in files:
            try:
                mode = os.stat(f)[stat.ST_MODE]
            except Exception as e:
                print e
                continue
            if stat.S_ISDIR(mode) and not stat.S_ISLNK(mode):
                try:
                    dir_list = os.listdir(f)
                except OSError as e:
                    sys.stderr.write('Error: %s\n'%(e,))
                    dir_list = []
            else:
                dir_list = [f]
            #print dir_list
            for ff in dir_list:
                if self._isdir(f):
                    ffullpath = os.path.join(f, ff)
                else:
                    ffullpath = f

                if recurse and self._isdir(ffullpath):
                    subfiles = self.read_directory([ffullpath], True)
                    all_files.extend(subfiles)
                else:
                    file_ok = True
                    if self.file_re:
                        if self.file_re.search(ffullpath):
                            file_ok = True
                        else:
                            file_ok = False
                    if self.file_nre:
                        if self.file_nre.search(ffullpath):
                            file_ok = False
                        #else:
                        #    file_ok = True
                    if file_ok:
                        all_files.append(ffullpath)
                        if self.visit:
                            self.visit(ffullpath)
        return all_files

def print_name(f):
    print f

if __name__=='__main__':
    ff = FileFinder(visit=print_name)
    initial = sys.argv[1]
    ff.read_directory([initial])




