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
    

class Repeat:
    def __init__(self, count, body):
        self.count = count
        self.body = body

    def __repr__(self):
        return f"Repeat(count={self.count!r}, body={self.body!r})"

class BinOp: #binary operations
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __repr__(self):
        return f"BinOp(left={self.left!r}, op={self.op!r}, right={self.right!r})"

class If:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"If(condition={self.condition!r}, body={self.body!r})"