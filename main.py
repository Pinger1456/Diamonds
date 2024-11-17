"""This module handles the initialization and execution of the project.
Make sure to organize imports and configurations correctly."""

from config import DIAMOND_SIZES
from diamonds.diamonds import display_outline_diamond, display_filled_diamond


def main():
    """Main function to display diamonds of various sizes."""
    print('Diamonds Project')
    for size in DIAMOND_SIZES:
        print(f"\nOutline Diamond (Size {size}): ")
        display_outline_diamond(size)
        print(f"\nFilled Diamond (Size {size}): ")
        display_filled_diamond(size)


if __name__ == "__main__":
    main()
