# -*- coding: utf-8 -*-

import codecs

class DataFile:
    
    def __init__(self, path):
        self.f = codecs.open(path, 'w', 'utf-8')
        self.f.write("SoftwareName,isMalware,Feature\n")
    
    def append(self, name, isMalware, feature):
        self.f.write(
                "".join([name, ",", str(isMalware), ",", feature,  "\n"])
                ) 
    
    def close(self):
        self.f.close()
