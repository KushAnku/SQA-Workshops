# WorkShop_2
# Ankush Singh 

import unittest
import source

class TestAddition(unittest.TestCase):
    # Tests for addition operation
    def testAddition1(self): 
        self.assertEqual(3, source.performAdd(2, 1), "Error in implementation.")

    def testAddition2(self):
        self.assertEqual(101, source.performAdd(100, 1), "Error again!") 

class TestSubtraction(unittest.TestCase):
    # Tests for subtraction operation
    def testSub1(self):
        self.assertEqual(5, source.performSub(10, 5), "Error!")

    def testSub2(self):
        self.assertEqual(-1, source.performSub(5, 6), "Error in subtraction.")

class TestMultiplication(unittest.TestCase):
    # Tests for multiplication operation
    def testMultiplication1(self):
        self.assertEqual(source.performMul(10, 5), 50, "Error in multiplication.")

    def testMultiplication2(self):
        self.assertEqual(source.performMul(-3, 4), -12, "Error again in multiplication.")

class TestDivision(unittest.TestCase):
    # Tests for division operation
    def testDivision1(self):
        self.assertEqual(source.performDiv(10, 2), 5, "Error in division.")

    def testDivision2(self):
        self.assertEqual(source.performDiv(9, 3), 3, "Error again in division.")

    # Test for division by zero exception
    def testDivisionByZero(self):
        with self.assertRaises(ValueError, msg="Cannot divide by zero"):
            source.performDiv(10, 0)

if __name__ == '__main__': 
    unittest.main()
