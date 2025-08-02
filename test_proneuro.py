# test_proneuro.py
"""
Tests for ProNeuro module.
"""

import unittest
from proneuro import ProNeuro

class TestProNeuro(unittest.TestCase):
    """Test cases for ProNeuro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProNeuro()
        self.assertIsInstance(instance, ProNeuro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProNeuro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
