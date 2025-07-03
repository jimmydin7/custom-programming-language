# Variable storage

class Environment():
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        raise NameError(f"Variable '{name}' is not defined")