import matplotlib.pyplot as plt
import numpy as np

class f:
    x = 0   # kuadrat
    y = 0   # linear
    z = 0   # konstanta

class g:
    x = 0   # kuadrat
    y = 0   # linear
    z = 0   # konstanta

def scanstr(string):
    x = string
    i = 0
    while i < len(x):
        if x[i] == 'x':
            if x[i+1] == '^' and x[i+2] == '2':
                f.x += 1
                i += 3
            else:
                f.y += 1
                i += 1
        elif x[i].isdigit():
            while x[i].isdigit():
                f.x = (f.x * 10) + int(x[i])
                i += 1
            if x[i] == 'x':
                if x[i+1] == '^' and x[i+2] == '2':
                    f.x += 1
                    i += 3
                else:
                    f.y += 1
                    i += 1
            
        elif x[i] == '+' or x[i] == '-' or x[i] == '*' or x[i] == '/':
            i += 1
        else:
            print("Invalid character")
            break
        i += 1

def integrate(argument):
    x = argument()

# Example usage:
    
input
# Generate x values
x = np.linspace(-10, 10, 100)

# Evaluate the function for each x value
y1 = 2*x
y2 = x**2 + 2*x + 1

# Plot the graph
plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x)')
plt.grid(True)
plt.show()

