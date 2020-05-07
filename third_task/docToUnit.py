import unittest
import doctest
import third_task

def load_tests(loader, tests, ignore):
 tests.addTests(doctest.DocTestSuite(third_task))
 TestRunner().run(tests)
 return tests
 