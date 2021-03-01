from lexer import Lexer
from parser_ import Parser

while True:
    text = input("clac >")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)
