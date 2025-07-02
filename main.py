# main
from lang.lexer import Tokenizer
from lang.parser import Parser


source_code_path = 'examples/hello.txt'

if __name__ == "__main__":
    with open(source_code_path, 'r') as f:
        source_code = f.read()
    
    lexer = Tokenizer(source_code)
    tokens = lexer.tokenize()
    print("=== Tokens ===")
    print(tokens)

    parser = Parser(tokens)
    ast = parser.parse()
    print("=== AST ===")
    for node in ast:
        print(node)