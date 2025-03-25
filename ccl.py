import numpy as np
import matplotlib.pyplot as plt


def ccl(map):
    h, w = map.shape
    res = np.zeros_like(map)
    counter = 0
    for yi in range(h):
        for xi in range(w):
            left = res[yi, xi - 1]
            top = res[yi - 1, xi]
            if map[yi, xi]:
                if yi == 0 and xi == 0:
                    counter += 1
                    res[yi, xi] = counter

                elif yi == 0:
                    if left:
                        res[yi, xi] = left
                    else:
                        counter += 1
                        res[yi, xi] = counter
                elif xi == 0:
                    if top:
                        res[yi, xi] = top
                    else:
                        counter += 1
                        res[yi, xi] = counter
                else:
                    if left and top:
                        res = np.where(res == top, left, res)
                        res[yi, xi] = left
                    elif left:
                        res[yi, xi] = left
                    elif top:
                        res[yi, xi] = top
                    else:
                        counter += 1
                        res[yi, xi] = counter
    return res


map = np.random.randint(0, 2, (20, 20))

_, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(map, 'gray')
ax2.imshow(ccl(map), 'inferno')
plt.show()
