from textparser import Parser,re
parser = Parser(line_sep=r'[\{\[].*[\}|\]](?:"|[^"])*',flags=re.MULTILINE) #default line_sep='\n'


@parser._(r'(?:"|[^"])*')
def parse_dict()
