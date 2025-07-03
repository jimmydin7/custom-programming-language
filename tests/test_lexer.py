import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from lang.tokenizer.lexer import Tokenizer

def test_tokenize_variable_assignment():
    source = 'x = int(5)'
    tokenizer = Tokenizer(source)
    tokens = tokenizer.tokenize()

    expected = [
        ('ID', 'x', 1),
        ('EQUALS', '=', 1),
        ('ID', 'int', 1),
        ('LPAREN', '(', 1),
        ('INT', '5', 1),
        ('RPAREN', ')', 1)
    ]
    assert tokens == expected
    
