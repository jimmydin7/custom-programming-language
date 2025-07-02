# main
from lang.lexer import Tokenizer

source_code_path = 'examples/hello.txt'

if __name__ == "__main__":
    with open(source_code_path, 'r') as f:
        source_code = f.read()
    
    lexer = Tokenizer(source_code)
    tokens = lexer.tokenize()

    for token in tokens:
        print(token)
