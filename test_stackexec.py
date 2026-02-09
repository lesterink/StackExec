# test_stackexec.py
"""
Tests for StackExec module.
"""

import unittest
from stackexec import StackExec

class TestStackExec(unittest.TestCase):
    """Test cases for StackExec class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StackExec()
        self.assertIsInstance(instance, StackExec)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StackExec()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
