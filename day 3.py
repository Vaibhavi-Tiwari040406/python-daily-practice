# %% [markdown]
# # 🐍 NumPy Revision & Quick Reference Guide
# **Topic:** Core NumPy Operations for Data Science & Computing  
# **Format:** Revision Notes + Executable Code  

# ---

# %% [markdown]
# ## 1. Fundamentals & Array Creation
# * NumPy arrays (`ndarray`) are homogeneous, N-dimensional, and memory-efficient compared to Python lists.

# %%
import numpy as np

# Creating 1D and 2D arrays
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Built-in initializers
zeros = np.zeros((2, 3))        # 2x3 matrix of 0s
ones = np.ones((3, 3))          # 3x3 matrix of 1s
identity = np.eye(3)            # 3x3 Identity matrix
ranged = np.arange(0, 10, 2)    # Start, Stop (exclusive), Step -> [0, 2, 4, 6, 8]
linear_space = np.linspace(0, 1, 5) # 5 evenly spaced numbers from 0 to 1

print("1D Shape:", arr_1d.shape)
print("2D Shape & Data Type:", arr_2d.shape, "|", arr_2d.dtype)

# %% [markdown]
# ## 2. Array Attributes & Reshaping
# * **Key Rule:** Reshaping requires the total number of elements to remain constant ($N_{\text{old}} = N_{\text{new}}$).

# %%
arr = np.arange(12) # [0, 1, ..., 11]

# Reshaping 1D -> 3x4 Matrix
matrix_3x4 = arr.reshape(3, 4)

# Flattening back to 1D
flattened = matrix_3x4.flatten()

# Transpose
transposed = matrix_3x4.T

print("Reshaped (3x4):\n", matrix_3x4)
print("\nTransposed (4x3):\n", transposed)

# %% [markdown]
# ## 3. Indexing, Slicing & Boolean Masking
# * NumPy uses zero-based indexing and supports multi-dimensional slicing `[row_slice, col_slice]`.
# * **Boolean Masking** is essential for filtering data based on conditions.

# %%
data = np.array([10, 20, 30, 40, 50, 60])

# Basic Slicing [start:stop:step]
subset = data[1:4] # [20, 30, 40]

# Filtering / Boolean Masking
mask = data > 30
filtered_data = data[mask] # Elements greater than 30

print("Filtered (>30):", filtered_data)

# Modifying elements conditionally
data[data < 30] = 0
print("Modified Array:", data)

# %% [markdown]
# ## 4. Vectorized Operations & Broadcasting
# * **Vectorization:** Operations occur element-wise without explicit `for` loops.
# * **Broadcasting:** Allows arithmetic operations between arrays of different shapes under specific compatibility rules.

# %%
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Element-wise operations
add = a + b
square = a ** 2

# Broadcasting example (1D array + Scalar)
scaled = a * 10 

print("Element-wise Addition:", add)
print("Scaled Array:", scaled)

# %% [markdown]
# ## 5. Aggregations & Axis Operations
# * Aggregations compress arrays along specified axes:
#   * `axis=0`: Operations down the columns.
#   * `axis=1`: Operations across the rows.

# %%
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])

total_sum = np.sum(matrix)
col_sum = np.sum(matrix, axis=0)  # [1+4, 2+5, 3+6] -> [5, 7, 9]
row_sum = np.sum(matrix, axis=1)  # [1+2+3, 4+5+6] -> [6, 15]

mean_val = np.mean(matrix)
std_dev = np.std(matrix)

print(f"Column Sums: {col_sum} | Row Sums: {row_sum}")
print(f"Mean: {mean_val:.2f} | Standard Dev: {std_dev:.2f}")

# %% [markdown]
# ## 6. Random Sampling & Statistics
# * Useful for generating synthetic data, initializing weights, or sampling.

# %%
np.random.seed(42) # Reproducibility

rand_uniform = np.random.rand(3)      # Uniform distribution [0, 1)
rand_normal = np.random.randn(3)     # Standard Normal distribution (mean=0, std=1)
rand_integers = np.random.randint(1, 100, size=(2, 2)) # Random integers

print("Random Integers Matrix:\n", rand_integers)
