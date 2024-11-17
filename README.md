# Diamonds

A Python project that generates artistic diamond shapes of various sizes. This project is both a fun way to learn Python and a demonstration of basic shape-generation logic.

## Features

- Generates both **outline diamonds** and **filled diamonds**.
- Customizable sizes for diamonds.
- Modular design for easy extension and integration.
- Includes automated tests to ensure functionality.

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- **Python 3.6+**  
  Ensure Python is installed on your system. Check your version:
  ```bash
  python --version
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/diamonds.git
   cd diamonds
   ```

2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the project with:
```bash
python main.py
```

The program will display both outline and filled diamonds of various sizes.

---

## Project Structure

```
diamonds/
│
├── diamonds/             # Core module for diamond logic
│   ├── __init__.py       # Module initialization
│   ├── diamonds.py       # Functions for generating diamonds
│
├── tests/                # Automated test files
│   ├── test_diamonds.py  # Unit tests for diamonds module
│
├── config.py             # Configurable constants for the project
├── main.py               # Entry point of the program
└── requirements.txt      # Dependencies for the project
```

---

## Configuration

You can configure the range of diamond sizes in the `config.py` file:
```python
# Range of diamond sizes to display
DIAMOND_SIZES = range(0, 6)
```

Modify `DIAMOND_SIZES` to display larger or smaller diamonds.

---

## Testing

Run unit tests to ensure everything is working correctly:
```bash
python -m unittest discover tests
```

The test suite will validate the behavior of diamond-generation functions.

---

## Contributing

Contributions are welcome!  
1. Fork the repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by [Al Sweigart](https://nostarch.com/big-book-small-python-projects) and his work on Python projects.
- Thanks to the Python community for fostering creativity and fun in coding.
