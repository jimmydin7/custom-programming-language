# Tokenizer
import re

TOKEN_TYPES = [
    ("STRING", r'"[^"]*"'),
    ("INT", r'\d+'),
    ("ID", r'[a-zA-Z_]\w*'),
    ("EQUALS", r'='),
    ("LPAREN", r'\('),
    ("RPAREN", r'\)'),
    ("COMMA", r','),
    ("NEWLINE", r'\n'),
    ("SKIP", r'[ \t]+') 
]

class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.pos = 0
        self.line = 1

    def tokenize(self):
        pattern = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_TYPES)
        regex = re.compile(pattern)
        for match in regex.finditer(self.source):
            kind = match.lastgroup
            value = match.group()
            if kind == 'SKIP':
                continue
            elif kind == 'NEWLINE':
                self.line += 1
            else:
                self.tokens.append((kind, value, self.line))
            
        return self.tokens