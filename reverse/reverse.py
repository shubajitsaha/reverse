class ReverseFile:
    def __init__(self,filename, sep=' ',encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding
        if len(sep) != 1:
            raise ValueError('separator should be a single character')
        self.separator = sep
        
    def _read_file(self):
        with open(self.filename,'r',encoding=self.encoding) as fip:
            text = fip.read()
        return text
    
    def _split(self,text):
        return text.split(self.separator)
    
    def _reverse(self,text):
        return ''.join([text[id] for id in range(len(text)-1,-1,-1)])
    
    def _join(self,text_list):
        return self.separator.join(text_list)
    
    def reverse(self):
        
        self.text = self._read_file()
        
        segments = self._split(self.text)
        for i in range(len(segments)):
            segments[i] = self._reverse(segments[i])
            
        self.revrsed_text = self._join(segments)
        
        return self.revrsed_text
    
    def write(self,filename):
        with open(filename,'w',encoding=self.encoding) as fop:
            fop.write(self.revrsed_text)
            