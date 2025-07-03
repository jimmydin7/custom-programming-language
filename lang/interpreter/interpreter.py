from .environment import Environment
from ..parser.ast_nodes import VarAssign, Say

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.env = Environment()

    def run(self):
        for node in self.ast:
            if isinstance(node, Say):
                if node.value_type == 'variable':
                    value = self.env.get_variable(node.value)
                    print(value)
                elif node.value_type == 'string':
                    print(node.value)
                else:
                    raise RuntimeError(f"Unknown value_type: {node.value_type}")

            elif isinstance(node, VarAssign):
                value = node.value
                if node.datatype == 'int':
                    value = int(value)
                self.env.set_variable(node.name, value)

            else:
                raise RuntimeError(f"Unknown AST node type: {type(node)}")
