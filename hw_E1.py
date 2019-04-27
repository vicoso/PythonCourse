#есть такой варинат, там ошибка invalid syntax, но я не оч поняла почему
import matplotlib.pyplot as plt
import numpy as np
n=np.random.poisson(10000)
fig, axes=plt.subplots(1, figsize=(12,4))
axes.hist(n)
axes.set_title('Poisson dstrb')
axes.set_xlim((min(str((n), max(str(n)))
plt.show()
                   
#и такой вариант, он вроде рабочй, но мня смущает, что он разрешил ему оси проиндексировать, потому что в каком-то лсучае у меня была ошибка, что их нельзя индексировать..
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
n=np.random.poisson(10, 10000)
fig, axes=plt.subplots(1, 2, figsize=(12,4))

axes[0].hist(n)
axes[0].set_title('poisson')
axes[0].set_xlim((min(n), max(n)))
plt.show()
