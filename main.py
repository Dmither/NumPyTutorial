import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x1 = random.binomial(n=100, p=0.5, size=1000)
# x1 = random.binomial(n=100, p=0.5, size=1000)
# x2 = random.normal(loc=50, scale=5, size=1000)

sns.kdeplot(x1)
# sns.kdeplot(x2)
plt.show()