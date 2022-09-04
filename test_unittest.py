import unittest
from arm import *

class Test_number(unittest.TestCase):
  def test_armstrongmumber(self):
    self.assertEqual(armstrongnumber(371), 371);
    self.assertEqual(armstrongnumber(1634), 1634);
    self.assertEqual(armstrongnumber(373), 373);
  if __name__ == '__main__':
    unittest.main()