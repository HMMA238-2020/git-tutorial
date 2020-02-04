import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('file_data.csv')

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='k', alpha=0.25)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=5$ but this is no longer a Gaussian')
plt.xlim(40, 250)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
