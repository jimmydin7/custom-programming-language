#Executes the AST

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def run(self):
        for node in self.ast:
            if node["type"] == "var_assign":
                self.handle_var_assign(node)
            elif node["type"] == "say":
                self.handle_say(node)
            else:
                raise RuntimeError(f"Unknown AST node type: {node['type']}")

    def handle_var_assign(self, node):
        var_name = node["name"]
        datatype = node["datatype"]
        value = node["value"]


        if datatype == "int":
            try:
                value = int(value)
            except ValueError:
                raise RuntimeError(f"Invalid int value for {var_name}")
        elif datatype == "string":
            value = str(value)
        else:
            raise RuntimeError(f"Unknown datatype: {datatype}")

        self.variables[var_name] = value

    def handle_say(self, node):
        var_name = node["value"]
        if var_name not in self.variables:
            raise RuntimeError(f"Variable '{var_name}' not defined")
        print(self.variables[var_name])
