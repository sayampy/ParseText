# ParseAnyText
[![GitHub license](https://img.shields.io/github/license/sayampy/ParseAnyText)](https://github.com/sayampy/ParseAnyText/blob/main/LICENSE)

A small package to parse strings.

## What is the work of it?
<section>
Well It's a module to creates parser that helps to parse a text easily with less coding.
Like a language parsing or file parsing like json.
</section>

## How to use?
```py
from textparser import Parser
p = Parser()

@p._(r'<re.pattern>')
def function(args,kwargs):
   #<do something>
p.parse(<text>)
```
## Want to Contribute?
![](https://c.tenor.com/ikmzhcmdj6EAAAAM/looking-looking-good.gif)
<br>🙄👉👈
