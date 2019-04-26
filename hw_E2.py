import matplotlib.pyplot as plt
import numpy as np
from numpy import *
n=np.random.pareto(100, 10000)
fig, axes=plt.subplots(1, 2, figsize=(12,4))

axes[0].hist(n)
axes[0].set_title('pareto')
axes[0].set_xlim((min(n), max(n)))
