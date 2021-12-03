import re
from functools import wraps

class Parser():
    patterns = {}

    def __init__(self,line_sep=r'\n'):
        self.line_sep=line_sep

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
        '''Split the text'''
        if type(self.line_sep)!=str or self.line_sep =='':
            raise Execption('SplitingLineError',
            f'''not a valid type, {type(self.line_sep)}''')
        return re.split(self.line_sep,text,maxsplit)

    def update_line(self,rx,line,func_val):
        '''Remove or replace the pattern with return function value
        Ex:
          1+2+1 = `1+2` will replaced by 3
          then 3+1 will replaced by 4
        '''
        if func_val==None:
            func_val=''
        return rx.sub(str(func_val),line,1)

    def parse(self,text):
        parsed_lines=[]
        for line in self.split_line(text):
            line=line.strip()
            for pattern, func in self.patterns.items():
                rx = re.compile(pattern)
                while rx.search(line):
                    m = rx.match(line)
                    func_val = func(*m.groups(), **m.groupdict())
                    line=self.update_line(rx,line,func_val)
            parsed_line.append(line)
        return '\n'.join(parsed_lines)
