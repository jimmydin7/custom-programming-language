import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from lang.parser import Parser

def test_parse_var_assign():
    tokens = [
        ('ID', 'x', 1),
        ('EQUALS', '=', 1),
        ('ID', 'int', 1),
        ('LPAREN', '(', 1),
        ('INT', '5', 1),
        ('RPAREN', ')', 1)
    ]
    parser = Parser(tokens)
    ast = parser.parse()

    expected = [{
        "type": "var_assign",
        "name": "x",
        "datatype": "int",
        "value": "5"
    }]
    assert ast == expected
    