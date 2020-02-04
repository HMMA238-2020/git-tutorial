import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x_gaussian = mu + sigma * np.random.randn(10000)

np.savetxt('file_data.csv', x_gaussian, delimiter=',')
