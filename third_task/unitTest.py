import unittest
import third_task
import doctest

def load_tests(loader, tests, ignore):
 tests.addTests(doctest.DocTestSuite(third_task))
 return tests
 
class TestFactorialFunction(unittest.TestCase):

	def test_answer1(self):
		self.assertEqual(third_task.factorial(5), 120)
		
	def test_wrong_answer(self):
		self.assertNotEqual(third_task.factorial(3), 1)
		
	def test_zero_value(self):
		with self.assertRaises(ValueError):
			third_task.factorial(0)
			
	def test_too_big_value(self):
		with self.assertRaises(OverflowError):
			third_task.factorial(1e100)

if __name__ == '__main__':
	unittest.main()
