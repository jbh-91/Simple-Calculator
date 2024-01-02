import unittest
from calculator import calculator


class TestCalculatorMethods(unittest.TestCase):
    
    tc = calculator.Calculator()

    def test_addition(self):
        self.assertEqual(self.tc.calculate("123.45 + 670.89"), 794.34)
    
    def test_substraction(self):
        self.assertAlmostEqual(self.tc.calculate("670.89 - 123.45"), 547.44)
    
    def test_multiplication(self):
        self.assertEqual(self.tc.calculate("123.45 * 670.89"), 82821.3705)
    
    def test_division(self):
        self.assertEqual(self.tc.calculate("123.45 / 670.89"), 0.18400930107767294)
    
    def test_exponentiation(self):
        # 2nd to 9tg potentiation 
        err_msg = "result of potentiation calculation is wrong"

        self.assertEqual(self.tc.calculate("123.4567809 ** 2"), 15241.576750190605, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** 3"), 1881676.0014188155, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** 4"), 232305661.83195078, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** 5"), 28679709194.616642, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** 6"), 3540704574315.502, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** 7"), 437123988862896.7, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** 8"), 5.396592051918067e+16, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** 9"), 6.662458825603302e+18, err_msg)

        # square root
        self.assertEqual(self.tc.calculate("123.4567809 ** (1/2)"), 11.111110696055547, 
                         "result of square root claculation is wrong")

        # qubic root
        self.assertEqual(self.tc.calculate("123.4567809 ** (1/3)"), 4.979338483283606, 
                         "result of qubic root claculation is wrong")
        
        # 4th to 9th root 
        err_msg = "result of root is wrong"

        self.assertEqual(self.tc.calculate("123.4567809 ** (1/4)"), 3.333333271074998, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** (1/5)"), 2.620010246173881, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** (1/6)"), 2.2314431391553775, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** (1/7)"), 1.9897011447521342, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** (1/8)"), 1.8257418413004063, err_msg)
        self.assertEqual(self.tc.calculate("123.4567809 ** (1/9)"), 1.7076173150528808, err_msg)

    def test_division_by_zero_caught(self):
        # TODO: rework with asserRaise or something
        self.assertEqual(self.tc.validate("10 / 0 "), "<class 'ZeroDivisionError'>: division by zero!")

    def test_operations_hirarchy(self):
        # PEMDAS: Parentheses, Exponents, Multiplication/Division,
        #         Addition/Subtraction from left to right.
        self.assertEqual(self.tc.calculate("10 + 15 * (3 - 8) ** 5"), -46865, "order of operation is violated")


if __name__ == "__name__":
    unittest.main()