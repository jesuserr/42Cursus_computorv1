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
    
def plot(coefficients):
    a, b, c = coefficients[2], coefficients[1], coefficients[0]
    max_value = max(scale_calculator(a, b, c))
    min_value = min(scale_calculator(a, b, c))
    max_value *= SCALE if max_value > 0 else 1 / SCALE
    min_value *= SCALE if min_value < 0 else 1 / SCALE
    x_step = (max_value - min_value) / POINTS
    x_values = []
    y_values = []
    for i in range(POINTS):
        x = min_value + i * x_step
        x_values.append(x)
        y = a * x**2 + b * x + c
        y_values.append(y)
    #x_values = [min_value + i * x_step for i in range(POINTS)]
    #y_values = [a * x**2 + b * x + c for x in x_values]
    plt.plot(x_values, y_values, label=f'{c} + {b}x + {a}x²')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.xlim(x_values[0], x_values[POINTS - 1])
    plt.show()





