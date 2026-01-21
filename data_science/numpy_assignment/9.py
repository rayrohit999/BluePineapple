'''
-Generate synthetic data:
    X: 200 samples, 1 feature (random)
    y = 3*X + 5 + noise
-Fit using closed-form normal equation (no sklearn).
-Print estimated slope and intercept.
'''
import numpy as np

# Seting random seed for reproducibility
np.random.seed(42)

# Generating synthetic data
n_samples = 200
X = np.random.rand(n_samples, 1)        
noise = np.random.randn(n_samples, 1)
y = 3 * X + 5 + noise                

# Fitting using Closed-form formula
X_sum = np.sum(X)
y_sum = np.sum(y)
XX_sum = np.sum(X * X)
XY_sum = np.sum(X * y)

denominator = n_samples * XX_sum - X_sum ** 2

b = (n_samples * XY_sum - X_sum * y_sum) / denominator  # slope
a = (y_sum - b * X_sum) / n_samples  # intercept

print(f"Estimated intercept (a): {a}")
print(f"Estimated slope (b): {b}")
print(f"Equation: y = {a:.3f} + {b:.3f}X")
