#ast nodes clasiffier
class VarAssign:
    def __init__(self, name, datatype, value):
        self.name = name
        self.datatype = datatype
        self.value = value

    def __repr__(self):
        return f"VarAssign(name={self.name!r}, datatype={self.datatype!r}, value={self.value!r})"

class Say:
    def __init__(self, value, value_type):
        self.value = value
        self.value_type = value_type

    def __repr__(self):
        return f"Say(value={self.value!r}, value_type={self.value_type!r})"
