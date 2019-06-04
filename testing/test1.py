import unittest

def DrinkAndDrive(age):
    return True

class TestScript(unittest.TestCase):
    def test_1(self):
    # it should always return False
        self.assertFalse(DrinkAndDrive(99),
                         "99 is not old enough to drink and drive.")
if __name__ == '__main__':
    print(DrinkAndDrive(99))
    unittest.main()
