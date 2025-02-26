import unittest
from src.project_setup import setup_project

class TestProjectSetup(unittest.TestCase):
    def test_setup_project(self):
        self.assertIsNone(setup_project())

if __name__ == "__main__":
    unittest.main()