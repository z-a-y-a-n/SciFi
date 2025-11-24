# 🧮 Pro Scientific Calculator

A modern, feature-rich scientific calculator built with Python, featuring a sleek dark interface, symbolic computation capabilities, and real-time function plotting.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-6.5+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### 🔢 Core Functionality
- **Standard Calculations**: Basic arithmetic operations (+, −, ×, ÷)
- **Exponentiation**: Power operations with the `^` button
- **Parentheses Support**: Complex expression evaluation

### 📐 Scientific Functions
- **Trigonometric**: sin, cos, tan, asin, acos, atan
- **Logarithmic**: Natural log (ln), base-10 log (log10)
- **Other**: Square root (√), exponentiation (x², x³, eˣ)
- **Constants**: π (pi), e (Euler's number)
- **Absolute Value**: abs(x)

### 🧮 Calculus Operations
- **Differentiation**: Calculate derivatives with respect to x
- **Integration**: Compute indefinite integrals
- **Symbolic Math**: Powered by SymPy for exact symbolic computations

### 📊 Function Plotting
- **Real-time Visualization**: Plot mathematical functions in x
- **Interactive Graphs**: Matplotlib-powered plotting window
- **LaTeX Rendering**: Beautiful mathematical notation in plot titles

## 🖼️ Screenshots

### Main Calculator Interface
The calculator features a clean, modern dark theme with:
- Large, easy-to-read display
- Color-coded function buttons
- Intuitive layout

### Plotting Window
Visualize functions with:
- High-resolution plots
- Grid overlay
- LaTeX-formatted titles

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Installation

#### Using uv (Recommended)
```bash
# Clone the repository
git clone https://github.com/z-a-y-a-n/SciFi.git
cd calculator

# Install dependencies with uv
uv sync
```

#### Using pip
```bash
# Clone the repository
git clone https://github.com/z-a-y-a-n/SciFi.git
cd calculator

# Create a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# If using uv
uv run python main.py

# If using pip
python main.py
```

## 📖 Usage Guide

### Basic Calculations
1. Click number and operator buttons or type directly in the display
2. Press `=` to evaluate the expression

### Scientific Functions
1. Select a function from the right panel (e.g., `sin`)
2. Enter your value in parentheses: `sin(pi/4)`
3. Press `=` to calculate

### Calculus Operations
1. Enter an expression with variable `x`: `x**2 + 3*x + 1`
2. Click `d/dx` for derivative or `∫ dx` for integration
3. Result displays in the main screen

### Plotting Functions
1. Enter a function with variable `x`: `sin(x) + cos(2*x)`
2. Click the `Plot` button
3. A new window opens with your plotted function from x = -10 to 10

### Example Expressions
```
sin(pi/4) + 2**3          # Trigonometry and powers
(5 + 3) * 2 - 10 / 2      # Arithmetic with parentheses
ln(e**2)                   # Logarithms
sqrt(16) + abs(-5)         # Square root and absolute value
```

## 🛠️ Technical Stack

- **GUI Framework**: PySide6 (Qt for Python)
- **Symbolic Math**: SymPy
- **Plotting**: Matplotlib
- **Numerical Computing**: NumPy

## 📁 Project Structure

```
calculator/
├── main.py              # Main application file
├── pyproject.toml       # Project metadata and dependencies
├── requirements.txt     # Pip requirements
├── uv.lock             # UV lock file
└── README.md           # This file
```

## 🎨 Features Highlight

### Smart Expression Parsing
- Automatic syntax handling
- Support for Python/SymPy notation
- Real-time error detection

### Precision Output
- 15-digit numerical precision
- Automatic trailing zero removal
- Symbolic results when possible

### Modern UI/UX
- Dark theme for reduced eye strain
- Responsive button layout
- Color-coded function categories
- Large, readable display

## 🔧 Customization

The calculator's appearance can be easily customized by modifying the stylesheets in `main.py`:
- Display colors and fonts
- Button colors and hover effects
- Window size and layout

## 🐛 Known Limitations

- Plotting range is fixed at x ∈ [-10, 10]
- Complex number plotting shows only real parts
- Some advanced SymPy features not exposed in UI

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [PySide6](https://wiki.qt.io/Qt_for_Python)
- Mathematical engine powered by [SymPy](https://www.sympy.org/)
- Plotting powered by [Matplotlib](https://matplotlib.org/)

## 📬 Contact

For questions or feedback, please open an issue on GitHub.

---

**Enjoy calculating!** 🎉
