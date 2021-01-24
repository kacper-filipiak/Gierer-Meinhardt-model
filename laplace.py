import numpy as np
array = np.zeros((5,5))
array[2,2] = 10
print(array)

print(np.gradient(array))
from scipy.ndimage import generic_laplace
