from .environment import Environment
from ..parser.ast_nodes import VarAssign, Say, Repeat, BinOp, If, Function, FunctionCall

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.env = Environment()

    def run(self):
        for node in self.ast:
            self.execute(node)

    def eval_node(self, node):
        if isinstance(node, BinOp):
            left = self.eval_node(node.left)
            right = self.eval_node(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left // right 
            elif node.op == '>':
                return left > right
            elif node.op == '<':
                return left < right
            elif node.op == '>=':
                return left >= right
            elif node.op == '<=':
                return left <= right
            elif node.op == '==':
                return left == right
            elif node.op == '!=':
                return left != right
            else:
                raise RuntimeError(f"Unknown operator: {node.op}")
        elif isinstance(node, int):
            return node
        elif isinstance(node, str):

            try:
                return self.env.get_variable(node)
            except Exception:
                return node
        else:
            return node

    def execute(self, node):
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
                value = self.eval_node(value)
            self.env.set_variable(node.name, value)

        elif isinstance(node, Repeat):
            for _ in range(node.count):
                for stmt in node.body:
                    self.execute(stmt)
        elif isinstance(node, If):
            condition_result = self.eval_node(node.condition)
            if condition_result:
                for stmt in node.body:
                    self.execute(stmt)
        elif isinstance(node, Function):
            self.env.set_function(node.name, node)
        elif isinstance(node, FunctionCall):
            function = self.env.get_function(node.name)
            for stmt in function.body:
                self.execute(stmt)
        else:
            raise RuntimeError(f"Unknown AST node type: {type(node)}")
