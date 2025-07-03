#AST Generator

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ast = []

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def advance(self):
        self.pos += 1

    def parse(self):
        while self.pos < len(self.tokens):
            token = self.peek()
            if token[0] == 'ID':
                if token[1] == 'say':
                    self.ast.append(self.parse_say())
                else:
                    self.ast.append(self.parse_var_assign())
            else:
                self.error(f"Unexpected token {token}")
        return self.ast
    
    def parse_var_assign(self):
        name = self.expect('ID')[1]
        self.expect('EQUALS')
        datatype = self.expect('ID')[1]
        self.expect('LPAREN') # (

        if datatype == 'string':
            value_token = self.expect('STRING')
        elif datatype == 'int':
            value_token = self.expect('INT')
        else:
            self.error("Unexpected datatype")

        value = value_token[1].strip('"') #remove quotes
        self.expect('RPAREN') #)
        return {
            "type": "var_assign",
            "name": name,
            "datatype": datatype,
            "value": value
        }
    
    def parse_say(self): #allowing say("custom text")
        self.expect('ID')                    
        self.expect('LPAREN')                 

        token = self.peek()
        if token[0] == 'ID':
            value = self.expect('ID')[1]
            value_type = 'variable'
        elif token[0] == 'STRING':
            value = self.expect('STRING')[1].strip('"')  # remove quotes
            value_type = 'string'
        else:
            self.error(f"Expected variable name or string, got {token}")

        self.expect('RPAREN')                 # )

        return {
            "type": "say",
            "value": value,
            "value_type": value_type
        }

    def expect(self, expected_type):
        token = self.peek()
        if token is None or token[0] != expected_type:
            self.error(f"Expected {expected_type}, got {token}")
        self.advance()
        return token

    def error(self, message):
        raise SyntaxError(message)