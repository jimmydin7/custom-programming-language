TOKEN_TYPES = [
    ('COMMENT',   r'#.*'),
    ('ID',        r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('EQUALS',    r'='),
    ('INT',       r'\d+'),
    ('STRING',    r'"[^"]*"'),
    ('LPAREN',    r'\('),
    ('RPAREN',    r'\)'),
    ('NEWLINE',   r'\n'),
    ('SKIP',      r'[ \t]+'),
    ('MISMATCH',  r'.'),
]
