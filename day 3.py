# %% [markdown]
# # 🐍 NumPy Core Concepts & Revision Guide
# **Topics Covered:** Vectorized Operations, Broadcasting Rules, Aggregations, Axis Operations, and Boolean Masking Logic.

# ---

# %% [markdown]
# ## 1. Vectorized Operations & Element-Wise Math
# Vectorization applies operations to entire arrays at once without explicit loops.

# %%
import numpy as np

array = np.array([1.1, 2.2, 3.3, 4.4])

# Basic Universal Functions (ufuncs)
print("Original Array: ", array)
print("Square Root:    ", np.sqrt(array))
print("Power / Square: ", np.square(array))
print("Addition:       ", np.add(array, array))
print("Subtraction:    ", np.subtract(array, array))
print("Multiplication: ", np.multiply(array, array))
print("Division:       ", np.divide(array, array))
print("Modulus:        ", np.mod(array, array))

# Rounding & Trigonometry
print("\n--- Rounding & Trig ---")
print("Round: ", np.round(array))
print("Floor: ", np.floor(array))
print("Ceil:  ", np.ceil(array))
print("Sin:   ", np.sin(array))
print("Sinh:  ", np.sinh(array))

# Geometric calculations using constants
pi = np.pi
radii = np.array([1, 2, 3, 4])
areas = pi * (radii ** 2)
print("\nCircle Areas:", areas)

# %% [markdown]
# ## 2. Broadcasting Rules & Array Shapes
# Broadcasting stretches smaller arrays across larger arrays without copying data.
# * **Rule:** Two dimensions are compatible if they are equal OR if one of them is `1`.

# %%
array1 = np.array([[1, 2, 3, 4]])  # Shape: (1, 4) -> Row Vector
array2 = np.array([[5], [6], [7], [8]])  # Shape: (4, 1) -> Column Vector

print("Shape of array1:", array1.shape)
print("Shape of array2:", array2.shape)

# Broadcasting Result Shape: (4, 4)
broadcast_result = array1 * array2
print("\nBroadcasting Result (Outer Product Grid):\n", broadcast_result)

# %% [markdown]
# ## 3. Aggregations & Axis Operations
# Summary statistics across the entire array or specific axes.
# * `axis=0`: Operations down columns (vertical)
# * `axis=1`: Operations across rows (horizontal)

# %%
grid = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Total Sum:", np.sum(grid))
print("Mean:     ", np.mean(grid))
print("Variance: ", np.var(grid))      # Var = Σ(x - μ)² / N
print("Std Dev:  ", np.std(grid))      # Std = √Variance
print("Max Value:", np.max(grid))
print("Min Value:", np.min(grid))

# Argmin / Argmax return the flattened index of min/max values
print("\nIndex of Min (Argmin):", np.argmin(grid)) # Index 0 -> value 1
print("Index of Max (Argmax):", np.argmax(grid)) # Index 11 -> value 12

# Axis-based Aggregations
print("\nColumn-wise Sum (axis=0):", np.sum(grid, axis=0)) # [1+5+9, 2+6+10, ...]
print("Row-wise Sum    (axis=1):", np.sum(grid, axis=1)) # [1+2+3+4, ...]

# %% [markdown]
# ## 4. Application: Boolean Masking & Leap Year Calculator
# Using vectorized conditionals `&` (AND), `|` (OR) to filter data without `if` statements.

# %%
ages = np.array([22, 34, 12, 45, 35, 88, 2, 20, 55, 67, 1026])
current_year = 2026

# Vectorized birth year calculation
birth_years = current_year - ages

# Leap Year Condition: (divisible by 4 AND NOT by 100) OR (divisible by 400)
is_leap_year = (birth_years % 4 == 0) & ((birth_years % 100 != 0) | (birth_years % 400 == 0))

# Boolean Masking to filter arrays
leap_year_ages = ages[is_leap_year]
leap_birth_years = birth_years[is_leap_year]

print("Original Ages:      ", ages)
print("Calculated Births:  ", birth_years)
print("\n--- Filtered Leap Year Results ---")
print("Birth Years: ", leap_birth_years)
print("Ages:        ", leap_year_ages)
