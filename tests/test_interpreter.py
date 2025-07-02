import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from lang.interpreter import Interpreter

def test_say_statement(capsys):
    ast = [
        {'type': 'var_assign', 'name': 'x', 'datatype': 'string', 'value': 'hello'},
        {'type': 'say', 'value': 'x'}
    ]
    interpreter = Interpreter(ast)
    interpreter.run()

    captured = capsys.readouterr()
    assert captured.out.strip() == 'hello'
    
