import matplotlib.pyplot as plt
import numpy as np
n=np.random.poisson(10000)
fig, axes=plt.subplots(1, figsize=(12,4))
axes.hist(n)
axes.set_title('Poisson dstrb')
axes.set_xlim((min(str((n), max(str(n)))
plt.show()
