# Beispiel aus der VL
import fib
import unittest

class FibTest(unittest.TestCase):

    def testFibonacci(self):
        self.assertEqual(fib.fib(0), 0, "Tested fib(0)=0")
        self.assertEqual(fib.fib(1), 1, "Tested fib(1)=0")
        self.assertEqual(fib.fib(2), 1, "Tested fib(2)=1")
