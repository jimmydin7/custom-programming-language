#AST Generator
from .ast_nodes import VarAssign, Say, Repeat, BinOp, If, Function, FunctionCall
from helpers.utils import *

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
                elif token[1] == 'repeat':
                    self.ast.append(self.parse_repeat())
                elif token[1] == 'if':
                    self.ast.append(self.parse_if())
                elif token[1] == 'function':
                    self.ast.append(self.parse_function())
                elif token[1] == 'call':
                    self.ast.append(self.parse_function_call())
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
            value = value_token[1].strip('"')
        elif datatype == 'int':
            value = self.parse_expression()  # Parse a full expression for int
        else:
            self.error("Unexpected datatype")

        self.expect('RPAREN') #)
        return VarAssign(name, datatype, value)

    
    def parse_say(self): #allowing say("custom text")
        self.expect('ID')                    
        self.expect('LPAREN')                 

        token = self.peek()
        if token[0] == 'ID':
            value = self.expect('ID')[1]
            value_type = 'variable'
        elif token[0] == 'STRING':
            raw_value = self.expect('STRING')[1]  
            value = strip_quotes(raw_value)     
            value_type = 'string'
        else:
            self.error(f"Expected variable name or string, got {token}")

        self.expect('RPAREN')                 # )

        return Say(value, value_type)

    def parse_repeat(self):
        self.expect('ID')  # 'repeat'
        count_token = self.expect('INT')
        count = int(count_token[1])
        self.expect('LBRACE')

        body = []
        while self.peek() and self.peek()[0] != 'RBRACE':
            token = self.peek()
            if token[0] == 'ID':
                if token[1] == 'say':
                    body.append(self.parse_say())
                elif token[1] == 'repeat':
                    body.append(self.parse_repeat())
                elif token[1] == 'if':
                    body.append(self.parse_if())
                else:
                    body.append(self.parse_var_assign())
            else:
                self.error(f"Unexpected token {token} in repeat body")

        self.expect('RBRACE')
        return Repeat(count, body)

    def parse_expression(self):
        node = self.parse_term()
        while self.peek() and self.peek()[0] in ('PLUS', 'MINUS'):
            op_token = self.expect(self.peek()[0])
            right = self.parse_term()
            node = BinOp(node, op_token[1], right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.peek() and self.peek()[0] in ('STAR', 'SLASH'):
            op_token = self.expect(self.peek()[0])
            right = self.parse_factor()
            node = BinOp(node, op_token[1], right)
        return node

    def parse_factor(self):
        token = self.peek()
        if token[0] == 'INT':
            return int(self.expect('INT')[1])
        elif token[0] == 'ID':
            return self.expect('ID')[1]
        elif token[0] == 'LPAREN':
            self.expect('LPAREN')
            node = self.parse_expression()
            self.expect('RPAREN')
            return node
        else:
            self.error(f"Unexpected token in factor: {token}")

    

    def expect(self, expected_type):
        token = self.peek()
        if token is None or token[0] != expected_type:
            self.error(f"Expected {expected_type}, got {token}")
        self.advance()
        return token

    def error(self, message):
        raise SyntaxError(message)

    def parse_condition(self):
        left = self.parse_expression()
        op_token = self.peek()
        if op_token[0] in ('EQ', 'NEQ', 'GTE', 'LTE', 'GT', 'LT'):
            op = self.expect(op_token[0])[1]
            right = self.parse_expression()
            return BinOp(left, op, right)
        else:
            self.error(f"Expected comparison operator, got {op_token}")

    def parse_if(self):
        self.expect('ID')  # 'if'
        condition = self.parse_condition()
        self.expect('LBRACE')
        body = []
        while self.peek() and self.peek()[0] != 'RBRACE':
            token = self.peek()
            if token[0] == 'ID':
                if token[1] == 'say':
                    body.append(self.parse_say())
                elif token[1] == 'repeat':
                    body.append(self.parse_repeat())
                elif token[1] == 'if':
                    body.append(self.parse_if())
                else:
                    body.append(self.parse_var_assign())
            else:
                self.error(f"Unexpected token {token} in if body")
        self.expect('RBRACE')
        return If(condition, body)

    def parse_function(self):
        self.expect('ID')  # 'function'
        name = self.expect('ID')[1]
        self.expect('LBRACE')
        
        body = []
        while self.peek() and self.peek()[0] != 'RBRACE':
            token = self.peek()
            if token[0] == 'ID':
                if token[1] == 'say':
                    body.append(self.parse_say())
                elif token[1] == 'repeat':
                    body.append(self.parse_repeat())
                elif token[1] == 'if':
                    body.append(self.parse_if())
                elif token[1] == 'function':
                    body.append(self.parse_function())
                elif token[1] == 'call':
                    body.append(self.parse_function_call())
                else:
                    body.append(self.parse_var_assign())
            else:
                self.error(f"Unexpected token {token} in function body")
        
        self.expect('RBRACE')
        return Function(name, body)

    def parse_function_call(self):
        self.expect('ID')  # 'call'
        self.expect('LPAREN')
        name = self.expect('ID')[1]
        self.expect('RPAREN')
        return FunctionCall(name)