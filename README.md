# ComputorV1 - Polynomial Equation Solver

A Python-based polynomial equation solver handling first and second-degree polynomial equations. Part of the 42 curriculum.

## Features

- **Equation Parsing**: Flexible parsing for various input formats
- **Polynomial Reduction**: Displays equations in canonical reduced form
- **Degree Detection**: Determines polynomial degree automatically
- **Solution Computation**: Linear and quadratic equations with real and complex solutions
- **Irreducible Fractions**: Display solutions as fractions (`-i` flag)
- **Step-by-Step Solution**: Show intermediate calculation steps (`-s` flag)
- **Graphical Visualization**: Plot polynomial equations (`-p` flag)
- **Robust Validation**: Comprehensive error checking

## Installation

### Prerequisites
- Python 3.x
- matplotlib (for plotting)

### Setup
```bash
git clone https://github.com/jesuserr/42Cursus_computorv1
cd 42Cursus_computorv1

# Install matplotlib (optional, for plotting)
# Debian/Ubuntu (system packages):
sudo apt update
sudo apt install -y python3 python3-pip python3-matplotlib
```

## Usage

### Basic Syntax
```bash
python3 computor.py "equation" [OPTIONS]
```

### Options
- `-p`: Display graphical plot
- `-s`: Show calculation steps  
- `-i`: Display solutions as irreducible fractions

### Equation Format
Format: `a * X^n + b * X^m + ... = c * X^k + ...`
- Variables: `X` or `x`
- Spaces optional
- Coefficients: integers or decimals
- Powers: non-negative integers

### Examples
```bash
python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
python3 computor.py "3*x^2-10*x+7=0" -s
python3 computor.py "x^2-4*x+4=0" -i
python3 computor.py "x^2-4*x+5=0" -p
python3 computor.py "2*x^2-5*x+3=0" -s -i -p
```

## Project Structure

```
42Cursus_computorv1/
├── computor.py          # Main entry point
├── tester.sh            # Test script
├── srcs/
│   ├── parser.py        # Equation parsing and validation
│   ├── solver.py        # Solution calculation
│   ├── plot.py          # Graphical visualization
│   └── utils.py         # Helper functions
└── subject/
    └── en.subject.pdf   # Requirements
```

## How It Works

### Parsing (parser.py)
- Validates input characters and sequences using regex pattern matching
- Splits equation into left and right sides
- Extracts coefficients and powers
- Supports multiple free form entries

**Regex Learning**: One of the biggest learnings of this project has been discovering regular expressions (regex). Regex allows pattern matching in strings, which is crucial for parsing user input. For example, patterns like `\d+\.?\d*` match numbers with optional decimals, while `[a-zA-Z]` matches any letter. The `re` module in Python enables flexible validation and extraction of terms from equations without writing complex conditional logic, making the code cleaner and more maintainable (although patterns are more difficult to read by humans).

### Solving (solver.py)
- Displays equation in canonical form
- Determines polynomial degree (0, 1, or 2)
- **Linear**: `x = -b/a`
- **Quadratic**: Uses discriminant `Δ = b² - 4ac`
  - `Δ > 0`: Two distinct real solutions
  - `Δ = 0`: Two identical real solutions
  - `Δ < 0`: Two complex conjugate solutions

### Visualization (plot.py)
- Plots polynomial function on 2D graph
- Marks real solutions on x-axis
- Automatically scales axes

## Examples Output

### Two Real Solutions

```bash
$ python3 computor.py "3 * X^0 -5 * X^1 + 2 * X^2 = 0"
Reduced form: 3 * X^0 - 5 * X^1 + 2 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
1
1.5
```

### Two Identical Solutions
```bash
$ python3 computor.py "4 * X^0 - 4 * X^1 + 1 * X^2 = 0"
Reduced form: 4 * X^0 - 4 * X^1 + 1 * X^2 = 0
Polynomial degree: 2
Discriminant is zero, the two solutions are identical:
2
2
```

### Complex Solutions
```bash
$ python3 computor.py "5 * X^0 - 4 * X^1 + 1 * X^2 = 0"
Reduced form: 5 * X^0 - 4 * X^1 + 1 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly negative, the two complex solutions are:
2.000000000-1.000000000j
2.000000000+1.000000000j
```

### Linear Equation
```bash
$ python3 computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"
Reduced form: 1 * X^0 + 4 * X^1 = 0
Polynomial degree: 1
The solution is:
-0.25
```

## Testing

```bash
./tester.sh           # All tests
./tester.sh -s        # Show steps
./tester.sh -i        # Show fractions
./tester.sh -p        # Show plots
```

Test coverage includes: two real solutions, identical solutions, complex solutions, linear equations, higher degrees, infinite/inconsistent equations, and various formats.

## Error Handling

- Invalid characters or digit separation
- Non-integer exponents
- Polynomial degree > 2
- Inconsistent equations (e.g., `5 = 0`)
- Division by zero
- Infinite solutions (e.g., `0 = 0`)

## Mathematical Formulas

**Quadratic Formula**: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

**Discriminant**: $\Delta = b^2 - 4ac$

**Complex Solutions** (Δ < 0): $x = \frac{-b}{2a} \pm i\frac{\sqrt{|\Delta|}}{2a}$

## Key Implementation Details

- **Modular Architecture**: Separated parsing, solving, plotting, and utilities
- **Flexible Parsing**: Accepts various input formats
- **Clear Output**: Well-formatted with labels
- **Precision**: Python float precision with trailing zero stripping
- **Limitations**: Max degree 2, non-negative integer exponents, no symbolic computation
