import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 23.7)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(23.7)) 

    def test_individual_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 1.2),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 4.5)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(1.2), NumberNode(4.5))) 

        tokens = [
            Token(TokenType.NUMBER, 1.2),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 4.5)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(1.2), NumberNode(4.5))) 

        tokens = [
            Token(TokenType.NUMBER, 1.2),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 4.5)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(1.2), NumberNode(4.5))) 

        tokens = [
            Token(TokenType.NUMBER, 1.2),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 4.5)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(1.2), NumberNode(4.5))) 

    def test_full_expression(self):
        tokens = [
            # 27 + (43 / 36 - 48) * 51
            Token(TokenType.NUMBER, 27.0),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 43.0),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 36.0),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 48.0),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 51.0)
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, 
            AddNode(
                NumberNode(27.0), 
                MultiplyNode(
                    SubtractNode(
                        DivideNode(
                            NumberNode(43.0), 
                            NumberNode(36.0)
                        ),
                        NumberNode(48.0)
                    ), 
                    NumberNode(51.0)
                )
            )
        )

if __name__ == '__main__':
    unittest.main()