import unittest
from nodes import *
from interpreter import Interpreter
from values import Number

class TestInterpreter(unittest.TestCase):

    def test_number(self):
        value = Interpreter().visit(NumberNode(23.5))
        self.assertEqual(value, Number(23.5))

    def test_individual_operations(self):
        value = Interpreter().visit(AddNode(NumberNode(27), NumberNode(12)))
        self.assertEqual(value, Number(39))

        value = Interpreter().visit(SubtractNode(NumberNode(27), NumberNode(12)))
        self.assertEqual(value, Number(15))

        value = Interpreter().visit(MultiplyNode(NumberNode(7), NumberNode(2)))
        self.assertEqual(value, Number(14))

        value = Interpreter().visit(DivideNode(NumberNode(8), NumberNode(2)))
        self.assertAlmostEqual(value, Number(4), 5)

        with self.assertRaises(Exception):
            Interpreter().visit(DivideNode(NumberNode(8), NumberNode(0)))

    def test_full_expression(self):
        tree = AddNode(
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
        result = Interpreter().visit(tree)
        self.assertAlmostEqual(result.value, -2360.08, 2)