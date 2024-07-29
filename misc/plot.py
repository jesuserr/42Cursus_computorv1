#pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients of the polynomial (ax^2 + bx + c)
a = 1
b = -3
c = 2

# Create a range of x values
x = np.linspace(-10, 10, 400)

# Compute the corresponding y values
y = a * x**2 + b * x + c

# Plot the polynomial
plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('2nd Degree Polynomial')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('polynomial_plot.png')