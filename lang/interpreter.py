#Executes the AST
from .environment import Environment

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.env = Environment()

    def run(self):
        for node in self.ast:
            if node["type"] == "say":
                if node["value_type"] == "string":
                    print(node["value"])
                elif node["value_type"] == "variable":
                    value = self.env.get_variable(node["value"])
                    print(value)

            if node["type"] == "var_assign":
                value = node["value"]
                if node["datatype"] == "int":
                    value = int(value)
                self.env.set_variable(name=node["name"], value=value)