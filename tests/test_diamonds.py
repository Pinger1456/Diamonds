"""
Unit tests for the diamonds module.
This file tests the functionality of the functions
that generate diamond shapes.
"""

import unittest
from diamonds.diamonds import display_outline_diamond, display_filled_diamond


class TestDiamonds(unittest.TestCase):
    """Test cases for the diamonds module."""

    def test_display_outline_diamond(self):
        """Test that the outline diamond function
           runs without errors for a valid size."""
        try:
            display_outline_diamond(3)
        except ValueError as ve:
            self.fail(f"display_outline_diamond raised ValueError: {ve}")
        except TypeError as te:
            self.fail(f"display_outline_diamond raised TypeError: {te}")

    def test_display_filled_diamond(self):
        """Test that the filled diamond function
           runs without errors for a valid size."""
        try:
            display_filled_diamond(3)
        except ValueError as ve:
            self.fail(f"display_filled_diamond raised ValueError: {ve}")
        except TypeError as te:
            self.fail(f"display_filled_diamond raised TypeError: {te}")


if __name__ == '__main__':
    unittest.main()
