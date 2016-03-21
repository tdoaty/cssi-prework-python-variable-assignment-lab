import sys
import unittest

from variable import * 

class TestVariable(unittest.TestCase):

    def testGreeting(self):
      self.assertEqual(greeting, "Hello World")

if __name__ == '__main__':
    unittest.main()
