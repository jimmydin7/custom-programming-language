# Variable storage

class Environment():
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        raise NameError(f"Variable '{name}' is not defined")

    def set_function(self, name, function):
        self.functions[name] = function

    def get_function(self, name):
        if name in self.functions:
            return self.functions[name]
        raise NameError(f"Function '{name}' is not defined")