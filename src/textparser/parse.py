import re
from functools import wraps,partial
#from test1 import _pattern

'''
class ParserMeta(type):
    @classmethod
    def __prepare__(meta,*args,**kwargs):
        return {'_':_pattern}'''

class Parser():
    def __init__(self,line_sep=r'\n'):
        self.line_sep=line_sep

    patterns = {}
    def p(self,re_pattern,*args,**kwargs):
        '''Creates re pattern to parse'''
        def new_func(func):
            self.patterns[re_pattern]=func

            @wraps(func)
            def wrapper(*args,**kwargs):
                return func(self,*args,**kwargs)
            return wrapper
        return new_func

    def split_line(self,text,maxsplit=0):
        '''Split the tex to restart pattern matching'''
        if type(self.line_sep)!=str or self.line_sep =='':
            raise Execption('SplitingLineError',
            f'''not a valid type, {type(self.line_sep)}''')
        return re.split(self.line_sep,text,maxsplit)
    
    def update_line(self,rx,line,func_val):
        if func_val==None:
            func_val=''
        return rx.sub(str(func_val),line,1)

    def parse(self,text):
        for line in self.split_line(text):
            line=line.strip()
            for pattern, func in self.patterns.items():
                rx = re.compile(pattern)
                while rx.search(line):
                    m = rx.match(line)
                    func_val = func(*m.groups(), **m.groupdict())
                    line=self.update_line(rx,line,func_val)


# Test
parser = Parser()

digit = r'-?\d+'
@parser.p(r'({digit})\s*\+\s*({digit})'.format(digit=digit))
def add(*nums):
    return sum(map(int,nums))
@parser.p(r'({digit})'.format(digit=digit))
def expr(num):
    print(num)
res = parser.parse('-2+3+2+2')
