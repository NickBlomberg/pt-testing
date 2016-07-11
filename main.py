import unittest
from test import LoginTestCase, DashboardTestCase, ProjectFormTestCase

all_tests = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(LoginTestCase),
    unittest.TestLoader().loadTestsFromTestCase(DashboardTestCase),
    unittest.TestLoader().loadTestsFromTestCase(ProjectFormTestCase),
])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=3).run(all_tests)
