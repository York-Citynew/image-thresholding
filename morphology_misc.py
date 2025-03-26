
from scipy.ndimage import generic_filter
import numpy as np

def dilation(image, shape, size):
    if shape == 'square':
        kernel = np.ones(size**2)
    else:
        y, x = np.ogrid[:size, :size]
        r = size//2
        kernel = ((x-r)**2 + (y-r)**2 <= r**2).ravel()
    return generic_filter(image,lambda image: bool(np.any(np.array(image)*kernel)),(size,size))

def erosion(image, shape, size):
    if shape == 'square':
        kernel = np.ones(size**2)
    else:
        y, x = np.ogrid[:size, :size]
        r = size//2
        kernel = ((x-r)**2 + (y-r)**2 <= r**2).ravel()
    return generic_filter(image,lambda image: np.sum(np.array(image)*kernel) == np.sum(kernel),(size,size))

opening = lambda image, shape, size: dilation(erosion(image, shape, size), shape, size)
closing = lambda image, shape, size: erosion(dilation(image, shape, size), shape, size)