r"""Diamonds, by Al Sweigart al@inventwithpython.com
Draws diamonds of various sizes.
View this code at
https://nostarch.com/big-book-small-python-projects
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
Tags: tiny, beginner, artistic"""


def display_outline_diamond(size):
    """Displays an outline diamonds of the given size."""
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left side space.
        print('/', end='')  # Left side of diamonds.
        print(' ' * (i * 2), end='')  # Interior of diamonds.
        print('\\')  # Right side of diamonds.

    for i in range(size):
        print(' ' * i, end='')  # Left side space.
        print('\\', end='')  # Left side of diamonds.
        print(' ' * ((size - i - 1) * 2), end='')  # Interior of diamonds.
        print('/')  # Right side of diamonds.


def display_filled_diamond(size):
    """Displays a filled diamonds of the given size."""
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left side space.
        print('/' * (i + 1), end='')  # Left half of diamonds.
        print('\\' * (i + 1))  # Right half of diamonds.

    for i in range(size):
        print(' ' * i, end='')  # Left side space.
        print('\\' * (size - i), end='')  # Left side of diamonds.
        print('/' * (size - i))  # Right side of diamonds.
