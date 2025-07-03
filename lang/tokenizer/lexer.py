# Tokenizer
import re
from .tokens import TOKEN_TYPES


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
            if kind in ('SKIP', 'COMMENT'):  # Skip whitespace and comments
                continue
            elif kind == 'NEWLINE':
                self.line += 1
            else:
                self.tokens.append((kind, value, self.line))
    
        return self.tokens
