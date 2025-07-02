# main
from lang.lexer import Tokenizer
from lang.parser import Parser
from lang.interpreter import Interpreter


source_code_path = 'examples/hello.txt'



def run(debug):
    with open(source_code_path, 'r') as f:
        source_code = f.read()
    
    lexer = Tokenizer(source_code)
    tokens = lexer.tokenize()
    if debug == 'on':
        print("=== Tokens ===")
        print(tokens)
        print(" ")
    else:
        pass

    parser = Parser(tokens)
    ast = parser.parse()
    if debug == 'on':
        print("=== AST ===")
        for node in ast:
            print(node)
        print(" ")
    else:
        pass
    

    if debug:
        print("=== OUTPUT === (Debug enabled!)")
    else:
        print("=== OUTPUT ===")
    interpreter = Interpreter(ast)
    interpreter.run()


if __name__ == "__main__":
    run(debug='on') #debug for logs (on / off)