print("\n \n Probability distribution ")


### Binomial Distribution
from scipy.stats import binom #scientific python-binomial
import matplotlib.pyplot as plt  # Graph, charts

num_trials = 10
heads_probability = 0.5

probs = [binom.pmf(i, num_trials, heads_probability) for i in range(11)] #probability mass function 
plt.stem(list(range(11)), probs)
plt.show()


### Poisson distribution
from scipy.stats import poisson
import matplotlib.pyplot as plt

rate = 3.3

probs = [poisson.pmf(i, rate) for i in range(15)]  # probability mass function
plt.stem(list(range(15)), probs)
plt.show()
