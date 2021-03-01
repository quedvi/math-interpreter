from lexer import Lexer

while True:
    text = input("clac >")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    print(list(tokens))
