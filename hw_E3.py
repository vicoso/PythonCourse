import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn import datasets

mpl.rcParams['figure.figsize'] = (12, 8)

figure = datasets.load_boston()
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
fig, axes = plt.subplots(nrows=1, ncols=2)
print(figure.feature_names)

axes[0].scatter(figure.data[:, 0], figure.target)
axes[0].set_xlabel('crime')
axes[0].set_ylabel('price')
axes[0].set_title('You think this bad neighborhood?')

axes[1].scatter(figure.data[:, 4], figure.target)
axes[1].set_xlabel('nox')
axes[1].set_ylabel('price')
axes[1].set_title('You think this bad neighborhood?')

fig.tight_layout()
fig.savefig('tmp.png')
