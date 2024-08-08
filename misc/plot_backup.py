import numpy as np
import matplotlib.pyplot as plt

SCALE = 2
POINTS = 400

def plot(coefficients):
    a, b, c = coefficients[2], coefficients[1], coefficients[0]
    max_value = max(scale_calculator(a, b, c))
    min_value = min(scale_calculator(a, b, c))
    x_values = np.linspace(min_value, max_value, POINTS)
    y_values = a * x_values**2 + b * x_values + c    
    plt.plot(x_values, y_values, label=f'{c} + {b}x + {a}x²')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.show()

def scale_calculator(a, b, c):
    if a != 0:
        plt.title('2nd Degree Polynomial')
        discriminant = (b ** 2) - (4 * a *c)
        numerator1 = -b - (discriminant) ** 0.5
        numerator2 = -b + (discriminant) ** 0.5
        denominator = 2 * a
        if discriminant == 0:
            numerator2 *= -1
        elif discriminant < 0:
            return SCALE * -b / denominator, SCALE * b / denominator
        return SCALE * numerator1 / denominator, SCALE * numerator2 / denominator
    else:
        plt.title('1st Degree Polynomial')
        return SCALE * c / -b, SCALE * c / b




